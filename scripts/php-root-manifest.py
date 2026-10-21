"""Derives the repository-root composer.json from the generated php/composer.json.

Packagist reads composer.json from the root of a repository and has no notion of a package that
lives in a subdirectory. Go has the same shape of problem and solves it with directory-prefixed
tags; Composer has no equivalent, so for PHP the published manifest has to BE the root one.

It is derived rather than written by hand because two manifests maintained separately are two
manifests that disagree. `php/composer.json` stays where the generator puts it — it is what makes
the subdirectory usable on its own — and this rewrites its autoload roots and replaces the
generator's placeholder metadata, which the PHP generator does not take from the contract the way
the Python and Java ones do.

Also writes .gitattributes. Composer installs from the archive GitHub builds for a tag, and without
`export-ignore` a PHP project would download all seven language clients — about 31 MB — to use one.
`git clone` is unaffected; only the generated archive is trimmed.
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

contract = json.loads((ROOT / "openapi.json").read_text(encoding="utf-8"))
generated = json.loads((ROOT / "php" / "composer.json").read_text(encoding="utf-8"))

info = contract.get("info", {})
contact = info.get("contact", {})

manifest = dict(generated)
manifest["description"] = (
    "Official PHP client for the Growwer API: orders, projects, the media catalogue, seller "
    "medias and wallets."
)
manifest["homepage"] = "https://github.com/viralitymedia/growwer-api-sdk"
manifest["license"] = "MIT"
manifest["authors"] = [
    {
        "name": contact.get("name", "Growwer Support"),
        "email": contact.get("email", "support@growwer.com"),
        "homepage": contact.get("url", "https://growwer.com/contact/"),
    }
]
manifest["support"] = {
    "issues": "https://github.com/viralitymedia/growwer-api-sdk/issues",
    "docs": "https://tool.growwer.com/api/v1/doc",
}
manifest["keywords"] = [
    "growwer",
    "api",
    "sdk",
    "seo",
    "link-building",
    "sponsored-posts",
    "marketplace",
]

# The sources stay where the generator puts them; only the roots move, because the package is now
# rooted one directory up.
manifest["autoload"] = {"psr-4": {"Growwer\\Api\\": "php/lib/"}}
manifest["autoload-dev"] = {"psr-4": {"Growwer\\Api\\Test\\": "php/test/"}}

(ROOT / "composer.json").write_text(
    json.dumps(manifest, indent=4, ensure_ascii=False) + "\n", encoding="utf-8"
)

# Everything a PHP consumer does not need, kept out of the archive Composer downloads. The PHP
# client, the contract it was generated from, the licence and the README stay in.
EXPORT_IGNORED = [
    ".github",
    ".generator-configs",
    ".gitattributes",
    ".gitignore",
    "csharp",
    "generate.sh",
    "go",
    "java",
    "python",
    "ruby",
    "scripts",
    "sdks.json",
    "tests",
    "typescript",
]

lines = [
    "# Composer installs from the archive GitHub builds for a tag. Without this, a PHP project",
    "# would download all seven language clients to use one of them.",
    "",
    *[f"/{path} export-ignore" for path in EXPORT_IGNORED],
    "",
    "# The PHP client's own development scaffolding is not needed to consume it either.",
    "/php/test export-ignore",
    "/php/.openapi-generator export-ignore",
    "/php/.openapi-generator-ignore export-ignore",
    "/php/git_push.sh export-ignore",
    "/php/phpunit.xml.dist export-ignore",
    "",
]

(ROOT / ".gitattributes").write_text("\n".join(lines), encoding="utf-8")

print(f"  root composer.json: {manifest['name']} ({manifest['license']})")
