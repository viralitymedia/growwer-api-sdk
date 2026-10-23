"""Keeps the C# client from sending null for an optional, nullable request property left unset.

OpenAPI Generator 7.24.0's csharp model template (httpclient library) marks a nullable property
`EmitDefaultValue = true`, so that a null the caller sets reaches the API. It does so for an
optional one too, and an unset property is null as well: every request then carries it as null.
Here a null means something, so a PATCH that only renames a project also sends `country: null`,
which sets it to worldwide, and a seller media update sends `linkAdditionOffer: null`, which stops
link additions. The template's `conditionalSerialization` option tracks what was set, but it never
marks a required constructor argument set, so it would drop every required property instead.

So after every run each such property becomes a backing field with a flag the setter raises, and
Newtonsoft.Json writes it only when `ShouldSerialize<Property>()` returns that flag, the same shape
`conditionalSerialization` generates. The constructor raises the flag only for an argument that is
not null, so `new UpdateProjectRequest(name: "x")` sends the name alone, while `Country = null` set
through the property still sends the null.

The properties come from the contract: each one not in its schema's `required` and nullable, by
itself or through the schema its `$ref` or single `allOf` names, in a schema a JSON request body
uses, the component schemas it references and the inline objects under it. An inline object lands
in a class named after its path (updateSellerMedia_request_linkAdditionOffer ->
UpdateSellerMediaRequestLinkAdditionOffer, array items with `_inner`), unless sdks.json's
inlineSchemaNameMappings pins another name. A model or declaration that cannot be found fails the
run rather than leaving one unpatched, and a run over its own output changes nothing. When a
generator upgrade omits these properties itself (`EmitDefaultValue = false`), nothing is left to
patch and this step fails, so it is removed then rather than kept as a silent no-op.
"""

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODELS = ROOT / "csharp" / "src" / "Growwer.Api" / "Model"

contract = json.loads((ROOT / "openapi.json").read_text(encoding="utf-8"))
schemas = contract.get("components", {}).get("schemas", {})
name_mappings = json.loads((ROOT / "sdks.json").read_text(encoding="utf-8")).get("inlineSchemaNameMappings", {})


def class_name(inline_name):
    """The C# class the generator writes for an inline schema or component named `inline_name`."""
    mapped = name_mappings.get(inline_name, inline_name)
    return "".join(part[:1].upper() + part[1:] for part in mapped.split("_"))


def referenced(definition):
    """The component a property names through `$ref` or a single-member `allOf`, or None."""
    if "$ref" in definition:
        return definition["$ref"].rsplit("/", 1)[-1]
    parts = definition.get("allOf", [])
    if len(parts) == 1 and "$ref" in parts[0]:
        return parts[0]["$ref"].rsplit("/", 1)[-1]
    return None


def nullable(definition):
    target = referenced(definition)
    return bool(definition.get("nullable")) or (target is not None and bool(schemas.get(target, {}).get("nullable")))


def own_optional_nullables(schema):
    """The optional, nullable properties a schema's class declares, its allOf parents' included."""
    required = set(schema.get("required", []))
    for part in schema.get("allOf", []):
        required |= set(part.get("required", []))
    found = []
    for part in [schema, *schema.get("allOf", [])]:
        if "$ref" in part:
            found += own_optional_nullables(schemas[part["$ref"].rsplit("/", 1)[-1]])
            continue
        for prop, definition in part.get("properties", {}).items():
            if isinstance(definition, dict) and prop not in required and nullable(definition):
                found.append(prop)
    return found


def holds_inline_object(schema):
    """Whether one of the schema's properties, or the items of one, is an inline object."""
    for definition in schema.get("properties", {}).values():
        if not isinstance(definition, dict):
            continue
        items = definition.get("items")
        if definition.get("properties") or isinstance(items, dict) and items.get("properties"):
            return True
    return False


def request_optional_nullables():
    """Yields (class name, property) for each optional, nullable property a JSON request can carry."""
    visited = set()

    def walk(schema, inline_name):
        if not isinstance(schema, dict):
            return
        target = referenced(schema)
        if target is not None and "properties" not in schema:
            if target not in visited:
                visited.add(target)
                yield from walk(schemas[target], target)
            return
        for prop in own_optional_nullables(schema):
            yield class_name(inline_name), prop
        for keyword in ("allOf", "oneOf", "anyOf"):
            for part in schema.get(keyword, []):
                if "$ref" in part:
                    yield from walk(part, inline_name)
                elif part.get("properties") if keyword != "allOf" else holds_inline_object(part):
                    # The generator names these after the composition rather than the path, which
                    # no request body needs yet; guessing that name would patch nothing silently.
                    raise SystemExit(f"{inline_name}: an inline object under {keyword} is not supported by this script")
        for prop, definition in schema.get("properties", {}).items():
            if not isinstance(definition, dict):
                continue
            yield from walk(definition, f"{inline_name}_{prop}")
            items = definition.get("items")
            if isinstance(items, dict):
                yield from walk(items, f"{inline_name}_{prop}_inner")

    for path_item in contract.get("paths", {}).values():
        for operation in path_item.values():
            if not isinstance(operation, dict) or "requestBody" not in operation:
                continue
            for media_type, content in operation["requestBody"].get("content", {}).items():
                # Any other body is sent as form fields, not as a model the client serialises.
                if media_type == "application/json" or media_type.endswith("+json"):
                    yield from walk(content.get("schema"), f"{operation['operationId']}_request")


