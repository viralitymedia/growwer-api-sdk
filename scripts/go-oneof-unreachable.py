"""Removes the unreachable copy of the no-match branch the Go generator writes into oneOf models.

OpenAPI Generator 7.24.0's Go oneOf template emits the "data failed to match schemas in oneOf(X)"
if/else twice in a row inside UnmarshalJSON. Both branches of the first copy return, so the second
can never run, and `go vet` rejects the package with "unreachable code". The template offers no
option for it, so the duplicate is dropped here after every run; behaviour is unchanged.

When a generator upgrade stops emitting the duplicate, nothing matches and this step fails, so the
step is removed then rather than kept as a silent no-op.
"""

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

DUPLICATED = re.compile(
    r"(?P<block>(?P<indent>[ \t]+)if err != nil \{\n"
    r"[ \t]+return fmt\.Errorf\(\"data failed to match schemas in oneOf\((?P<name>\w+)\): %v\", err\)\n"
    r"[ \t]+\} else \{\n"
    r"[ \t]+return fmt\.Errorf\(\"data failed to match schemas in oneOf\((?P=name)\)\"\)\n"
    r"(?P=indent)\}\n)"
    r"(?P=block)"
)

fixed = []
for path in sorted((ROOT / "go").glob("model_*.go")):
    text = path.read_text(encoding="utf-8")
    corrected, count = DUPLICATED.subn(r"\g<block>", text)
    if count:
        path.write_text(corrected, encoding="utf-8")
        fixed.append(path.name)

if not fixed:
    raise SystemExit(
        "no oneOf model repeats its no-match branch any more: remove scripts/go-oneof-unreachable.py "
        "and its call in generate.sh"
    )

print(f"    oneOf unreachable branch removed: {', '.join(fixed)}")
