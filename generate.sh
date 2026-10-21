#!/usr/bin/env bash
#
# Regenerates every client in this repository from openapi.json.
#
# Each client is generated whole from the contract, so there is nothing to port between languages
# and nothing to keep in sync by hand: adding a language means one entry in sdks.json, and a change
# to the API reaches all of them in the same run.
#
# Usage:
#   ./generate.sh                regenerate every SDK from the committed openapi.json
#   ./generate.sh python go      regenerate only these
#   ./generate.sh --sync         fetch the live contract first, then regenerate everything
#
# --sync reads sdks.json's contractUrl, or GROWWER_CONTRACT_URL when it is set. The URL goes to
# curl, so a contract dumped to disk is synced with a file URL:
#
#   GROWWER_CONTRACT_URL=file:///absolute/path/openapi.json ./generate.sh --sync
#
# The fetch is opt-in on purpose. A regeneration that silently pulls a new contract turns a
# mechanical rerun into a content change nobody reviewed, and the diff runs to six figures of lines
# across seven languages — the one place a surprise must not hide.

set -euo pipefail

cd "$(dirname "$0")"

GENERATOR_VERSION=$(python3 -c 'import json; print(json.load(open("sdks.json"))["generatorVersion"])')
PACKAGE_VERSION=$(python3 -c 'import json; print(json.load(open("sdks.json"))["packageVersion"])')
CONTRACT_URL="${GROWWER_CONTRACT_URL:-$(python3 -c 'import json; print(json.load(open("sdks.json"))["contractUrl"])')}"
IMAGE="openapitools/openapi-generator-cli:v${GENERATOR_VERSION}"

GO_TOOLCHAIN=$(python3 -c 'import json; print(json.load(open("sdks.json"))["goToolchain"])')
GO_MODULE="github.com/viralitymedia/growwer-api-sdk/go"
GO_GENERATED_MODULE="github.com/viralitymedia/growwer-api-sdk/$(python3 -c '
import json
sdk = next(s for s in json.load(open("sdks.json"))["sdks"] if s["dir"] == "go")
print(sdk["config"]["packageName"])
')"

sync_contract() {
  echo "fetching ${CONTRACT_URL}"
  # Written in the committed file's layout — two-space indent, UTF-8 left unescaped — so a sync
  # changes only what the contract changed. `python3 -m json.tool` indents by four and escapes every
  # non-ASCII character, which rewrote the whole file on each run.
  curl --fail --silent --show-error "${CONTRACT_URL}" | python3 -c '
import json, sys
contract = json.loads(sys.stdin.buffer.read())
with open(sys.argv[1], "w", encoding="utf-8") as output:
    json.dump(contract, output, indent=2, ensure_ascii=False)
    output.write("\n")
' openapi.json.new

  local operations
  operations=$(python3 -c '
import json
methods = {"get", "post", "put", "patch", "delete"}
paths = json.load(open("openapi.json.new", encoding="utf-8")).get("paths", {})
print(sum(len(methods & set(item)) for item in paths.values()))
')

  # A contract that lost most of its surface is far more likely to be a misrouted response or a
  # half-booted container than a real change, and regenerating from it would gut every client here.
  if [[ "${operations}" -lt 60 ]]; then
    echo "contract published only ${operations} operations; refusing to overwrite" >&2
    rm -f openapi.json.new
    exit 1
  fi

  mv openapi.json.new openapi.json
  echo "openapi.json updated (${operations} operations)"
}

targets=()
for argument in "$@"; do
  case "${argument}" in
    --sync) sync_contract ;;
    -*) echo "unknown option: ${argument}" >&2; exit 1 ;;
    *) targets+=("${argument}") ;;
  esac
done