patched = []
already = []
for name, prop in sorted(set(request_optional_nullables())):
    model = MODELS / f"{name}.cs"
    if not model.exists():
        raise SystemExit(
            f"no C# model {model.name} for the optional, nullable {name}.{prop}: "
            "pin the class the generator chose with inlineSchemaNameMappings in sdks.json"
        )
    text = model.read_text(encoding="utf-8")
    member = r"[ \t]*\[DataMember\(Name = \"" + re.escape(prop) + r"\", EmitDefaultValue = true\)\]\n(?:[ \t]*\[[^\n]*\]\n)*"
    declaration = re.compile(
        r"(?P<attributes>" + member + r")(?P<indent>[ \t]*)public (?P<type>[^\n]+?) (?P<property>\w+) \{ get; set; \}\n"
    )
    match = declaration.search(text)
    if match is None:
        if re.search(member + r"[ \t]*public [^\n]+? \w+\n[ \t]*\{\n[ \t]*get \{ return _\w+; \}", text):
            already.append(f"{name}.{prop}")
            continue
        if f'[DataMember(Name = "{prop}", EmitDefaultValue = false)]' in text:
            # The generator leaves this one out when unset by itself now.
            continue
        raise SystemExit(f"{model.name}: no optional, nullable property declaration for {prop} to patch")
    indent, kind, member_name = match["indent"], match["type"], match["property"]
    if f"ShouldSerialize{member_name}(" in text:
        raise SystemExit(f"{model.name}: {member_name} already has a ShouldSerialize{member_name} method")
    replacement = (
        f"{match['attributes']}"
        f"{indent}public {kind} {member_name}\n"
        f"{indent}{{\n"
        f"{indent}    get {{ return _{member_name}; }}\n"
        f"{indent}    set\n"
        f"{indent}    {{\n"
        f"{indent}        _{member_name} = value;\n"
        f"{indent}        _flag{member_name} = true;\n"
        f"{indent}    }}\n"
        f"{indent}}}\n"
        f"{indent}private {kind} _{member_name};\n"
        f"{indent}private bool _flag{member_name};\n"
        f"\n"
        f"{indent}/// <summary>\n"
        f"{indent}/// Returns true once {member_name} has been set, so that a property left unset is left out of\n"
        f"{indent}/// the request rather than sent as null, which the API reads as a value.\n"
        f"{indent}/// </summary>\n"
        f"{indent}/// <returns>true once {member_name} has been set (boolean)</returns>\n"
        f"{indent}public bool ShouldSerialize{member_name}()\n"
        f"{indent}{{\n"
        f"{indent}    return _flag{member_name};\n"
        f"{indent}}}\n"
    )
    text = text[: match.start()] + replacement + text[match.end() :]
    assignment = re.compile(rf"^(?P<indent>[ \t]*)this\.{member_name} = (?P<argument>\w+);$", re.MULTILINE)
    assignments = assignment.findall(text)
    if len(assignments) != 1:
        raise SystemExit(f"{model.name}: expected one constructor assignment to {member_name}, found {len(assignments)}")
    text = assignment.sub(
        lambda found: (
            f"{found['indent']}// a null \"{found['argument']}\" leaves {member_name} unset, so it is not sent\n"
            f"{found['indent']}this._{member_name} = {found['argument']};\n"
            f"{found['indent']}if (this.{member_name} != null)\n"
            f"{found['indent']}{{\n"
            f"{found['indent']}    this._flag{member_name} = true;\n"
            f"{found['indent']}}}"
        ),
        text,
    )
    model.write_text(text, encoding="utf-8")
    patched.append(f"{name}.{member_name}")

if not patched and not already:
    raise SystemExit(
        "no optional, nullable C# request property is left to patch: remove "
        "scripts/csharp-optional-nullables.py and its call in generate.sh"
    )

print(f"    optional nullables: {', '.join(patched) or 'already patched'}")
