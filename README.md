# Growwer API SDKs

[![CI](https://github.com/viralitymedia/growwer-api-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/viralitymedia/growwer-api-sdk/actions/workflows/ci.yml)
[![Release](https://github.com/viralitymedia/growwer-api-sdk/actions/workflows/release.yml/badge.svg)](https://github.com/viralitymedia/growwer-api-sdk/actions/workflows/release.yml)

Official clients for the [Growwer](https://growwer.com) customer API — 66 operations over your
account, projects, orders, the media catalogue, your seller medias and orders, wallets and the
managed service.

Every client here is **generated from the OpenAPI contract the API itself publishes**, so they say
what the running service does rather than what a handwritten wrapper remembers about it. One
contract, one generator run, one version: a change to the API reaches all seven languages together.

| Language | Package | Version | Directory |
|---|---|---|---|
| Python 3.9+ | `growwer` | [![PyPI](https://img.shields.io/pypi/v/growwer?label=pypi&color=informational)](https://pypi.org/project/growwer/) | [`python/`](python/) |
| TypeScript (Node 18+, browsers) | `@growwer/api` | [![npm](https://img.shields.io/npm/v/%40growwer%2Fapi?label=npm&color=informational)](https://www.npmjs.com/package/@growwer/api) | [`typescript/`](typescript/) |
| PHP 8.1+ | `growwer/growwer-api-sdk` | [![Packagist](https://img.shields.io/packagist/v/growwer/growwer-api-sdk?label=packagist&color=informational)](https://packagist.org/packages/growwer/growwer-api-sdk) | [`php/`](php/) |
| Go 1.21+ | `github.com/viralitymedia/growwer-api-sdk/go` | [![Go module](https://img.shields.io/github/v/tag/viralitymedia/growwer-api-sdk?filter=go%2F*&label=go&color=informational)](https://pkg.go.dev/github.com/viralitymedia/growwer-api-sdk/go) | [`go/`](go/) |
| Java 11+ | `com.growwer:growwer-api` | [![Maven Central](https://img.shields.io/maven-central/v/com.growwer/growwer-api?label=maven%20central&color=informational)](https://central.sonatype.com/artifact/com.growwer/growwer-api) | [`java/`](java/) |
| .NET 8 | `Growwer.Api` | [![NuGet](https://img.shields.io/nuget/v/Growwer.Api?label=nuget&color=informational)](https://www.nuget.org/packages/Growwer.Api/) | [`csharp/`](csharp/) |
| Ruby 3.0+ | `growwer` | [![RubyGems](https://img.shields.io/gem/v/growwer?label=gem&color=informational)](https://rubygems.org/gems/growwer) | [`ruby/`](ruby/) |

Each directory carries the generated reference for its language: one page per resource and one per
model under its own `docs/`.

## Get a key

Create one on your Growwer **profile page**, under API keys. Name it after the integration that
will use it, and pick what it may do:

| Key | What it allows |
|---|---|
| Read only | Every `GET` operation: your account, projects, the catalogue, orders and wallets. |
| Read and write | Also every write: creating and changing projects, placing and acting on orders — and spending your balance. |

**The key is shown once, when you create it, and never again**: Growwer stores only a fingerprint
of it. Copy it then and keep it where you keep any other secret. If you lose it, revoke it and
create another; a revoked key stops working at once.

Send it as a bearer token on every request: `Authorization: Bearer <key>`.

## First call

`getMe` returns the account the key belongs to: its wallet balances, its seller status and whether
the catalogue is open to it. It is the quickest way to confirm a key works.

Every client already points at `https://tool.growwer.com`. The examples show where to change that,
for instance to call another host.

<details open>
<summary><strong>Python</strong></summary>

```python
import os

from growwer import ApiClient, Configuration
from growwer.api import AccountApi, OrdersApi

config = Configuration(
    host="https://tool.growwer.com",  # optional: this is the default
    access_token=os.environ["GROWWER_API_KEY"],
)

with ApiClient(config) as client:
    me = AccountApi(client).get_me()
    print(me.email, me.buyer.balance.available.amount, me.buyer.balance.available.currency)

    page = OrdersApi(client).list_orders(limit=100)
    print(f"{len(page.items)} of {page.total} orders")
```
</details>

<details>
<summary><strong>TypeScript</strong></summary>

```ts
import { Configuration, AccountApi, OrdersApi } from "@growwer/api"

const config = new Configuration({
  basePath: "https://tool.growwer.com", // optional: this is the default
  accessToken: process.env.GROWWER_API_KEY,
})

const me = await new AccountApi(config).getMe()
console.log(me.email, me.buyer.balance.available.amount)

const page = await new OrdersApi(config).listOrders({ limit: 100 })
console.log(`${page.items.length} of ${page.total} orders`)
```
</details>

<details>
<summary><strong>Go</strong></summary>

```go
import (
	"context"
	"os"

	growwer "github.com/viralitymedia/growwer-api-sdk/go"
)

config := growwer.NewConfiguration()
// Optional: this is the default.
config.Servers = growwer.ServerConfigurations{{URL: "https://tool.growwer.com"}}
client := growwer.NewAPIClient(config)

ctx := context.WithValue(context.Background(), growwer.ContextAccessToken, os.Getenv("GROWWER_API_KEY"))
me, _, err := client.AccountAPI.GetMe(ctx).Execute()
```
</details>

<details>
<summary><strong>PHP</strong></summary>

```php
use Growwer\Api\Api\AccountApi;
use Growwer\Api\Configuration;

$config = Configuration::getDefaultConfiguration()
    ->setHost('https://tool.growwer.com') // optional: this is the default
    ->setAccessToken(getenv('GROWWER_API_KEY'));

$me = (new AccountApi(new GuzzleHttp\Client(), $config))->getMe();
```
</details>

<details>
<summary><strong>Ruby</strong></summary>

```ruby
require "growwer"

Growwer.configure do |config|
  config.host = "tool.growwer.com" # optional: this is the default
  config.access_token = ENV.fetch("GROWWER_API_KEY")
end

me = Growwer::AccountApi.new.get_me
```
</details>

<details>
<summary><strong>Java</strong></summary>

```java
import com.growwer.api.ApiClient;
import com.growwer.api.api.AccountApi;

ApiClient client = new ApiClient();
client.setBasePath("https://tool.growwer.com"); // optional: this is the default
client.setBearerToken(System.getenv("GROWWER_API_KEY"));

var me = new AccountApi(client).getMe();
```
</details>

<details>
<summary><strong>C#</strong></summary>

```csharp
using Growwer.Api.Api;
using Growwer.Api.Client;

var config = new Configuration
{
    BasePath = "https://tool.growwer.com", // optional: this is the default
    AccessToken = Environment.GetEnvironmentVariable("GROWWER_API_KEY"),
};

var me = new AccountApi(config).GetMe();
```
</details>

## Conventions

These hold in every language. The per-language docs cover the signatures; this is what the
signatures cannot say.

### Errors and request ids

Every response carries an `X-Request-Id` header, and every refusal answers the same envelope with
that id in `requestId`. Quote it when you report a problem and it identifies your exact request.

```json
{
  "code": "insufficient_balance",
  "message": "The available balance of your wallet does not cover the price of this order. Nothing was charged. Add funds to your wallet and retry.",
  "requestId": "4f1c2a9e8b7d6c5e",
  "details": {
    "required": { "amount": 9000, "currency": "EUR" },
    "available": { "amount": 2500, "currency": "EUR" },
    "missing": { "amount": 6500, "currency": "EUR" }
  }
}
```

`code` is stable and machine-readable; branch on it. `message` is for people and may change.
`details` appears on some errors only — the invalid fields of a `422 validation_failed`, the
shortfall of a `409 insufficient_balance` — as each operation's responses describe.

Header names are case-insensitive, so look them up that way. This matters in **C#**: .NET rewrites
the header names it knows, so `X-Request-Id` arrives as `X-Request-ID`, and the client's
`Multimap` of response headers compares names exactly:

```csharp
catch (ApiException e)
{
    var requestId = e.Headers
        .Where(h => string.Equals(h.Key, "X-Request-Id", StringComparison.OrdinalIgnoreCase))
        .SelectMany(h => h.Value)
        .FirstOrDefault();
}
```

PHP's `ApiException::getResponseHeaders()` is a plain array keyed in the case the server sent, which
over HTTP/2 is lower case; compare names case-insensitively there too.

### Rate limits

600 requests per user, across all of that user's keys, and 300 per key, in fixed windows of 60
seconds. The per-user ceiling is the real one: issuing more keys divides the same budget rather
than adding to it.

Every response reports the tighter of the two windows in `X-RateLimit-Limit`,
`X-RateLimit-Remaining` and `X-RateLimit-Reset` (seconds until it refills). A request beyond either
answers `429 rate_limit_exceeded` with a `Retry-After` header in seconds. Honour it:

```python
import time

from growwer.exceptions import ApiException


def with_backoff(call, attempts=3):
    for attempt in range(attempts):
        try:
            return call()
        except ApiException as error:
            if error.status != 429 or attempt == attempts - 1:
                raise
            time.sleep(int(error.headers.get("Retry-After", "1")))
```

Repeated failed authentications from one address are refused with
`429 too_many_failed_authentications` until the window refills. When the rate limiter itself cannot
be reached, the API refuses the call with `503 rate_limit_unavailable` rather than serving it
unmetered; retry later.

### Writes are idempotent

**Every write requires an `Idempotency-Key` header**: 1 to 255 printable ASCII characters. A UUID
is the obvious choice. Use a new key for each operation and reuse it only to retry that same
operation. Keys belong to your account, not to one API key.

```python
import uuid

from growwer.api import ProjectsApi
from growwer.models import CreateProjectRequest

ProjectsApi(client).create_project(
    idempotency_key=str(uuid.uuid4()),
    create_project_request=CreateProjectRequest(
        root_url="https://www.example.com",
        website_type="ecommerce",
        topics=[3],
        language="es",
        promoted_products=["running shoes", "trail shoes", "socks", "insoles", "gaiters"],
    ),
)
```

Generate the key **outside** your retry loop. A fresh key per attempt is the same as having no
idempotency at all.

- **A successful write is stored for 30 days.** A retry with the same key and the same request
  replays its response with `Idempotent-Replayed: true` and does nothing again.
- **A refused write (4xx) has no effect and releases its key.** Fix the cause and retry with the
  same key: the write runs.
- **A failed write (5xx) may have taken effect**, so it is never run again under its key: a retry
  answers `409 idempotency_outcome_unknown`. Check whether it took effect before retrying with a new
  key.
- A retry while the first request is still running answers `409 idempotency_request_in_progress`.
  A request still running after 5 minutes is treated as failed: a retry answers
  `409 idempotency_outcome_unknown`.
- The same key with a different request — method, path, query or body — answers
  `409 idempotency_key_reused` rather than the wrong operation. A write without the header answers
  `400 idempotency_key_required`.

### Placing the same order twice

Independently of the idempotency key, placing the same order — same project, media, type and
price — again within **5 seconds** of one still in progress is refused with `409 duplicate_order`,
and nothing is charged. `details.orderId` is the earlier order, or null when that order has
finished or was deleted since.

Estimate an order first (`estimateOrder`) and send the price it answers as `expectedPrice`: the
order is placed only at that price.

### Paging

Listings take `limit` (default 20, maximum 100) and `offset`, and answer `{items, total}`. A limit
above the maximum is **refused with `422 validation_failed`, never quietly clamped**, so the page
you asked for is the page you get. `total` counts everything the filter matches, not the size of
the page.

### Following changes

Orders are polled, not pushed. Call `GET /orders` (or `GET /seller/orders` for the orders on your
medias) with `sort=updatedAt` and `updatedSince` set to the `updatedAt` of the last order you saw:
an order moves to the end of that list each time it changes state. `updatedAt` changes on state
changes only.

### Money and dates

Money is an object of integer **cents** and a currency code — `{"amount": 9000, "currency": "EUR"}`
is 90.00 EUR — never a float. Dates and date-times are ISO-8601. A date-time sent in a query string
carries its offset, and its `+` must be sent as `%2B`.

### The catalogue

The catalogue operations (searching a project's medias, flash offers, media details) are open to
accounts with recent completed orders, as buyer or as seller. Until then they answer
`403 catalogue_requires_recent_order`; `GET /me` reports `catalogue.eligible`. A media you have
ordered is always readable with `GET /medias/{id}`.

Each account may see a limited number of distinct medias per UTC day through the catalogue. A
response that would go beyond it answers `429 catalogue_daily_cap_reached`: `details.remaining`
says how many new medias still fit today, `Retry-After` is the time to the next UTC midnight, and
medias already seen today stay readable.

The managed service requests are capped per UTC day too, at 5 of each kind:
`429 managed_service_request_limit_reached`, with `Retry-After` the time to the next UTC midnight.

### Forward compatibility

The API adds fields to its responses without a new version. **Every client here ignores a response
field it does not know**, so a client generated today keeps reading tomorrow's responses. The
offline fixture tests under [`tests/`](tests/) prove it for each language on every change.

**Known limitation: enum values.** A new value in an existing enum field is not tolerated
everywhere. The Python, PHP, Java, C# and Ruby clients refuse a value they were not generated with,
and the whole response fails to deserialise. Go and TypeScript hold enum fields as plain strings
and pass a new value through. The generator's `enumUnknownDefaultCase` option would map unknown
values to a sentinel instead; it is not enabled. Upgrade to the release that follows an enum change
before the API starts sending the new value to you.

## Regenerating

```bash
./generate.sh                # every SDK, from the committed openapi.json
./generate.sh python go      # only these
./generate.sh --sync         # fetch the live contract first, then regenerate everything
```

Requires Docker and Python 3. Everything inside each language directory is generated and must not
be edited by hand — the next run discards it. Adding a language is one entry in
[`sdks.json`](sdks.json).

`--sync` reads the contract from `contractUrl` in [`sdks.json`](sdks.json), or from
`GROWWER_CONTRACT_URL` when it is set. The URL goes to `curl`, so a contract dumped to disk is
synced with a file URL:

```bash
GROWWER_CONTRACT_URL=file:///absolute/path/openapi.json ./generate.sh --sync
```

The fetch is opt-in because a regeneration that silently pulls a new contract turns a mechanical
rerun into a content change nobody reviewed, and the diff runs to six figures of lines across seven
languages — the one place a surprise must not hide. A fetched contract with fewer than 60
operations is refused rather than written: it is far more likely to be a misrouted response than a
real change.

`--sync` writes the contract in the layout of the committed `openapi.json` — two-space indent, UTF-8
left unescaped, a trailing newline — so the diff it leaves is only what the contract changed. It is
written with Python's `json` module, which would differ from `jq` in two cases the contract does not
contain: U+007F (DEL) is written raw where `jq` escapes it, and a number literal is rewritten in
Python's form (`1e3` becomes `1000.0`, `1.50` becomes `1.5`).

The generator never deletes a file it no longer emits, so after each language is generated the
script deletes every file the previous `.openapi-generator/FILES` listed and the new one does not.
Three kinds of listed path are kept, because their absence from the new list does not mean the
contract dropped them:

- **Test stubs**, except Go's. The generator writes a stub only when it is missing and lists it only
  on the run that writes it, so a stub added in one run is gone from the next run's list. Nothing
  under the directory named by the SDK's `testStubDir` in [`sdks.json`](sdks.json) is deleted
  (`python/test/`, `php/test/`, `java/src/test/`, `csharp/src/Growwer.Api.Test/`, `ruby/spec/`), so
  when the contract drops a schema or operation its stub has to be deleted by hand. Go is generated
  into an empty directory, so its stubs are written and listed on every run and are removed with
  the rest; TypeScript has none. For the same reason, after a contract change that adds a schema or
  operation, run the script twice before committing: the first run lists the new stubs in
  `.openapi-generator/FILES` and the second drops them again, which is the list CI expects.
- **`.openapi-generator-ignore`**, which the generator likewise writes only when it is missing.
- **Any path the target's `.openapi-generator-ignore` names**: the generator stopped writing it
  because it is now maintained by hand.

These corrections are applied by the generator script rather than by hand, because a hand edit
would be discarded on the next run:

- **Go** has no package registry, so the import path is the repository URL plus the directory. The
  generator derives the module path from the Go package name, and `go` is a keyword, so it cannot
  produce `.../growwer-api-sdk/go` on its own.
- **Go**'s oneOf template writes its no-match branch twice in a row, and `go vet` rejects the second
  copy as unreachable code. The copy is dropped by
  [`scripts/go-oneof-unreachable.py`](scripts/go-oneof-unreachable.py).
- **C#**'s model template makes an enum property nullable only when it is optional, ignoring
  `nullable: true`, so the null the contract allows in a required enum such as `Order.pendingAction`
  would fail deserialisation. The `?` is added by
  [`scripts/csharp-nullable-enums.py`](scripts/csharp-nullable-enums.py).
- **Package metadata.** Left alone, the Python, TypeScript and PHP manifests name OpenAPI Generator
  as their author and carry its description and keywords. They are rewritten from
  [`sdks.json`](sdks.json) by [`scripts/package-metadata.py`](scripts/package-metadata.py), which
  also sets the PHP package name.

The two template fixes fail the run when they find nothing left to correct, so a generator upgrade
that makes one obsolete removes it rather than leaving a silent no-op.

## Contract

- [`openapi.json`](openapi.json) — the contract every client here is generated from
- [Live contract](https://tool.growwer.com/api/v1/doc/json) and
  [browsable reference](https://tool.growwer.com/api/v1/doc)

## Releasing

A `vX.Y.Z` tag runs [`release.yml`](.github/workflows/release.yml). It checks that the tag equals
`packageVersion` in [`sdks.json`](sdks.json) and that regenerating leaves no diff, then publishes to
npm, PyPI, Maven Central, NuGet and RubyGems, and pushes the `go/vX.Y.Z` tag the Go module proxy
resolves. Packagist picks the tag up through its webhook.

**No release happens before the committed contract matches production.** The API it describes
reaches production with the monolith's customer API slices 5, 6 and 7a. Once those are deployed,
`./generate.sh --sync` against production must leave no diff; only then is the first tag pushed.

An owner sets the registries up once, before the first tag:

- [ ] **npm**: the `growwer` organisation, and an automation token with publish rights on
      `@growwer/api` stored as the repository secret `NPM_TOKEN`.
- [ ] **PyPI**: a trusted publisher for the `growwer` project naming this repository, the workflow
      `release.yml` and the environment `release`.
- [ ] **NuGet**: a trusted publishing policy for `Growwer.Api` naming this repository, `release.yml`
      and the environment `release`, and the nuget.org account it was created under stored as the
      repository variable `NUGET_USER` (a variable, not a secret).
- [ ] **RubyGems**: a push key for the `growwer` gem stored as the repository secret
      `RUBYGEMS_API_KEY`.
- [ ] **Maven Central**: the Sonatype Central namespace `com.growwer`, verified with a DNS TXT record
      on growwer.com, and the repository secrets `MAVEN_CENTRAL_USERNAME`, `MAVEN_CENTRAL_PASSWORD`,
      `MAVEN_GPG_PRIVATE_KEY` and `MAVEN_GPG_PASSPHRASE`.
- [ ] **Packagist**: submit this repository as `growwer/growwer-api-sdk`, and add Packagist's GitHub
      webhook so new tags are picked up.
- [ ] **Go**: nothing. The module proxy resolves the `go/vX.Y.Z` tag the workflow pushes.
- [ ] The GitHub environment `release`, which every publishing job runs in.

## License

MIT. See [LICENSE](LICENSE).