mapfile -t all_dirs < <(python3 -c '
import json
for sdk in json.load(open("sdks.json"))["sdks"]:
    print(sdk["dir"])
')

if [[ ${#targets[@]} -eq 0 ]]; then
  targets=("${all_dirs[@]}")
else
  for target in "${targets[@]}"; do
    if [[ ! " ${all_dirs[*]} " =~ " ${target} " ]]; then
      echo "unknown sdk: ${target} (known: ${all_dirs[*]})" >&2
      exit 1
    fi
  done
fi

mkdir -p .generator-configs

go_output=""
cleanup_go_output() {
  if [[ -n "${go_output}" ]]; then
    python3 -c 'import shutil, sys; shutil.rmtree(sys.argv[1])' "${go_output}"
  fi
}
trap cleanup_go_output EXIT

for target in "${targets[@]}"; do
  generator=$(python3 -c "
import json
sdk = next(s for s in json.load(open('sdks.json'))['sdks'] if s['dir'] == '${target}')
print(sdk['generator'])
")

  # The per-language config is derived rather than committed: the fields every language shares —
  # version, repository, user agent, licence — must not be able to disagree between seven copies.
  # Each generator spells the licence differently and two do not take one at all, so the shared
  # value is mapped onto whatever option that language actually has.
  python3 -c "
import json
manifest = json.load(open('sdks.json'))
sdk = next(s for s in manifest['sdks'] if s['dir'] == '${target}')
config = dict(sdk['config'])
config.update({
    'packageVersion': manifest['packageVersion'],
    'gitUserId': 'viralitymedia',
    'gitRepoId': 'growwer-api-sdk',
    'httpUserAgent': 'growwer-${target}/' + manifest['packageVersion'],
    'hideGenerationTimestamp': True,
})

# Three generators ignore packageVersion and read a name of their own, so a version bump that
# only set packageVersion would leave Java, TypeScript and Ruby on whatever they defaulted to.
version = manifest['packageVersion']
version_options = {
    'java': 'artifactVersion',
    'typescript-fetch': 'npmVersion',
    'ruby': 'gemVersion',
}
if sdk['generator'] in version_options:
    config[version_options[sdk['generator']]] = version

license = manifest['license']
license_options = {
    'java': {'licenseName': license['name'], 'licenseUrl': license['url']},
    'typescript-fetch': {'licenseName': license['name']},
    'php': {'licenseName': license['name']},
    'csharp': {'licenseId': license['name']},
    'ruby': {'gemLicense': license['name']},
}
config.update(license_options.get(sdk['generator'], {}))

# Left unset, these fall back to the generator's own name and site, which would publish every
# package as authored by OpenAPI Generator. Python takes its author from the contract's info.contact
# and TypeScript has no option at all; scripts/package-metadata.py covers both.
author = manifest['author']
description = manifest['description']
author_options = {
    'java': {
        'artifactDescription': description,
        'developerName': author['name'],
        'developerEmail': author['email'],
        'developerOrganization': author['organization'],
        'developerOrganizationUrl': author['url'],
    },
    'php': {
        'artifactUrl': 'https://github.com/viralitymedia/growwer-api-sdk',
        'developerOrganization': author['organization'],
        'developerOrganizationUrl': author['url'],
    },
    'csharp': {
        'packageAuthors': author['name'],
        'packageCompany': author['organization'],
        'packageTitle': config.get('packageName'),
        'packageDescription': description,
        'packageCopyright': 'Copyright (c) ' + author['organization'],
    },
    'ruby': {
        'gemAuthor': author['name'],
        'gemAuthorEmail': author['email'],
        'gemHomepage': 'https://github.com/viralitymedia/growwer-api-sdk',
        'gemSummary': description,
        'gemDescription': description,
    },
}
config.update(author_options.get(sdk['generator'], {}))

json.dump(config, open('.generator-configs/${target}.json', 'w'), indent=2)
"

  # A property whose name collides with something the generator itself declares has to be renamed
  # in that language's client. It is a CLI option rather than a config field, so it is assembled
  # here from the manifest.
  mapfile -t name_mappings < <(python3 -c "
import json
sdk = next(s for s in json.load(open('sdks.json'))['sdks'] if s['dir'] == '${target}')
for source, renamed in sdk.get('nameMappings', {}).items():
    print(f'{source}={renamed}')
")

  mapping_args=()
  if [[ ${#name_mappings[@]} -gt 0 ]]; then
    mapping_args=(--name-mappings "$(IFS=,; echo "${name_mappings[*]}")")
  fi

  output_dir="${target}"
  if [[ "${target}" == "go" ]]; then
    # Go API tests are deliberately not overwritten by OpenAPI Generator. Generate in an empty
    # directory so changed response signatures also update those tests, then overlay only after
    # successful generation. A generator failure leaves the existing client and tests intact.
    go_output=$(mktemp -d .generator-configs/go.XXXXXXXX)
    output_dir="${go_output}"
  fi

  # The generator records every file it writes in .openapi-generator/FILES but never deletes one it
  # no longer emits, so a schema or operation dropped from the contract leaves its model, docs and
  # tests behind — still compiled, and referring to code that no longer exists. The list from before
  # this run is kept so that whatever it named and this run did not can be removed afterwards.
  previous_files=".generator-configs/${target}.FILES"
  rm -f "${previous_files}"
  if [[ -f "${target}/.openapi-generator/FILES" ]]; then
    cp "${target}/.openapi-generator/FILES" "${previous_files}"
  fi

  echo "==> ${target} (${generator})"
  docker run --rm \
    -u "$(id -u):$(id -g)" \
    -v "$PWD:/local" \
    "${IMAGE}" \
    generate \
    -i /local/openapi.json \
    -g "${generator}" \
    -o "/local/${output_dir}" \
    -c "/local/.generator-configs/${target}.json" \
    "${mapping_args[@]}" \
    2>&1 | sed '/^\[main\] INFO /d'

  if [[ "${target}" == "go" ]]; then
    mkdir -p go
    cp -a "${go_output}/." go/
    cleanup_go_output
    go_output=""
  fi

  # Only a path the previous list named is ever deleted: a file it never named — one somebody added,
  # or one the generator never wrote — is left alone. Directories are removed only once deleting a
  # file has emptied them.
  #
  # FILES is not a complete inventory of the client, though. The generator writes a test stub and
  # .openapi-generator-ignore only when they are missing, and lists them only on the run that writes
  # them: a stub added in one run drops out of the next run's list without having been dropped from
  # the contract. Deleting it then would recreate it the run after, and the tree would never settle.
  # So nothing under the SDK's testStubDir in sdks.json is deleted, nor the ignore file itself, and
  # neither is a path the ignore file now names — the generator stopped writing it because somebody
  # took it over by hand, not because the contract dropped it. Go needs no testStubDir: it is
  # generated into an empty directory, so its stubs are written and listed on every run.
  python3 -c '
import fnmatch, json, pathlib, sys

target = sys.argv[1]
sdk = pathlib.Path(target).resolve()
previous_list = pathlib.Path(sys.argv[2])
current_list = sdk / ".openapi-generator" / "FILES"
if not previous_list.is_file() or not current_list.is_file():
    sys.exit(0)

manifest = next(s for s in json.load(open("sdks.json"))["sdks"] if s["dir"] == target)
stub_parts = pathlib.PurePosixPath(manifest["testStubDir"]).parts if "testStubDir" in manifest else None

ignore_file = sdk / ".openapi-generator-ignore"
ignore_patterns = []
if ignore_file.is_file():
    for line in ignore_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        # A negation only narrows what the patterns before it cover; skipping it keeps more files.
        if line and not line.startswith(("#", "!")):
            ignore_patterns.append(line)


def listed(path):
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def matches(path, pattern):
    # A pattern without a slash names a file or directory at any depth, as in .gitignore.
    name = path.name if "/" not in pattern else str(path)
    candidates = {pattern, pattern.replace("**/", "")}
    return any(name == candidate or fnmatch.fnmatchcase(name, candidate) for candidate in candidates)


def ignored(relative):
    # Matched generously: a pattern that could name the path keeps it, since deleting a file somebody
    # maintains by hand loses work and keeping one costs nothing.
    for pattern in ignore_patterns:
        pattern = pattern.lstrip("/")
        if pattern.endswith("/"):
            if any(matches(parent, pattern.rstrip("/")) for parent in relative.parents if parent.parts):
                return True
        elif matches(relative, pattern):
            return True
    return False


for name in sorted(listed(previous_list) - listed(current_list)):
    relative = pathlib.PurePosixPath(name)
    if relative.is_absolute() or ".." in relative.parts:
        continue
    if relative == pathlib.PurePosixPath(".openapi-generator-ignore"):
        continue
    if stub_parts and relative.parts[:len(stub_parts)] == stub_parts:
        continue
    if ignored(relative):
        continue
    path = sdk / relative
    if not path.parent.resolve().is_relative_to(sdk):
        continue
    if not (path.is_file() or path.is_symlink()):
        continue
    path.unlink()
    print(f"    removed {target}/{name}")
    directory = path.parent
    while directory != sdk and not any(directory.iterdir()):
        directory.rmdir()
        directory = directory.parent
' "${target}" "${previous_files}"
  rm -f "${previous_files}"

  if [[ " python typescript php " =~ " ${target} " ]]; then
    # These three manifests carry author, description or keyword text the generator writes from
    # its own templates with no option to replace it, so the packages would be published as the
    # work of OpenAPI Generator. Corrected here from sdks.json, before the PHP root manifest is
    # derived from php/composer.json.
    python3 scripts/package-metadata.py "${target}"
  fi

  if [[ "${target}" == "php" ]]; then
    # Packagist reads composer.json from the repository ROOT and has no notion of a package living
    # in a subdirectory — the same shape of problem Go has, and with no equivalent of Go's
    # directory-prefixed tags. So the published PHP manifest is the root one, derived here from the
    # generated php/composer.json rather than written by hand, because two manifests maintained
    # separately are two manifests that disagree.
    python3 scripts/php-root-manifest.py
    echo "    root composer.json <- php/composer.json"
  fi

  if [[ "${target}" == "java" ]]; then
    # Maven needs a deploy destination and the Java generator has no option that emits one, so the
    # generated pom cannot be published as it stands. The plugin that supplies it is injected here
    # rather than committed by hand, because a hand edit is discarded by the next run.
    python3 scripts/java-pom-publish.py
    python3 scripts/license.py java
  fi

  if [[ "${target}" == "python" ]]; then
    python3 scripts/license.py python
  fi

  if [[ "${target}" == "csharp" ]]; then
    # The csharp template ignores `nullable: true` on a required enum, so the null the contract
    # allows (Order.pendingAction) fails deserialisation. The `?` is added here after every run.
    python3 scripts/csharp-nullable-enums.py
  fi

  if [[ "${target}" == "go" ]]; then
    # Go has no package registry: the import path IS the repository URL plus the directory, so in a
    # monorepo it has to be ".../growwer-api-sdk/go". The generator derives the module path from
    # packageName, which is also the Go package name — and `go` is a keyword, so it cannot produce
    # that path. The module line and every generated file that echoes it are corrected here rather
    # than by hand, because a hand edit would be discarded by the next run.
    grep -rl "${GO_GENERATED_MODULE}" go \
      | xargs sed -i "s|${GO_GENERATED_MODULE}|${GO_MODULE}|g"
    echo "    module path -> ${GO_MODULE}"

    # The oneOf template repeats its no-match branch, which `go vet` rejects as unreachable code.
    python3 scripts/go-oneof-unreachable.py

    # The generated go.sum covers the client but not the generated tests, so `go build ./...`
    # fails on a fresh checkout with "no required module provides package". Tidying here keeps
    # that fix inside the generation step, where the next run reproduces it, instead of leaving a
    # manual `go mod tidy` that regeneration would silently undo.
    docker run --rm -u "$(id -u):$(id -g)" \
      -e GOCACHE=/tmp/go-build -e GOMODCACHE=/tmp/go-mod \
      -v "$PWD/go:/src" -w /src \
      "golang:${GO_TOOLCHAIN}-alpine" go mod tidy
  fi
done

echo
echo "generated ${#targets[@]} sdk(s) at version ${PACKAGE_VERSION}. Review the diff before committing."
