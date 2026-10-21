"""Fails if any package manifest disagrees with sdks.json about the version being released.

The release is driven by one tag and the verify job already checks that tag against
sdks.json. That is not enough on its own: three generators ignore `packageVersion` and read an
option of their own — `artifactVersion`, `npmVersion`, `gemVersion` — so a bump that set only
packageVersion regenerated Java, TypeScript and Ruby at whatever they defaulted to, and a tagged
release would have republished a version those three registries already hold.

generate.sh now feeds all of them, which is the actual fix. This is the check that says so before
anything is uploaded, because the failure it guards against is the one the release workflow is
built to avoid: a version that exists in four registries and not in the other three.

PHP is absent on purpose. Packagist versions a package by the repository tag and a hardcoded
version field in composer.json only gives it something to contradict.
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

expected = json.loads((ROOT / "sdks.json").read_text(encoding="utf-8"))["packageVersion"]


def from_json(path, *keys):
    value = json.loads((ROOT / path).read_text(encoding="utf-8"))
    for key in keys:
        value = value[key]
    return value


def from_pattern(path, pattern):
    match = re.search(pattern, (ROOT / path).read_text(encoding="utf-8"), re.MULTILINE)
    if match is None:
        raise SystemExit(f"no version found in {path}")
    return match.group(1)


manifests = {
    "python": lambda: from_pattern("python/pyproject.toml", r'^version = "([^"]+)"'),
    "typescript": lambda: from_json("typescript/package.json", "version"),
    "java": lambda: from_pattern("java/pom.xml", r"^    <version>([^<]+)</version>"),
    "csharp": lambda: from_pattern(
        "csharp/src/Growwer.Api/Growwer.Api.csproj", r"<Version>([^<]+)</Version>"
    ),
    "ruby": lambda: from_pattern("ruby/lib/growwer/version.rb", r"VERSION = '([^']+)'"),
}

mismatched = []
for name, read in sorted(manifests.items()):
    found = read()
    mark = "ok " if found == expected else "BAD"
    print(f"  {mark} {name}: {found}")
    if found != expected:
        mismatched.append(name)

if mismatched:
    print(f"expected {expected} everywhere; {', '.join(mismatched)} disagree", file=sys.stderr)
    sys.exit(1)

print(f"every manifest is at {expected}")
