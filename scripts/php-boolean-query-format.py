"""Makes the PHP client send boolean query parameters as `true` and `false` by default.

OpenAPI Generator 7.24.0's php Configuration template starts every configuration with
`BOOLEAN_FORMAT_INT`, so a boolean query filter such as `bestPrice` goes out as `1` or `0`. The API
accepts only `true` and `false` for its boolean filters and answers anything else with a 400, so
every boolean filter sent from PHP was refused. The template has no option for the default, so after
every run this step starts the configuration with `BOOLEAN_FORMAT_STRING` instead. A caller can still
choose either format with `setBooleanFormatForQueryString` on the default configuration, which is the
one the serializer reads.

When a generator upgrade changes that line, nothing matches and this step fails, so it is removed or
updated then rather than kept as a silent no-op.
"""

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIGURATION = ROOT / "php" / "lib" / "Configuration.php"

GENERATED = "    protected $booleanFormatForQueryString = self::BOOLEAN_FORMAT_INT;\n"
CORRECTED = "    protected $booleanFormatForQueryString = self::BOOLEAN_FORMAT_STRING;\n"

text = CONFIGURATION.read_text(encoding="utf-8")
if text.count(GENERATED) != 1:
    raise SystemExit(
        "php/lib/Configuration.php no longer starts the boolean query format at BOOLEAN_FORMAT_INT: "
        "remove or update scripts/php-boolean-query-format.py and its call in generate.sh"
    )

CONFIGURATION.write_text(text.replace(GENERATED, CORRECTED), encoding="utf-8")
print("    boolean query format -> BOOLEAN_FORMAT_STRING")
