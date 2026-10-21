"""Applies the repository's licence where the generator insists on the contract's.

The clients here are MIT, because LICENSE at the root of this repository is what governs the code
in it. The contract says `"license": {"name": "Proprietary", "url": "https://growwer.com/legal/terms-of-use/"}`,
which describes the terms of the service the API sells, not the terms of the generated client that
calls it — and openapi.json is fetched from the running API, so it is not ours to correct.

Five generators take a licence option and sdks.json now feeds all five from one value. Two do not
honour it:

  java    takes licenseName but reads the URL from the contract, leaving a pom that names MIT and
          links to a page of commercial terms
  python  takes no licence option at all and writes the contract's name straight into pyproject

Both are fixed here from the same sdks.json value, so the seven clients cannot drift into the
three different licences they carried before.
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

manifest = json.loads((ROOT / "sdks.json").read_text(encoding="utf-8"))
license = manifest["license"]

target = sys.argv[1]


def replace_once(path, old, new):
    text = path.read_text(encoding="utf-8")
    if new in text and old not in text:
        return False
    if text.count(old) != 1:
        raise SystemExit(f"expected exactly one {old!r} in {path}")
    path.write_text(text.replace(old, new), encoding="utf-8")
    return True


if target == "java":
    pom = ROOT / "java" / "pom.xml"
    contract = json.loads((ROOT / "openapi.json").read_text(encoding="utf-8"))
    contract_url = contract["info"]["license"]["url"]
    replace_once(
        pom,
        f"            <url>{contract_url}</url>",
        f"            <url>{license['url']}</url>",
    )
    print(f"  pom.xml: licence url -> {license['url']}")

elif target == "python":
    pyproject = ROOT / "python" / "pyproject.toml"
    contract = json.loads((ROOT / "openapi.json").read_text(encoding="utf-8"))
    contract_name = contract["info"]["license"]["name"]
    replace_once(
        pyproject,
        f'license = {{ text = "{contract_name}" }}',
        f'license = {{ text = "{license["name"]}" }}',
    )
    print(f"  pyproject.toml: licence -> {license['name']}")

else:
    raise SystemExit(f"no licence fix is defined for {target}")
