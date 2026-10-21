"""Replaces the generator's own name in the manifests whose templates offer no option for it.

Java, C#, Ruby and PHP take their author, description and homepage as options, and generate.sh
feeds them from sdks.json. Three manifests keep template text that no option reaches:

  typescript  package.json hardcodes `"author": "OpenAPI-Generator"` and describes the package as
              "OpenAPI client for @growwer/api"
  python      pyproject.toml and setup.py hardcode the keywords "OpenAPI" and "OpenAPI-Generator";
              the author comes from the contract's info.contact and needs nothing here
  php         php/composer.json hardcodes the keywords "openapitools", "openapi-generator" and
              "openapi", and names the package gitUserId/gitRepoId whatever composerPackageName
              says, which would publish it as viralitymedia/growwer-api-sdk; the published root
              manifest is derived from this one by php-root-manifest.py

A registry shows these fields on the package page, so left alone every package would present itself
as the work of OpenAPI Generator. They are rewritten from sdks.json on each run, since a hand edit is
discarded by the next regeneration.
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

target = sys.argv[1]


def replace_line(path, pattern, new):
    # The generated line embeds the contract's title, so it is matched by shape, once.
    text = path.read_text(encoding="utf-8")
    matches = re.findall(pattern, text, re.MULTILINE)
    if len(matches) != 1:
        raise SystemExit(f"expected exactly one line matching {pattern!r} in {path}")
    path.write_text(re.sub(pattern, lambda _: new, text, flags=re.MULTILINE), encoding="utf-8")


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

    rewrite_json(ROOT / "typescript" / "package.json", 2, update)
    print("  package.json: author, description, keywords")

elif target == "python":
    keywords = json.dumps(KEYWORDS)
    replace_line(ROOT / "python" / "pyproject.toml", r"^keywords = \[.*\]$", f"keywords = {keywords}")
    replace_line(ROOT / "python" / "setup.py", r"^    keywords=\[.*\],$", f"    keywords={keywords},")
    print("  pyproject.toml, setup.py: keywords")

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
