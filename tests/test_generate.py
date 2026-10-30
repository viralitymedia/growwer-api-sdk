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
    "csharp-optional-nullables.py",
    "go-oneof-unreachable.py",
    "java-pom-publish.py",
    "license.py",
    "package-metadata.py",
    "php-root-manifest.py",
    "ruby-oneof-unknown-keys.py",
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


class GoGenerationInputsTest(unittest.TestCase):
    """Go is generated into an empty directory and tidied afterwards; neither step may lose what the
    committed client pins."""

    FAKE_DOCKER = (
        "import os, pathlib, sys\n"
        "if 'generate' not in sys.argv:\n"
        "    with open(os.environ['FAKE_DOCKER_LOG'], 'a') as log:\n"
        "        log.write(sys.argv[-1] + '\\n')\n"
        "    sys.exit(0)\n"
        "output = pathlib.Path(sys.argv[sys.argv.index('-o') + 1].removeprefix('/local/'))\n"
        # Like the real generator, it skips every path the output directory's ignore file names.
        "ignore = output / '.openapi-generator-ignore'\n"
        "skipped = set(ignore.read_text().split()) if ignore.exists() else set()\n"
        "written = [name for name in ('README.md', 'client.go') if name not in skipped]\n"
        "for name in written:\n"
        "    (output / name).write_text('generated github.com/viralitymedia/growwer-api-sdk/growwer')\n"
        "(output / '.openapi-generator').mkdir(exist_ok=True)\n"
        "(output / '.openapi-generator/FILES').write_text(''.join(name + '\\n' for name in written))\n"
    )

    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="growwer-go-inputs-test-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        copy_entry_point(self.root)
        commands = self.root / "bin"
        commands.mkdir()
        docker = commands / "docker"
        docker.write_text(f"#!{sys.executable}\n" + self.FAKE_DOCKER)
        docker.chmod(0o755)
        self.log = self.root / "docker.log"
        self.env = {**os.environ, "PATH": f"{commands}:{os.environ['PATH']}", "FAKE_DOCKER_LOG": str(self.log)}
        (self.root / "go").mkdir()

    def generate(self):
        result = subprocess.run(
            ["bash", "generate.sh", "go"], cwd=self.root, env=self.env, capture_output=True, text=True, check=False
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        return self.log.read_text().splitlines()

    def test_a_path_the_committed_ignore_file_names_keeps_its_hand_edits(self):
        (self.root / "go/.openapi-generator-ignore").write_text("README.md\n")
        (self.root / "go/README.md").write_text("edited by hand")
        self.generate()
        self.assertEqual("edited by hand", (self.root / "go/README.md").read_text())
        self.assertEqual("generated github.com/viralitymedia/growwer-api-sdk/go", (self.root / "go/client.go").read_text())
        self.assertEqual("README.md\n", (self.root / "go/.openapi-generator-ignore").read_text())

    def test_tidy_keeps_the_testify_release_the_committed_go_mod_names(self):
        (self.root / "go/go.mod").write_text(
            "module github.com/viralitymedia/growwer-api-sdk/go\n\ngo 1.23\n\n"
            "require (\n\tgithub.com/stretchr/testify v1.11.1\n\tgopkg.in/validator.v2 v2.0.1\n)\n"
        )
        self.assertEqual(
            ["go mod edit -require=github.com/stretchr/testify@v1.11.1 && go mod tidy"], self.generate()
        )

    def test_a_first_generation_without_a_go_mod_tidies_unpinned(self):
        self.assertEqual(["go mod tidy"], self.generate())


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

    def sync(self, contract, curl_status=0, contract_url=None, arguments=("--sync", "typescript")):
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
                ["bash", "generate.sh", *arguments],
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

    def test_an_invalid_argument_is_refused_before_anything_is_fetched(self):
        committed = (ROOT / "openapi.json").read_bytes()
        served = json.dumps({"openapi": "3.0.0", "paths": {f"/p/{n}": {"get": {}} for n in range(60)}}).encode()
        for arguments in (("--sync", "bogus"), ("--sync", "--bogus"), ("--sync", "typescript", "bogus")):
            with self.subTest(arguments=arguments):
                result, written, leftover = self.sync(served, arguments=arguments)
                self.assertEqual(1, result.returncode)
                self.assertIn("unknown", result.stderr)
                self.assertNotIn("fetching", result.stdout)
                self.assertEqual(committed, written)
                self.assertFalse(leftover)

    def test_a_failed_fetch_keeps_the_committed_contract(self):
        committed = (ROOT / "openapi.json").read_bytes()
        result, written, leftover = self.sync(b"", curl_status=22)
        self.assertNotEqual(0, result.returncode)
        self.assertEqual(committed, written)
        self.assertFalse(leftover)


class RubyOneOfUnknownKeysTest(unittest.TestCase):
    """scripts/ruby-oneof-unknown-keys.py drops the oneOf check that refuses unknown keys, but only
    while every member stays distinguishable without it."""

    CHECK = (
        "              # raise if data contains keys that are not known to the model\n"
        "              raise if const.respond_to?(:acceptable_attributes) && "
        "!(data.keys - const.acceptable_attributes).empty?\n"
    )
    ONE_OF = (
        "            else\n"
        "{check}"
        "              model = const.build_from_hash(data)\n"
        "              return model if model\n"
        "            end\n"
    )

    def run_script(self, schemas, models):
        with tempfile.TemporaryDirectory(prefix="growwer-ruby-oneof-test-") as directory:
            root = Path(directory)
            (root / "scripts").mkdir()
            shutil.copyfile(ROOT / "scripts/ruby-oneof-unknown-keys.py", root / "scripts/ruby-oneof-unknown-keys.py")
            (root / "openapi.json").write_text(json.dumps({"components": {"schemas": schemas}}))
            folder = root / "ruby/lib/growwer/models"
            folder.mkdir(parents=True)
            for name, text in models.items():
                (folder / f"{name}.rb").write_text(text)
            result = subprocess.run(
                [sys.executable, "scripts/ruby-oneof-unknown-keys.py"],
                cwd=root,
                capture_output=True,
                text=True,
                check=False,
            )
            return result, {path.stem: path.read_text() for path in folder.glob("*.rb")}

    @staticmethod
    def schemas(post_required=("title", "links"), post_properties=None):
        return {
            "Order": {"properties": {"briefing": {"oneOf": [
                {"$ref": "#/components/schemas/PostBriefing"},
                {"$ref": "#/components/schemas/LinkAdditionBriefing"},
            ]}}},
            "PostBriefing": {
                "required": list(post_required),
                "properties": post_properties or {"title": {"type": "string"}, "links": {"type": "array"}},
            },
            "LinkAdditionBriefing": {
                "required": ["linkingFrom", "link"],
                "properties": {"linkingFrom": {"type": "string"}, "link": {"type": "object"}},
            },
        }

    def test_the_check_is_dropped_from_every_one_of_module_and_nothing_else_changes(self):
        unrelated = "class Project\n  # raise if data contains keys that are not known to the model\nend\n"
        result, models = self.run_script(
            self.schemas(),
            {
                "order_briefing": self.ONE_OF.format(check=self.CHECK),
                "seller_order_briefing": self.ONE_OF.format(check=self.CHECK),
                "project": unrelated,
            },
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual(self.ONE_OF.format(check=""), models["order_briefing"])
        self.assertEqual(self.ONE_OF.format(check=""), models["seller_order_briefing"])
        self.assertEqual(unrelated, models["project"])
        self.assertIn("order_briefing, seller_order_briefing", result.stdout)

    def test_a_generator_that_no_longer_emits_the_check_fails_the_run(self):
        result, models = self.run_script(self.schemas(), {"order_briefing": self.ONE_OF.format(check="")})
        self.assertNotEqual(0, result.returncode)
        self.assertIn("remove scripts/ruby-oneof-unknown-keys.py", result.stderr)

    def test_members_told_apart_only_by_the_check_fail_the_run_and_are_not_patched(self):
        cases = {
            "a required property the other member also declares": self.schemas(
                post_required=("link",),
                post_properties={"link": {"type": "object"}, "title": {"type": "string"}},
            ),
            "a required property that is nullable": self.schemas(
                post_required=("title",),
                post_properties={"title": {"type": "string", "nullable": True}},
            ),
            "no required property": self.schemas(post_required=()),
        }
        for case, schemas in cases.items():
            with self.subTest(case=case):
                result, models = self.run_script(schemas, {"order_briefing": self.ONE_OF.format(check=self.CHECK)})
                self.assertNotEqual(0, result.returncode)
                self.assertIn("PostBriefing requires no non-nullable property", result.stderr)
                self.assertEqual(self.ONE_OF.format(check=self.CHECK), models["order_briefing"])

    def test_the_committed_contract_keeps_every_one_of_member_distinguishable(self):
        with tempfile.TemporaryDirectory(prefix="growwer-ruby-oneof-test-") as directory:
            root = Path(directory)
            (root / "scripts").mkdir()
            shutil.copyfile(ROOT / "scripts/ruby-oneof-unknown-keys.py", root / "scripts/ruby-oneof-unknown-keys.py")
            shutil.copyfile(ROOT / "openapi.json", root / "openapi.json")
            folder = root / "ruby/lib/growwer/models"
            folder.mkdir(parents=True)
            (folder / "order_briefing.rb").write_text(self.ONE_OF.format(check=self.CHECK))
            result = subprocess.run(
                [sys.executable, "scripts/ruby-oneof-unknown-keys.py"],
                cwd=root,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_the_committed_ruby_client_has_no_one_of_check_left(self):
        for path in (ROOT / "ruby/lib/growwer/models").glob("*.rb"):
            self.assertNotIn("data.keys - const.acceptable_attributes", path.read_text(encoding="utf-8"), path.name)


class CSharpOptionalNullablesTest(unittest.TestCase):
    """scripts/csharp-optional-nullables.py makes the C# client leave an optional, nullable request
    property out of the body until it is set, instead of sending it as null."""

    @staticmethod
    def model(name, members):
        """A C# model shaped like the generator's: (JSON name, type, EmitDefaultValue) per member."""
        pascal = [json_name[:1].upper() + json_name[1:] for json_name, _, _ in members]
        arguments = ", ".join(f"{kind} {json_name} = default" for json_name, kind, _ in members)
        assignments = "".join(f"            this.{prop} = {json_name};\n" for prop, (json_name, _, _) in zip(pascal, members))
        declarations = "".join(
            "\n"
            "        /// <summary>\n"
            f"        /// Gets or Sets {prop}\n"
            "        /// </summary>\n"
            f"        [DataMember(Name = \"{json_name}\", EmitDefaultValue = {str(emit).lower()})]\n"
            f"        public {kind} {prop} {{ get; set; }}\n"
            for prop, (json_name, kind, emit) in zip(pascal, members)
        )
        return (
            "namespace Growwer.Api.Model\n"
            "{\n"
            f"    public partial class {name}\n"
            "    {\n"
            f"        public {name}({arguments})\n"
            "        {\n"
            f"{assignments}"
            "        }\n"
            f"{declarations}"
            "    }\n"
            "}\n"
        )

    @staticmethod
    def contract(body, schemas=None, media_type="application/json", responses=None):
        operation = {"operationId": "updateProject", "requestBody": {"content": {media_type: {"schema": body}}}}
        if responses is not None:
            operation["responses"] = responses
        return {"paths": {"/projects/{id}": {"patch": operation}}, "components": {"schemas": schemas or {}}}

    def run_script(self, contract, models, mappings=None, runs=1):
        with tempfile.TemporaryDirectory(prefix="growwer-csharp-nullables-test-") as directory:
            root = Path(directory)
            (root / "scripts").mkdir()
            shutil.copyfile(ROOT / "scripts/csharp-optional-nullables.py", root / "scripts/csharp-optional-nullables.py")
            (root / "openapi.json").write_text(json.dumps(contract))
            (root / "sdks.json").write_text(json.dumps({"inlineSchemaNameMappings": mappings or {}}))
            folder = root / "csharp/src/Growwer.Api/Model"
            folder.mkdir(parents=True)
            for name, text in models.items():
                (folder / f"{name}.cs").write_text(text)
            for _ in range(runs):
                result = subprocess.run(
                    [sys.executable, "scripts/csharp-optional-nullables.py"],
                    cwd=root,
                    capture_output=True,
                    text=True,
                    check=False,
                )
            return result, {path.stem: path.read_text() for path in folder.glob("*.cs")}

    PROJECT_BODY = {
        "type": "object",
        "required": ["title"],
        "properties": {
            "title": {"type": "string", "nullable": True},
            "language": {"type": "string"},
            "country": {"type": "string", "nullable": True},
        },
    }
    PROJECT_MEMBERS = [("title", "string", True), ("language", "string", False), ("country", "string", True)]

    def test_an_optional_nullable_property_is_sent_only_once_set_and_nothing_else_changes(self):
        result, models = self.run_script(
            self.contract(self.PROJECT_BODY),
            {"UpdateProjectRequest": self.model("UpdateProjectRequest", self.PROJECT_MEMBERS)},
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        original = self.model("UpdateProjectRequest", self.PROJECT_MEMBERS)
        expected = original.replace(
            "            this.Country = country;\n",
            "            // a null \"country\" leaves Country unset, so it is not sent\n"
            "            this._Country = country;\n"
            "            if (this.Country != null)\n"
            "            {\n"
            "                this._flagCountry = true;\n"
            "            }\n",
        ).replace(
            "        public string Country { get; set; }\n",
            "        public string Country\n"
            "        {\n"
            "            get { return _Country; }\n"
            "            set\n"
            "            {\n"
            "                _Country = value;\n"
            "                _flagCountry = true;\n"
            "            }\n"
            "        }\n"
            "        private string _Country;\n"
            "        private bool _flagCountry;\n"
            "\n"
            "        /// <summary>\n"
            "        /// Returns true once Country has been set, so that a property left unset is left out of\n"
            "        /// the request rather than sent as null, which the API reads as a value.\n"
            "        /// </summary>\n"
            "        /// <returns>true once Country has been set (boolean)</returns>\n"
            "        public bool ShouldSerializeCountry()\n"
            "        {\n"
            "            return _flagCountry;\n"
            "        }\n",
        )
        self.assertNotEqual(original, expected)
        self.assertEqual(expected, models["UpdateProjectRequest"])
        self.assertIn("optional nullables: UpdateProjectRequest.Country", result.stdout)

    def test_nested_inline_objects_array_items_references_and_pinned_names_are_followed(self):
        body = {
            "type": "object",
            "properties": {
                "linkAdditionOffer": {
                    "type": "object",
                    "nullable": True,
                    "properties": {"fee": {"allOf": [{"$ref": "#/components/schemas/MoneyOrNull"}]}},
                },
                "options": {
                    "type": "array",
                    "items": {"type": "object", "properties": {"note": {"type": "string", "nullable": True}}},
                },
                "owner": {"$ref": "#/components/schemas/Owner"},
                "pinned": {"type": "object", "properties": {"memo": {"type": "string", "nullable": True}}},
            },
        }
        schemas = {
            "MoneyOrNull": {"type": "object", "nullable": True, "properties": {"amount": {"type": "integer"}}},
            "Owner": {"type": "object", "properties": {"email": {"type": "string", "nullable": True}}},
            "Report": {"type": "object", "properties": {"comment": {"type": "string", "nullable": True}}},
        }
        responses = {"200": {"content": {"application/json": {"schema": {"$ref": "#/components/schemas/Report"}}}}}
        models = {
            "UpdateProjectRequest": self.model(
                "UpdateProjectRequest",
                [
                    ("linkAdditionOffer", "UpdateProjectRequestLinkAdditionOffer", True),
                    ("options", "List<UpdateProjectRequestOptionsInner>", False),
                    ("owner", "Owner", False),
                    ("pinned", "PinnedThing", False),
                ],
            ),
            "UpdateProjectRequestLinkAdditionOffer": self.model(
                "UpdateProjectRequestLinkAdditionOffer", [("fee", "MoneyOrNull", True)]
            ),
            "UpdateProjectRequestOptionsInner": self.model("UpdateProjectRequestOptionsInner", [("note", "string", True)]),
            "Owner": self.model("Owner", [("email", "string", True)]),
            "PinnedThing": self.model("PinnedThing", [("memo", "string", True)]),
            "Report": self.model("Report", [("comment", "string", True)]),
        }
        result, patched = self.run_script(
            self.contract(body, schemas, responses=responses),
            models,
            mappings={"updateProject_request_pinned": "PinnedThing"},
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        for name, prop in (
            ("UpdateProjectRequest", "LinkAdditionOffer"),
            ("UpdateProjectRequestLinkAdditionOffer", "Fee"),
            ("UpdateProjectRequestOptionsInner", "Note"),
            ("Owner", "Email"),
            ("PinnedThing", "Memo"),
        ):
            with self.subTest(model=name):
                self.assertIn(f"public bool ShouldSerialize{prop}()", patched[name])
        for prop in ("Options", "Owner", "Pinned"):
            self.assertNotIn(f"ShouldSerialize{prop}", patched["UpdateProjectRequest"])
        self.assertEqual(models["Report"], patched["Report"])

    def test_a_body_sent_as_form_fields_is_left_alone(self):
        models = {"UpdateProjectRequest": self.model("UpdateProjectRequest", self.PROJECT_MEMBERS)}
        result, patched = self.run_script(self.contract(self.PROJECT_BODY, media_type="multipart/form-data"), models)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("remove scripts/csharp-optional-nullables.py", result.stderr)
        self.assertEqual(models, patched)

    def test_a_second_run_over_its_own_output_changes_nothing(self):
        models = {"UpdateProjectRequest": self.model("UpdateProjectRequest", self.PROJECT_MEMBERS)}
        once_result, once = self.run_script(self.contract(self.PROJECT_BODY), models)
        twice_result, twice = self.run_script(self.contract(self.PROJECT_BODY), models, runs=2)
        self.assertEqual(0, once_result.returncode, once_result.stderr)
        self.assertEqual(0, twice_result.returncode, twice_result.stderr)
        self.assertEqual(once, twice)
        self.assertIn("optional nullables: already patched", twice_result.stdout)

    def test_a_property_without_its_model_fails_the_run(self):
        result, _ = self.run_script(self.contract(self.PROJECT_BODY), {})
        self.assertNotEqual(0, result.returncode)
        self.assertIn("no C# model UpdateProjectRequest.cs", result.stderr)
        self.assertIn("inlineSchemaNameMappings", result.stderr)

    def test_a_declaration_or_constructor_in_another_shape_fails_the_run_and_is_not_written(self):
        regular = self.model("UpdateProjectRequest", self.PROJECT_MEMBERS)
        cases = {
            "no property to patch": (
                regular.replace("public string Country { get; set; }", "public string Country { get; init; }"),
                "no optional, nullable property declaration for country",
            ),
            "no constructor assignment": (
                regular.replace("            this.Country = country;\n", ""),
                "expected one constructor assignment to Country, found 0",
            ),
            "a ShouldSerialize method of its own": (
                regular.replace("    }\n}\n", "        public bool ShouldSerializeCountry() { return true; }\n    }\n}\n"),
                "Country already has a ShouldSerializeCountry method",
            ),
        }
        for case, (text, message) in cases.items():
            with self.subTest(case=case):
                result, models = self.run_script(self.contract(self.PROJECT_BODY), {"UpdateProjectRequest": text})
                self.assertNotEqual(0, result.returncode)
                self.assertIn(message, result.stderr)
                self.assertEqual(text, models["UpdateProjectRequest"])

    def test_a_generator_that_already_leaves_these_properties_out_fails_the_run(self):
        members = [("title", "string", True), ("language", "string", False), ("country", "string", False)]
        models = {"UpdateProjectRequest": self.model("UpdateProjectRequest", members)}
        result, patched = self.run_script(self.contract(self.PROJECT_BODY), models)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("remove scripts/csharp-optional-nullables.py", result.stderr)
        self.assertEqual(models, patched)

    def test_an_inline_object_under_a_composition_fails_the_run(self):
        for keyword in ("oneOf", "anyOf", "allOf"):
            with self.subTest(keyword=keyword):
                part = {"type": "object", "properties": {"note": {"type": "string", "nullable": True}}}
                if keyword == "allOf":
                    part = {"properties": {"inner": part}}
                body = {"type": "object", keyword: [part]}
                result, _ = self.run_script(self.contract(body), {})
                self.assertNotEqual(0, result.returncode)
                self.assertIn(f"an inline object under {keyword} is not supported", result.stderr)

    def test_the_committed_csharp_client_leaves_no_optional_nullable_request_property_unpatched(self):
        folder = ROOT / "csharp/src/Growwer.Api/Model"
        models = {path.stem: path.read_text(encoding="utf-8") for path in folder.glob("*.cs")}
        result, patched = self.run_script(
            json.loads((ROOT / "openapi.json").read_text(encoding="utf-8")),
            models,
            mappings=json.loads((ROOT / "sdks.json").read_text(encoding="utf-8")).get("inlineSchemaNameMappings", {}),
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("already patched", result.stdout)
        self.assertEqual(models, patched)
        for name, prop in (
            ("UpdateProjectRequest", "Country"),
            ("UpdateSellerMediaRequest", "LinkAdditionOffer"),
            ("CreateSellerMediaRequest", "LinkAdditionOffer"),
        ):
            self.assertIn(f"public bool ShouldSerialize{prop}()", models[name], name)


class PythonDependencyFloorsTest(unittest.TestCase):
    """scripts/package-metadata.py raises the floors the generator writes into the four Python
    manifests to releases free of the open advisories, and adds the filelock floor tox needs."""

    GENERATED = {
        "pyproject.toml": (
            'keywords = ["OpenAPI", "OpenAPI-Generator", "Growwer API"]\n'
            'requires-python = ">={python}"\n'
            "\n"
            "dependencies = [\n"
            '  "urllib3 (>={urllib3},<3.0.0)",\n'
            '  "python-dateutil (>=2.8.2)",\n'
            "]\n"
            "\n"
            "[tool.poetry.group.dev.dependencies]\n"
            'pytest = ">= {pytest}"\n'
            'pytest-cov = ">= 2.8.1"\n'
            'tox = ">= 3.9.0"\n'
            "{filelock_toml}"
            'flake8 = ">= 4.0.0"\n'
        ),
        "setup.py": (
            'PYTHON_REQUIRES = ">= {python_setup}"\n'
            "REQUIRES = [\n"
            '    "urllib3 >= {urllib3}, < 3.0.0",\n'
            '    "python-dateutil >= 2.8.2",\n'
            "]\n"
            "\n"
            "setup(\n"
            '    keywords=["OpenAPI", "OpenAPI-Generator", "Growwer API"],\n'
            ")\n"
        ),
        "requirements.txt": "urllib3 >= {urllib3}, < 3.0.0\npython_dateutil >= 2.8.2\n",
        "test-requirements.txt": (
            "pytest >= {pytest}\npytest-cov >= 2.8.1\ntox >= 3.9.0\n{filelock_txt}flake8 >= 4.0.0\n"
        ),
    }
    # What openapi-generator 7.24.0 writes, before any floor is raised.
    GENERATOR_FLOORS = {
        "python": "3.9", "python_setup": "3.10", "urllib3": "2.6.3", "pytest": "8.4.2",
        "filelock_toml": "", "filelock_txt": "",
    }
    RAISED_FLOORS = {
        "python": "3.10", "python_setup": "3.10", "urllib3": "2.8.0", "pytest": "9.0.3",
        "filelock_toml": 'filelock = ">= 3.20.3"\n', "filelock_txt": "filelock >= 3.20.3\n",
    }

    def manifests(self, **floors):
        values = {**self.GENERATOR_FLOORS, **floors}
        return {name: text.format(**values) for name, text in self.GENERATED.items()}

    @staticmethod
    def expected_keywords(text):
        keywords = '["growwer", "api", "sdk", "seo", "link-building"]'
        return text.replace('["OpenAPI", "OpenAPI-Generator", "Growwer API"]', keywords)

    def run_script(self, manifests, runs=1):
        with tempfile.TemporaryDirectory(prefix="growwer-python-floors-test-") as directory:
            root = Path(directory)
            (root / "scripts").mkdir()
            shutil.copyfile(ROOT / "scripts/package-metadata.py", root / "scripts/package-metadata.py")
            shutil.copyfile(ROOT / "sdks.json", root / "sdks.json")
            folder = root / "python"
            folder.mkdir()
            for name, text in manifests.items():
                (folder / name).write_text(text, encoding="utf-8")
            results = [
                subprocess.run(
                    [sys.executable, "scripts/package-metadata.py", "python"],
                    cwd=root,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                for _ in range(runs)
            ]
            return results, {name: (folder / name).read_text(encoding="utf-8") for name in manifests}

    def test_generator_floors_below_the_advisories_are_raised_in_every_manifest(self):
        (result,), manifests = self.run_script(self.manifests(python_setup="3.9"))
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        expected = {
            name: self.expected_keywords(text.format(**self.RAISED_FLOORS))
            for name, text in self.GENERATED.items()
        }
        self.assertEqual(expected, manifests)
        self.assertIn("urllib3 >= 2.8.0, pytest >= 9.0.3, filelock >= 3.20.3", result.stdout)

    def test_a_second_run_over_its_own_output_changes_nothing(self):
        (first,), once = self.run_script(self.manifests())
        results, twice = self.run_script(self.manifests(), runs=2)
        for result in (first, *results):
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual(once, twice)
        self.assertEqual(1, twice["pyproject.toml"].count("filelock"))
        self.assertEqual(1, twice["test-requirements.txt"].count("filelock"))

    def test_a_higher_floor_a_later_generator_writes_is_kept(self):
        higher = {
            "python": "3.11", "python_setup": "3.11", "urllib3": "2.10.0", "pytest": "10.0",
            "filelock_toml": 'filelock = ">= 3.21.0"\n', "filelock_txt": "filelock >= 3.21.0\n",
        }
        (result,), manifests = self.run_script(self.manifests(**higher))
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        expected = {
            name: self.expected_keywords(text.format(**higher)) for name, text in self.GENERATED.items()
        }
        self.assertEqual(expected, manifests)

    def test_a_manifest_without_exactly_one_floor_or_anchor_line_fails_the_run(self):
        generated = self.manifests()
        cases = {
            "requirements.txt": "python_dateutil >= 2.8.2\n",
            # raise_floor refuses to guess which of two matching lines is the dependency.
            "setup.py": generated["setup.py"].replace(
                '    "python-dateutil >= 2.8.2",\n', '    "python-dateutil >= 2.8.2",\n    "urllib3 >= 2.6.3, < 3.0.0",\n'
            ),
            # add_floor has no tox line to put the filelock floor after.
            "test-requirements.txt": "pytest >= 8.4.2\npytest-cov >= 2.8.1\nflake8 >= 4.0.0\n",
        }
        for name, text in cases.items():
            with self.subTest(name):
                broken = {**generated, name: text}
                (result,), _ = self.run_script(broken)
                self.assertNotEqual(0, result.returncode)
                self.assertIn(name, result.stderr)

    def test_the_committed_python_manifests_carry_the_floors(self):
        python = ROOT / "python"
        pyproject = (python / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn('requires-python = ">=3.10"\n', pyproject)
        self.assertIn('  "urllib3 (>=2.8.0,<3.0.0)",\n', pyproject)
        self.assertIn('\npytest = ">= 9.0.3"\n', pyproject)
        self.assertIn('\nfilelock = ">= 3.20.3"\n', pyproject)
        setup = (python / "setup.py").read_text(encoding="utf-8")
        self.assertIn('PYTHON_REQUIRES = ">= 3.10"\n', setup)
        self.assertIn('    "urllib3 >= 2.8.0, < 3.0.0",\n', setup)
        self.assertIn("urllib3 >= 2.8.0, < 3.0.0\n", (python / "requirements.txt").read_text(encoding="utf-8"))
        test_requirements = (python / "test-requirements.txt").read_text(encoding="utf-8")
        self.assertIn("pytest >= 9.0.3\n", test_requirements)
        self.assertIn("filelock >= 3.20.3\n", test_requirements)


class TypeScriptPackageMetadataTest(unittest.TestCase):
    """scripts/package-metadata.py replaces the generator's author, description and keywords in
    typescript/package.json and declares the Node floor the package is tested on."""

    # The fields openapi-generator 7.24.0 writes that the script rewrites; it emits no `engines`.
    GENERATED = {
        "name": "@growwer/api",
        "version": "1.1.1",
        "description": "OpenAPI client for @growwer/api",
        "author": "OpenAPI-Generator",
        "license": "MIT",
        "devDependencies": {"typescript": "^4.0 || ^5.0"},
    }

    def run_script(self, package, runs=1):
        with tempfile.TemporaryDirectory(prefix="growwer-typescript-metadata-test-") as directory:
            root = Path(directory)
            (root / "scripts").mkdir()
            shutil.copyfile(ROOT / "scripts/package-metadata.py", root / "scripts/package-metadata.py")
            shutil.copyfile(ROOT / "sdks.json", root / "sdks.json")
            folder = root / "typescript"
            folder.mkdir()
            (folder / "package.json").write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
            results = [
                subprocess.run(
                    [sys.executable, "scripts/package-metadata.py", "typescript"],
                    cwd=root,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                for _ in range(runs)
            ]
            return results, (folder / "package.json").read_text(encoding="utf-8")

    def test_the_generated_manifest_gets_the_node_floor_and_the_growwer_metadata(self):
        (result,), text = self.run_script(self.GENERATED)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        package = json.loads(text)
        manifest = json.loads((ROOT / "sdks.json").read_text(encoding="utf-8"))
        self.assertEqual({"node": ">=22"}, package["engines"])
        self.assertEqual(manifest["description"], package["description"])
        self.assertNotIn("OpenAPI", package["author"])
        self.assertEqual(["growwer", "api", "sdk", "seo", "link-building"], package["keywords"])
        # The fields the script does not own stay exactly as the generator wrote them.
        for field in ("name", "version", "license", "devDependencies"):
            self.assertEqual(self.GENERATED[field], package[field])
        self.assertIn("engines node >=22", result.stdout)

    def test_a_second_run_over_its_own_output_changes_nothing(self):
        (first,), once = self.run_script(self.GENERATED)
        results, twice = self.run_script(self.GENERATED, runs=2)
        for result in (first, *results):
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual(once, twice)

    def test_the_committed_manifest_declares_the_floor_ci_tests(self):
        package = json.loads((ROOT / "typescript/package.json").read_text(encoding="utf-8"))
        self.assertEqual({"node": ">=22"}, package["engines"])
        # A floor the package claims but CI never runs is a claim nobody checked.
        ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        self.assertIn('node-version: ["22", "26"]\n', ci)


class WorkflowSecretTest(unittest.TestCase):
    """A secret expanded into a `run` script becomes part of the shell source, where quoting it is the
    script's job and a stray character can break or leak it; it is passed through `env` instead."""

    @staticmethod
    def run_scripts(text):
        scripts, block, indent = [], None, 0
        for line in text.splitlines():
            stripped = line.lstrip(" ")
            depth = len(line) - len(stripped)
            if block is not None:
                if stripped and depth <= indent:
                    scripts.append("\n".join(block))
                    block = None
                else:
                    block.append(line)
                    continue
            key = stripped.removeprefix("- ")
            if key.startswith("run:"):
                value = key.removeprefix("run:").strip()
                if value in ("|", ">", "|-", ">-"):
                    block, indent = [], depth
                else:
                    scripts.append(value)
        if block is not None:
            scripts.append("\n".join(block))
        return scripts

    def test_the_reader_finds_secrets_in_block_and_inline_scripts(self):
        text = (
            "steps:\n"
            "  - run: echo ${{ secrets.A }}\n"
            "  - env:\n"
            "      B: ${{ secrets.B }}\n"
            "    run: |\n"
            "      printf '%s' \"$B\"\n"
            "      echo ${{ secrets.C }}\n"
            "  - uses: x\n"
        )
        scripts = self.run_scripts(text)
        self.assertEqual(2, len(scripts))
        self.assertIn("secrets.A", scripts[0])
        self.assertIn("secrets.C", scripts[1])
        self.assertNotIn("secrets.B", "".join(scripts))

    def test_no_workflow_expands_a_secret_inside_a_run_script(self):
        for workflow in sorted((ROOT / ".github/workflows").glob("*.yml")):
            for script in self.run_scripts(workflow.read_text(encoding="utf-8")):
                self.assertNotIn("secrets.", script, f"{workflow.name}: {script}")


if __name__ == "__main__":
    unittest.main()
