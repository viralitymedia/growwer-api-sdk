"""Makes the C# client accept null for the required enum properties the contract marks nullable.

OpenAPI Generator 7.24.0's csharp model template (httpclient library) declares an enum property
nullable only when it is optional: `{{^required}}?{{/required}}`, ignoring `nullable: true`. A
required, nullable enum such as Order.pendingAction becomes a plain `PendingActionEnum`, and
Newtonsoft.Json throws "Cannot convert null value" on every response that carries the null the
contract allows. The template offers no option for it, so after every run this step adds the `?`
to the property and its constructor parameter in each model that holds such a property.

The models come from the contract: a component schema's own properties land in its class and in
every schema that extends it through allOf; an inline object lands in a class named after its
path (SavedFilter.notifications -> SavedFilterNotifications). A model that cannot be found fails
the run rather than leaving one unpatched. When a generator upgrade declares these properties
nullable itself, nothing is left to patch and this step fails, so it is removed then rather than
kept as a silent no-op.
"""

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODELS = ROOT / "csharp" / "src" / "Growwer.Api" / "Model"

contract = json.loads((ROOT / "openapi.json").read_text(encoding="utf-8"))
schemas = contract["components"]["schemas"]


def extensions(name):
    """The schema itself and every component schema that extends it through allOf, transitively."""
    found = {name}
    grown = True
    while grown:
        grown = False
        for other, schema in schemas.items():
            refs = {part.get("$ref", "").rsplit("/", 1)[-1] for part in schema.get("allOf", [])}
            if other not in found and refs & found:
                found.add(other)
                grown = True
    return found


def nullable_required_enums(schema, owner, path, item_suffix="Inner"):
    """Yields (class name, property) for each required, nullable enum property under `schema`."""
    if not isinstance(schema, dict):
        return
    required = set(schema.get("required", []))
    for prop, definition in schema.get("properties", {}).items():
        if not isinstance(definition, dict):
            continue
        if definition.get("nullable") and "enum" in definition and prop in required:
            classes = extensions(owner) if not path else {owner + path}
            for name in classes:
                yield name, prop
        inner = path + prop[0].upper() + prop[1:]
        yield from nullable_required_enums(definition, owner, inner, item_suffix)
        yield from nullable_required_enums(definition.get("items"), owner, inner + item_suffix, item_suffix)
    for part in schema.get("allOf", []):
        if path or "properties" not in part:
            yield from nullable_required_enums(part, owner, path, item_suffix)
            continue
        # An inline object in a component's own allOf part is named with "AllOf" after the
        # component, and the items of an array under it take no "Inner": ProjectCatalogueMedia's
        # project.aiKeywords[] is ProjectCatalogueMediaAllOfProjectAiKeywords.
        own_required = set(part.get("required", []))
        for prop, definition in part["properties"].items():
            if not isinstance(definition, dict):
                continue
            if definition.get("nullable") and "enum" in definition and prop in own_required:
                for name in extensions(owner):
                    yield name, prop
            inner = "AllOf" + prop[0].upper() + prop[1:]
            yield from nullable_required_enums(definition, owner, inner, "")
            yield from nullable_required_enums(definition.get("items"), owner, inner, "")


patched = []
for owner, schema in schemas.items():
    for name, prop in sorted(set(nullable_required_enums(schema, owner, ""))):
        model = MODELS / f"{name}.cs"
        if not model.exists():
            raise SystemExit(f"no C# model {model.name} for the nullable enum {name}.{prop}")
        text = model.read_text(encoding="utf-8")
        member = r"\[DataMember\(Name = \"" + re.escape(prop) + r"\", IsRequired = true[^\]]*\)\]\n(?:[ \t]*\[Obsolete\]\n)?[ \t]*"
        declaration = re.compile(r"(" + member + r"public (?P<type>\w+Enum)) (?P<property>\w+) \{ get; set; \}")
        match = declaration.search(text)
        if match is None:
            if re.search(member + r"public \w+Enum\? \w+ \{ get; set; \}", text):
                continue
            raise SystemExit(f"{model.name}: no enum property declaration for {prop} to make nullable")
        text = declaration.sub(r"\1? \g<property> { get; set; }", text, count=1)
        text, count = re.subn(rf"\b{match['type']} {re.escape(prop)} = default\b", f"{match['type']}? {prop} = default", text)
        if count != 1:
            raise SystemExit(f"{model.name}: expected one constructor parameter {prop}, found {count}")
        model.write_text(text, encoding="utf-8")
        patched.append(f"{name}.{match['property']}")

if not patched:
    raise SystemExit(
        "no required, nullable C# enum property is left non-nullable: remove "
        "scripts/csharp-nullable-enums.py and its call in generate.sh"
    )

print(f"    nullable enums: {', '.join(patched)}")
