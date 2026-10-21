"""Exercise the generation entry point without Docker or generated-source edits."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent

# The per-language fixes that run after generation edit real generated files, which the fake
# generators here do not write, so each copy of the entry point gets empty stand-ins for them.
POST_PROCESSING_SCRIPTS = (
    "csharp-nullable-enums.py",
    "go-oneof-unreachable.py",
    "java-pom-publish.py",
    "license.py",
    "package-metadata.py",
    "php-root-manifest.py",
)


def copy_entry_point(root, *names):
    for name in ("generate.sh", "sdks.json", *names):
        shutil.copyfile(ROOT / name, root / name)
    scripts = root / "scripts"
    scripts.mkdir()
    for name in POST_PROCESSING_SCRIPTS:
        (scripts / name).write_text("")


class GeneratorExitStatusTest(unittest.TestCase):
    def run_generator(self, status, output):
        with tempfile.TemporaryDirectory(prefix="growwer-generation-test-") as directory:
            root = Path(directory)
            copy_entry_point(root)
            commands = root / "bin"
            commands.mkdir()
            docker = commands / "docker"
            docker.write_text(f"#!/bin/sh\nprintf '%s\\n' '{output}'\nexit {status}\n")
            docker.chmod(0o755)
            return subprocess.run(
                ["bash", "generate.sh", "typescript"],
                cwd=root,
                env={**os.environ, "PATH": f"{commands}:{os.environ['PATH']}"},
                capture_output=True,
                text=True,
                check=False,
            )

    def test_generator_failure_is_not_reported_as_success(self):
        result = self.run_generator(42, "[main] ERROR generation failed")
        self.assertEqual(42, result.returncode)
        self.assertIn("generation failed", result.stdout)
        self.assertNotIn("generated 1 sdk(s)", result.stdout)

    def test_docker_failure_keeps_its_diagnostic(self):
        result = self.run_generator(125, "docker: unavailable image")
        self.assertEqual(125, result.returncode)
        self.assertIn("docker: unavailable image", result.stdout)

    def test_success_without_warnings_is_success(self):
        result = self.run_generator(0, "[main] INFO generating")
        self.assertEqual(0, result.returncode)
        self.assertIn("generated 1 sdk(s)", result.stdout)


class GoTestRegenerationTest(unittest.TestCase):
    def run_generator(self, status):
        with tempfile.TemporaryDirectory(prefix="growwer-go-generation-test-") as directory:
            root = Path(directory)
            copy_entry_point(root)
            test = root / "go/test/api_analytics_test.go"
            test.parent.mkdir(parents=True)
            test.write_text("old two-result test")
            preserved = root / "go/consumer-note.txt"
            preserved.write_text("preserve existing files")
            commands = root / "bin"
            commands.mkdir()
            docker = commands / "docker"
            docker.write_text(
                f"#!{sys.executable}\n"
                "import pathlib, sys\n"
                "if 'generate' not in sys.argv: sys.exit(0)\n"
                "output = pathlib.Path(sys.argv[sys.argv.index('-o') + 1].removeprefix('/local/'))\n"
                "test = output / 'test/api_analytics_test.go'\n"
                "test.parent.mkdir(parents=True, exist_ok=True)\n"
                "if not test.exists():\n"
                "    test.write_text('updated three-result test github.com/viralitymedia/growwer-api-sdk/growwer')\n"
                f"sys.exit({status})\n"
            )
            docker.chmod(0o755)
            result = subprocess.run(
                ["bash", "generate.sh", "go"],
                cwd=root,
                env={**os.environ, "PATH": f"{commands}:{os.environ['PATH']}"},
                capture_output=True,
                text=True,
                check=False,
            )
            return result, test.read_text(), preserved.read_text(), list((root / ".generator-configs").glob("go.*"))

    def test_regeneration_refreshes_go_tests_and_preserves_existing_files(self):
        result, test, preserved, temporary_outputs = self.run_generator(0)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual("updated three-result test github.com/viralitymedia/growwer-api-sdk/go", test)
        self.assertEqual("preserve existing files", preserved)
        self.assertEqual(["go.json"], [path.name for path in temporary_outputs])

    def test_failed_generation_does_not_replace_existing_go_tests(self):
        result, test, preserved, temporary_outputs = self.run_generator(42)
        self.assertEqual(42, result.returncode)
        self.assertEqual("old two-result test", test)
        self.assertEqual("preserve existing files", preserved)
        self.assertEqual(["go.json"], [path.name for path in temporary_outputs])


FAKE_GENERATOR = (
    "import os, pathlib, sys\n"
    "if 'generate' not in sys.argv: sys.exit(0)\n"
    "output = pathlib.Path(sys.argv[sys.argv.index('-o') + 1].removeprefix('/local/'))\n"
    "names = [name for name in os.environ['FAKE_GENERATOR_FILES'].split(',') if name]\n"
    "for name in names:\n"
    "    path = output / name\n"
    "    path.parent.mkdir(parents=True, exist_ok=True)\n"
    "    path.write_text('generated github.com/viralitymedia/growwer-api-sdk/growwer')\n"
    # Written only when missing and listed only on the run that writes it, as the real generator
    # treats test stubs and .openapi-generator-ignore.
    "for name in os.environ.get('FAKE_GENERATOR_ONCE', '').split(','):\n"
    "    if name and not (output / name).exists():\n"
    "        (output / name).parent.mkdir(parents=True, exist_ok=True)\n"
    "        (output / name).write_text('written once')\n"
    "        names.append(name)\n"
    "listing = output / '.openapi-generator/FILES'\n"
    "listing.parent.mkdir(parents=True, exist_ok=True)\n"
    "listing.write_text(''.join(name + '\\n' for name in names))\n"
    # A failure is reported after part of the output, including a new list, has been written.
    "sys.exit(int(os.environ['FAKE_GENERATOR_STATUS']))\n"
)


class OrphanedFileTest(unittest.TestCase):
    """A file the previous run generated and this one did not is deleted; nothing else is."""

    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="growwer-orphan-test-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        copy_entry_point(self.root)
        commands = self.root / "bin"
        commands.mkdir()
        docker = commands / "docker"
        docker.write_text(f"#!{sys.executable}\n" + FAKE_GENERATOR)
        docker.chmod(0o755)
        self.path = f"{commands}:{os.environ['PATH']}"

    def previous_run(self, sdk, listed, unlisted=()):
        for name in (*(listed or ()), *unlisted):
            path = self.root / sdk / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"previous {name}")
        if listed is not None:
            listing = self.root / sdk / ".openapi-generator/FILES"
            listing.parent.mkdir(parents=True, exist_ok=True)
            listing.write_text("".join(f"{name}\n" for name in listed))

    def generate(self, sdk, emitted, status=0, once=()):
        return subprocess.run(
            ["bash", "generate.sh", sdk],
            cwd=self.root,
            env={
                **os.environ,
                "PATH": self.path,
                "FAKE_GENERATOR_FILES": ",".join(emitted),
                "FAKE_GENERATOR_ONCE": ",".join(once),
                "FAKE_GENERATOR_STATUS": str(status),
            },
            capture_output=True,
            text=True,
            check=False,
        )

    def assert_orphans_removed(self, sdk):
        self.previous_run(
            sdk,
            listed=["README.md", "docs/Removed.md", "models/removed/Removed.txt", "models/Kept.txt"],
            unlisted=["test/RemovedTest.txt", "notes.txt"],
        )
        result = self.generate(sdk, ["README.md", "models/Kept.txt", "docs/Added.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn(f"removed {sdk}/docs/Removed.md", result.stdout)
        self.assertIn(f"removed {sdk}/models/removed/Removed.txt", result.stdout)
        client = self.root / sdk
        self.assertFalse((client / "docs/Removed.md").exists())
        self.assertFalse((client / "models/removed").exists(), "an emptied directory is removed")
        for name in ("README.md", "models/Kept.txt", "docs/Added.md"):
            self.assertTrue((client / name).exists(), f"{name} is still generated")
        self.assertTrue((client / "docs").is_dir(), "a directory that still holds files is kept")
        # Not in the previous list, so not provably generated: a skipped test stub or a file
        # somebody added. Neither is the script's to delete.
        self.assertEqual("previous test/RemovedTest.txt", (client / "test/RemovedTest.txt").read_text())
        self.assertEqual("previous notes.txt", (client / "notes.txt").read_text())
        self.assertFalse(
            (self.root / f".generator-configs/{sdk}.FILES").exists(),
            "the copy of the previous list does not outlive the run",
        )

    def test_files_dropped_from_the_contract_are_removed(self):
        self.assert_orphans_removed("typescript")

    def test_go_removes_orphans_after_overlaying_the_temporary_output(self):
        self.assert_orphans_removed("go")

    def test_failed_generation_removes_nothing(self):
        self.previous_run("typescript", listed=["README.md", "docs/Removed.md"])
        result = self.generate("typescript", ["README.md"], status=42)
        self.assertEqual(42, result.returncode)
        # The failed run did write a list without docs/Removed.md, so only refusing to prune after a
        # failure keeps the file.
        self.assertEqual("README.md\n", (self.root / "typescript/.openapi-generator/FILES").read_text())
        self.assertTrue((self.root / "typescript/docs/Removed.md").exists())
        self.assertNotIn("removed", result.stdout)

    def test_a_first_generation_removes_nothing(self):
        self.previous_run("typescript", listed=None, unlisted=["notes.txt"])
        result = self.generate("typescript", ["README.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual("previous notes.txt", (self.root / "typescript/notes.txt").read_text())

    def test_paths_outside_the_client_are_never_removed(self):
        outside = self.root / "outside.txt"
        outside.write_text("not generated")
        absolute = self.root / "absolute.txt"
        absolute.write_text("not generated")
        self.previous_run("typescript", listed=["README.md"])
        listing = self.root / "typescript/.openapi-generator/FILES"
        listing.write_text(f"README.md\n../outside.txt\n{absolute}\n")
        result = self.generate("typescript", ["README.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertTrue(outside.exists())
        self.assertTrue(absolute.exists())

    def test_a_path_through_a_symlink_out_of_the_client_is_never_removed(self):
        outside = self.root / "elsewhere"
        outside.mkdir()
        (outside / "kept.txt").write_text("not generated")
        self.previous_run("typescript", listed=["README.md"])
        (self.root / "typescript/link").symlink_to(outside, target_is_directory=True)
        listing = self.root / "typescript/.openapi-generator/FILES"
        listing.write_text("README.md\nlink/kept.txt\n")
        result = self.generate("typescript", ["README.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual("not generated", (outside / "kept.txt").read_text())

    def test_an_unchanged_list_removes_nothing(self):
        self.previous_run("typescript", listed=["README.md", "docs/Kept.md"], unlisted=["test/Stub.txt"])
        result = self.generate("typescript", ["README.md", "docs/Kept.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertNotIn("removed", result.stdout)
        for name in ("README.md", "docs/Kept.md", "test/Stub.txt"):
            self.assertTrue((self.root / "typescript" / name).exists(), name)

    def test_an_orphan_already_gone_is_not_an_error(self):
        self.previous_run("typescript", listed=["README.md"])
        listing = self.root / "typescript/.openapi-generator/FILES"
        listing.write_text("README.md\ndocs/AlreadyDeleted.md\n")
        result = self.generate("typescript", ["README.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertNotIn("removed", result.stdout)

    def tree(self, sdk):
        client = self.root / sdk
        return {str(path.relative_to(client)): path.read_text() for path in client.rglob("*") if path.is_file()}

    def test_a_test_stub_written_only_when_missing_survives_every_later_run(self):
        # Where each generator puts its test stubs. Go writes them only when missing too, but it is
        # generated into an empty directory, so its stubs are written and listed on every run.
        stubs = {
            "python": "test/test_added_resource.py",
            "php": "test/Model/AddedResourceTest.php",
            "java": "src/test/java/com/growwer/api/model/AddedResourceTest.java",
            "csharp": "src/Growwer.Api.Test/Model/AddedResourceTests.cs",
            "ruby": "spec/models/added_resource_spec.rb",
            "go": "test/api_added_test.go",
        }
        for sdk, stub in stubs.items():
            with self.subTest(sdk=sdk):
                self.previous_run(sdk, listed=["README.md"])
                trees = []
                for run in (1, 2, 3):
                    result = self.generate(sdk, ["README.md"], once=[stub, ".openapi-generator-ignore"])
                    self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                    self.assertNotIn("removed", result.stdout, f"run {run}")
                    self.assertTrue((self.root / sdk / stub).is_file(), f"run {run} kept the stub")
                    trees.append(self.tree(sdk))
                self.assertEqual(set(trees[0]), set(trees[1]), "the second run changes no file set")
                self.assertEqual(trees[1], trees[2], "the third run changes nothing at all")

    def test_the_ignore_file_written_only_when_missing_is_never_removed(self):
        self.previous_run("typescript", listed=["README.md"])
        for run in (1, 2, 3):
            result = self.generate("typescript", ["README.md"], once=[".openapi-generator-ignore"])
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertTrue((self.root / "typescript/.openapi-generator-ignore").is_file(), f"run {run}")
        self.assertNotIn("removed", result.stdout)

    def test_the_test_stub_dir_protects_only_paths_inside_it(self):
        self.previous_run(
            "python",
            listed=["README.md", "test/test_removed.py", "test-requirements.txt", "testing/Removed.md", "docs/Removed.md"],
        )
        result = self.generate("python", ["README.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        client = self.root / "python"
        self.assertEqual("previous test/test_removed.py", (client / "test/test_removed.py").read_text())
        for name in ("test-requirements.txt", "testing/Removed.md", "docs/Removed.md"):
            self.assertFalse((client / name).exists(), f"{name} shares a prefix, not the directory")

    def test_each_test_stub_dir_holds_its_committed_stubs(self):
        for sdk in json.loads((ROOT / "sdks.json").read_text(encoding="utf-8"))["sdks"]:
            if "testStubDir" in sdk:
                with self.subTest(sdk=sdk["dir"]):
                    stub_dir = ROOT / sdk["dir"] / sdk["testStubDir"]
                    self.assertTrue(stub_dir.is_dir(), stub_dir)
                    self.assertTrue(any(path.is_file() for path in stub_dir.rglob("*")), stub_dir)

    def test_the_csharp_solution_with_its_random_project_guid_is_never_regenerated(self):
        csharp = ROOT / "csharp"
        patterns = (csharp / ".openapi-generator-ignore").read_text(encoding="utf-8").splitlines()
        self.assertIn("Growwer.Api.sln", patterns)
        self.assertTrue((csharp / "Growwer.Api.sln").is_file())
        self.assertNotIn("Growwer.Api.sln", (csharp / ".openapi-generator/FILES").read_text(encoding="utf-8").splitlines())

    def test_a_path_the_ignore_file_now_names_keeps_its_hand_edits(self):
        patterns = ["docs/Custom.md", "/docs/Custom.md", "docs/*.md", "docs/**", "docs/", "Custom.md", "**/Custom.md", "*.md"]
        for pattern in patterns:
            with self.subTest(pattern=pattern):
                shutil.rmtree(self.root / "typescript", ignore_errors=True)
                self.previous_run("typescript", listed=["README.md", "docs/Custom.md"])
                (self.root / "typescript/docs/Custom.md").write_text("edited by hand")
                (self.root / "typescript/.openapi-generator-ignore").write_text(
                    f"# OpenAPI Generator Ignore\n\n{pattern}\n"
                )
                result = self.generate("typescript", ["README.md"])
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                self.assertEqual("edited by hand", (self.root / "typescript/docs/Custom.md").read_text())
                self.assertNotIn("removed", result.stdout)

    def test_a_double_star_pattern_also_keeps_a_path_at_the_root(self):
        self.previous_run("typescript", listed=["README.md", "Custom.md"])
        (self.root / "typescript/Custom.md").write_text("edited by hand")
        (self.root / "typescript/.openapi-generator-ignore").write_text("**/Custom.md\n")
        result = self.generate("typescript", ["README.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual("edited by hand", (self.root / "typescript/Custom.md").read_text())
        self.assertNotIn("removed", result.stdout)

    def test_comments_blank_lines_negations_and_other_patterns_do_not_keep_an_orphan(self):
        self.previous_run("typescript", listed=["README.md", "docs/Removed.md"])
        (self.root / "typescript/.openapi-generator-ignore").write_text(
            "# docs/Removed.md\n\n   \n!docs/Removed.md\ndocs/Other.md\nRemoved.txt\nother/\n"
        )
        result = self.generate("typescript", ["README.md"])
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("removed typescript/docs/Removed.md", result.stdout)
        self.assertFalse((self.root / "typescript/docs/Removed.md").exists())


class ContractSyncTest(unittest.TestCase):
    """`--sync` writes the fetched contract in the committed layout, or not at all."""

    def sync(self, contract, curl_status=0, contract_url=None):
        """Runs `--sync` on a copy of the entry point. With `contract_url`, the real curl fetches that
        URL; otherwise a stand-in curl serves `contract`."""
        with tempfile.TemporaryDirectory(prefix="growwer-sync-test-") as directory:
            root = Path(directory)
            copy_entry_point(root, "openapi.json")
            commands = root / "bin"
            commands.mkdir()
            (commands / "fetched.json").write_bytes(contract)
            env = {**os.environ, "PATH": f"{commands}:{os.environ['PATH']}"}
            if contract_url is None:
                curl = commands / "curl"
                curl.write_text(f"#!/bin/sh\ncat '{commands / 'fetched.json'}'\nexit {curl_status}\n")
                curl.chmod(0o755)
            else:
                env["GROWWER_CONTRACT_URL"] = contract_url.replace("{fetched}", str(commands / "fetched.json"))
            docker = commands / "docker"
            docker.write_text("#!/bin/sh\nexit 0\n")
            docker.chmod(0o755)
            result = subprocess.run(
                ["bash", "generate.sh", "--sync", "typescript"],
                cwd=root,
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
            return result, (root / "openapi.json").read_bytes(), (root / "openapi.json.new").exists()

    def test_an_unchanged_contract_reproduces_the_committed_file_byte_for_byte(self):
        committed = (ROOT / "openapi.json").read_bytes()
        # Served compact and ASCII-escaped, the opposite of the committed layout on both counts.
        served = json.dumps(json.loads(committed), ensure_ascii=True, separators=(",", ":")).encode()
        self.assertNotEqual(committed, served)
        result, written, leftover = self.sync(served)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual(committed, written)
        self.assertFalse(leftover)

    def test_a_changed_contract_changes_only_the_lines_it_changed(self):
        committed = (ROOT / "openapi.json").read_bytes()
        contract = json.loads(committed)
        version = contract["info"]["version"]
        contract["info"]["version"] = f"{version}-changed"
        served = json.dumps(contract, ensure_ascii=True, separators=(",", ":")).encode()
        result, written, _ = self.sync(served)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        before = committed.decode("utf-8").splitlines()
        after = written.decode("utf-8").splitlines()
        self.assertEqual(len(before), len(after))
        changed = [(old, new) for old, new in zip(before, after) if old != new]
        self.assertEqual(1, len(changed), changed)
        self.assertIn(f'"version": "{version}-changed"', changed[0][1])

    def test_non_ascii_text_is_written_unescaped(self):
        contract = {
            "openapi": "3.0.0",
            "info": {"title": "Señal de marca — ñandú ✓", "version": "1"},
            "paths": {f"/projects/{number}": {"get": {"summary": "Visibilidad en búsqueda"}} for number in range(60)},
        }
        served = json.dumps(contract, ensure_ascii=True, separators=(",", ":")).encode()
        self.assertTrue(served.isascii())
        result, written, leftover = self.sync(served)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual((json.dumps(contract, indent=2, ensure_ascii=False) + "\n").encode(), written)
        self.assertIn("Señal de marca — ñandú ✓".encode(), written)
        self.assertFalse(leftover)

    def test_a_contract_that_lost_its_operations_is_refused(self):
        committed = (ROOT / "openapi.json").read_bytes()
        gutted = json.dumps({"openapi": "3.0.0", "paths": {"/health": {"get": {}}}}).encode()
        result, written, leftover = self.sync(gutted)
        self.assertEqual(1, result.returncode)
        self.assertIn("published only 1 operations", result.stderr)
        self.assertEqual(committed, written)
        self.assertFalse(leftover)

    def test_a_contract_dumped_to_disk_is_synced_through_a_file_url(self):
        committed = (ROOT / "openapi.json").read_bytes()
        dumped = json.dumps(json.loads(committed), ensure_ascii=True, separators=(",", ":")).encode()
        result, written, leftover = self.sync(dumped, contract_url="file://{fetched}")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("fetching file://", result.stdout)
        self.assertEqual(committed, written)
        self.assertFalse(leftover)

    def test_a_missing_file_keeps_the_committed_contract(self):
        committed = (ROOT / "openapi.json").read_bytes()
        result, written, leftover = self.sync(b"", contract_url="file://{fetched}.missing")
        self.assertNotEqual(0, result.returncode)
        self.assertEqual(committed, written)
        self.assertFalse(leftover)

    def test_the_operation_floor_is_sixty(self):
        def contract(operations):
            paths = {f"/projects/{number}": {"get": {}} for number in range(operations)}
            return json.dumps({"openapi": "3.0.0", "info": {"title": "t", "version": "1"}, "paths": paths}).encode()

        result, written, leftover = self.sync(contract(59))
        self.assertEqual(1, result.returncode)
        self.assertIn("published only 59 operations", result.stderr)
        self.assertEqual((ROOT / "openapi.json").read_bytes(), written)
        self.assertFalse(leftover)

        result, written, _ = self.sync(contract(60))
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("openapi.json updated (60 operations)", result.stdout)
        self.assertEqual(60, len(json.loads(written)["paths"]))

    def test_the_committed_contract_meets_the_floor_and_names_the_production_host(self):
        contract = json.loads((ROOT / "openapi.json").read_text(encoding="utf-8"))
        methods = {"get", "post", "put", "patch", "delete"}
        operations = [
            operation
            for item in contract["paths"].values()
            for method, operation in item.items()
            if method in methods
        ]
        self.assertGreaterEqual(len(operations), 60)
        self.assertEqual(len(operations), len({operation["operationId"] for operation in operations}))
        self.assertEqual("https://tool.growwer.com", contract["servers"][0]["url"])

    def test_a_failed_fetch_keeps_the_committed_contract(self):
        committed = (ROOT / "openapi.json").read_bytes()
        result, written, leftover = self.sync(b"", curl_status=22)
        self.assertNotEqual(0, result.returncode)
        self.assertEqual(committed, written)
        self.assertFalse(leftover)


if __name__ == "__main__":
    unittest.main()
