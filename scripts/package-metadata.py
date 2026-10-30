"""Replaces the generator's own name in the manifests whose templates offer no option for it, and
raises the Python dependency floors past the releases with open advisories.

Java, C#, Ruby and PHP take their author, description and homepage as options, and generate.sh
feeds them from sdks.json. Three manifests keep template text that no option reaches:

  typescript  package.json hardcodes `"author": "OpenAPI-Generator"` and describes the package as
              "OpenAPI client for @growwer/api"; it also declares no supported Node range, so the
              `engines` floor is added here
  python      pyproject.toml and setup.py hardcode the keywords "OpenAPI" and "OpenAPI-Generator";
              the author comes from the contract's info.contact and needs nothing here
  php         php/composer.json hardcodes the keywords "openapitools", "openapi-generator" and
              "openapi", and names the package gitUserId/gitRepoId whatever composerPackageName
              says, which would publish it as viralitymedia/growwer-api-sdk; the published root
              manifest is derived from this one by php-root-manifest.py

A registry shows these fields on the package page, so left alone every package would present itself
as the work of OpenAPI Generator. They are rewritten from sdks.json on each run, since a hand edit is
discarded by the next regeneration.

The Python manifests also get their dependency floors raised. The generator writes the floors of its
own templates (urllib3 >= 2.6.3, pytest >= 8.4.2, Python >= 3.9) and has no option to change them,
while Dependabot cannot fix a vulnerable dependency in a project with neither a lockfile nor a pinned
version: it can only report it. So the floors that exclude the known vulnerable releases are written
here, into pyproject.toml, setup.py, requirements.txt and test-requirements.txt, which have to agree
because pip, Poetry and tox each read a different one. filelock reaches the dev environment only
through tox, so the generator never lists it and its floor is added as a line of its own.
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

manifest = json.loads((ROOT / "sdks.json").read_text(encoding="utf-8"))
author = manifest["author"]
description = manifest["description"]

KEYWORDS = ["growwer", "api", "sdk", "seo", "link-building"]
COMPOSER_NAME = "growwer/growwer-api-sdk"

# The lowest releases free of the advisories open against the Python SDK, all of which need 3.10.
PYTHON_FLOOR = "3.10"
URLLIB3_FLOOR = "2.8.0"
PYTEST_FLOOR = "9.0.3"
FILELOCK_FLOOR = "3.20.3"

# The oldest Node release line still supported upstream; CI tests the package on it and on the
# current LTS.
NODE_FLOOR = "22"

target = sys.argv[1]


def replace_line(path, pattern, new):
    # The generated line embeds the contract's title, so it is matched by shape, once.
    text = path.read_text(encoding="utf-8")
    matches = re.findall(pattern, text, re.MULTILINE)
    if len(matches) != 1:
        raise SystemExit(f"expected exactly one line matching {pattern!r} in {path}")
    path.write_text(re.sub(pattern, lambda _: new, text, flags=re.MULTILINE), encoding="utf-8")


def version(text):
    return tuple(int(part) for part in text.split("."))


def raise_floor(path, pattern, floor):
    # Only the version inside the generated line is rewritten, so an upper bound or the quoting stays
    # the generator's. A floor a later generator release writes higher than this one is kept, not
    # lowered, and compared as numbers because "3.9" sorts after "3.10" as text.
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    if len(matches) != 1:
        raise SystemExit(f"expected exactly one line matching {pattern!r} in {path}")
    match = matches[0]
    if version(match["floor"]) >= version(floor):
        return
    path.write_text(text[:match.start("floor")] + floor + text[match.end("floor"):], encoding="utf-8")


def add_floor(path, pattern, floor, after, line):
    # For a dependency the generator never lists: the line goes in after the one matching `after` on
    # the first run, and a later run over the same file only raises its floor.
    text = path.read_text(encoding="utf-8")
    if re.search(pattern, text, re.MULTILINE):
        raise_floor(path, pattern, floor)
        return
    anchors = list(re.finditer(after, text, re.MULTILINE))
    if len(anchors) != 1:
        raise SystemExit(f"expected exactly one line matching {after!r} in {path}")
    end = anchors[0].end()
    path.write_text(text[:end] + "\n" + line + text[end:], encoding="utf-8")


def rewrite_json(path, indent, update):
    # Written back in the generator's own layout for that file, so the only lines that differ from
    # the generated file are the ones corrected.
    data = json.loads(path.read_text(encoding="utf-8"))
    update(data)
    path.write_text(json.dumps(data, indent=indent, ensure_ascii=False) + "\n", encoding="utf-8")


if target == "typescript":
    def update(package):
        package["description"] = description
        package["author"] = f"{author['name']} <{author['email']}> ({author['url']})"
        package["keywords"] = KEYWORDS
        package["engines"] = {"node": f">={NODE_FLOOR}"}

    rewrite_json(ROOT / "typescript" / "package.json", 2, update)
    print(f"  package.json: author, description, keywords, engines node >={NODE_FLOOR}")

elif target == "python":
    keywords = json.dumps(KEYWORDS)
    replace_line(ROOT / "python" / "pyproject.toml", r"^keywords = \[.*\]$", f"keywords = {keywords}")
    replace_line(ROOT / "python" / "setup.py", r"^    keywords=\[.*\],$", f"    keywords={keywords},")
    print("  pyproject.toml, setup.py: keywords")

    python = ROOT / "python"
    floor = r"(?P<floor>\d+(?:\.\d+)*)"
    raise_floor(python / "pyproject.toml", rf'^requires-python = ">={floor}"$', PYTHON_FLOOR)
    raise_floor(python / "pyproject.toml", rf'^  "urllib3 \(>={floor},.*\)",$', URLLIB3_FLOOR)
    raise_floor(python / "pyproject.toml", rf'^pytest = ">= {floor}"$', PYTEST_FLOOR)
    add_floor(
        python / "pyproject.toml",
        rf'^filelock = ">= {floor}"$',
        FILELOCK_FLOOR,
        r'^tox = ".*"$',
        f'filelock = ">= {FILELOCK_FLOOR}"',
    )
    raise_floor(python / "setup.py", rf'^PYTHON_REQUIRES = ">= {floor}"$', PYTHON_FLOOR)
    raise_floor(python / "setup.py", rf'^    "urllib3 >= {floor},.*",$', URLLIB3_FLOOR)
    raise_floor(python / "requirements.txt", rf"^urllib3 >= {floor},.*$", URLLIB3_FLOOR)
    raise_floor(python / "test-requirements.txt", rf"^pytest >= {floor}$", PYTEST_FLOOR)
    add_floor(
        python / "test-requirements.txt",
        rf"^filelock >= {floor}$",
        FILELOCK_FLOOR,
        r"^tox >= .*$",
        f"filelock >= {FILELOCK_FLOOR}",
    )
    print(
        f"  pyproject.toml, setup.py, requirements.txt, test-requirements.txt: Python >= {PYTHON_FLOOR}, "
        f"urllib3 >= {URLLIB3_FLOOR}, pytest >= {PYTEST_FLOOR}, filelock >= {FILELOCK_FLOOR}"
    )

elif target == "php":
    def update(composer):
        composer["name"] = COMPOSER_NAME
        composer["description"] = description
        composer["keywords"] = KEYWORDS

    rewrite_json(ROOT / "php" / "composer.json", 4, update)
    # The generated README's install snippet requires the package under the same wrong name.
    replace_line(
        ROOT / "php" / "README.md",
        r'^    "viralitymedia/growwer-api-sdk": "\*@dev"$',
        f'    "{COMPOSER_NAME}": "*@dev"',
    )
    print(f"  php/composer.json, php/README.md: name {COMPOSER_NAME}; description, keywords")

else:
    raise SystemExit(f"no package metadata fix is defined for {target}")
