"""Lets the Ruby client read a oneOf member that carries a field this client does not know.

OpenAPI Generator 7.24.0's Ruby oneOf module (partial_oneof_module.mustache) refuses a member
whenever the data holds a key outside that member's attributes:

    raise if const.respond_to?(:acceptable_attributes) && !(data.keys - const.acceptable_attributes).empty?

So once the API adds a field to an order briefing, every member is refused, `build` returns nil and
Order raises "briefing cannot be nil": the client breaks on a change the API's forward-compatibility
rule allows. The template offers no option for it, so the check is dropped here after every run.
build_from_hash already keeps only the attributes a member declares.

The check was also what told the members apart, and `build` returns the first member that builds.
Without it a member is refused only when a required, non-nullable attribute is missing, so this step
first proves from the contract that every member of every oneOf requires such an attribute the other
members do not declare, and fails the run if one does not. When a generator upgrade stops emitting
the check, nothing is left to patch and this step fails, so it is removed then rather than kept as
a silent no-op.
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODELS = ROOT / "ruby" / "lib" / "growwer" / "models"

CHECK = (
    "              # raise if data contains keys that are not known to the model\n"
    "              raise if const.respond_to?(:acceptable_attributes) && "
    "!(data.keys - const.acceptable_attributes).empty?\n"
)

schemas = json.loads((ROOT / "openapi.json").read_text(encoding="utf-8"))["components"]["schemas"]


def one_ofs(node):
    """Yields the member schema names of every oneOf under `node`."""
    if isinstance(node, dict):
        if "oneOf" in node:
            yield [member["$ref"].rsplit("/", 1)[-1] for member in node["oneOf"]]
        for value in node.values():
            yield from one_ofs(value)
    elif isinstance(node, list):
        for value in node:
            yield from one_ofs(value)


for members in one_ofs(schemas):
    for member in members:
        schema = schemas[member]
        properties = schema.get("properties", {})
        distinguishing = {
            name
            for name in schema.get("required", [])
            if not properties.get(name, {}).get("nullable")
            and all(name not in schemas[other].get("properties", {}) for other in members if other != member)
        }
        if not distinguishing:
            raise SystemExit(
                f"oneOf({', '.join(members)}): {member} requires no non-nullable property the other "
                "members lack, so the Ruby client cannot tell it apart without the unknown-key check"
            )

patched = []
for path in sorted(MODELS.glob("*.rb")):
    text = path.read_text(encoding="utf-8")
    if CHECK in text:
        path.write_text(text.replace(CHECK, ""), encoding="utf-8")
        patched.append(path.stem)

if not patched:
    raise SystemExit(
        "no Ruby oneOf module rejects unknown keys any more: remove scripts/ruby-oneof-unknown-keys.py "
        "and its call in generate.sh"
    )

print(f"    oneOf unknown keys accepted: {', '.join(patched)}")
