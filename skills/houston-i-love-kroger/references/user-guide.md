# Install the companion and ask for grocery help

## Detailed Content

### 1. Keep the complete companion together

This plugin lets an assistant help with Kroger groceries and deals directly in
conversation. The assistant understands your request, uses the shared shopping
microservice, checks returned packages and explains useful choices. The
companion and web app are independent projects sharing that service. You never
need to open, install or use the web app for this companion, including recovery.

1. Get the complete plugin ZIP from the [plugin repository](https://github.com/aipersonalized/houston-i-love-kroger-plugin)
   or its supplied release. Extract the whole `houston-i-love-kroger-plugin` folder.
2. Keep the whole folder together. Its skill is `skills/houston-i-love-kroger/`;
   `SKILL.md`, `config/connection.json`, scripts, playbooks, references, schemas
   and manuals are required. Copying just `SKILL.md` leaves it incomplete.
3. Follow your assistant host's supported local-plugin or Agent Skills import
   method. The portable core has no provider-specific installation directory.
   The optional `.codex-plugin/plugin.json` adapter declares the bundled skill;
   actual host import/discovery remains untested.
4. If your host can read local files but has no importer, ask it to read the
   skill's `SKILL.md`. That is manual use rather than verified automatic discovery.
5. Check that the host can execute Python 3.12+ or use an equivalent permitted
   HTTP client. The plugin does not install a remote connector. Without that
   capability, the assistant must explain the host gap; it cannot perform the
   lookups or replace them with a web-app visit.

No Node.js, supplier key, private database, provider SDK or model account is
required by the portable tools. Your assistant host's own requirements remain
separate. Original project material uses the plugin-root MIT LICENSE; that
license does not grant rights to supplier data or marks.

### 2. Ask naturally after installation

You can immediately ask the assistant for grocery help; you do not need to
supply a service URL, learn command names or request a technical setup workflow.
For example:

- "I need milk, eggs and coffee. Help me find some good deals at my Kroger."
- "Check the price of this package at the store we already chose."
- "Find two packages of whole milk and rice. Ask me before substituting brands."

The assistant infers the requested groceries and whether you want discounts,
low package prices, an exact price check or a quantity estimate. It asks only
for missing facts that affect the answer:

1. If your exact store is not already confirmed, supply a five-digit ZIP through
   your permitted privacy channel. It retrieves up to ten choices within the
   source query's ten-mile radius, shows actual returned names/addresses and
   waits for your exact choice before product searches. It never chooses the
   first store or invents distances. A valid earlier store choice is reused.
2. It searches the shared service for the requested groceries and matches actual
   descriptions, brands, package sizes and variants. It keeps no-match groceries
   visible and asks about meaningful substitution/package ambiguity.
3. It reports a small useful selection with product/package, reported price,
   supported saving and why each choice fits. A good discount and low package
   spending are different judgments. Searches cover bounded returned pages,
   never every product or every store promotion.
4. If you request quantity costs, it matches your intended packages/quantities
   and has the service recheck the selected products and calculate. Each estimate
   accepts 1–10 distinct product/item pairs and whole quantities 1–99. Larger
   lists remain visible; separate batches do not establish one combined snapshot.
5. It explains source check dates, unknowns and unresolved lines beside amounts.
   Current source currency and measure basis are unreported, so numeric totals
   have no currency symbol or verified budget fit. Tax, fees, coupons, eligibility
   checks and checkout changes remain excluded. Missing prices are never free.

A product-choice request does not require quantities or a budget. Supply brands,
package sizes, substitutions or a budget when they matter to you; the assistant
must not invent them. No companion command signs in, changes Cart, clips coupons,
purchases anything, starts collection or saves your shopping list.

### 3. Understand service access and source permissions

The tools load the skill's `config/connection.json` automatically. It selects
`https://aipersonalized.io/api/houston-i-love-kroger/` as the shared-service base.
A configured destination is not proof of a working or qualified live deployment;
the assistant reports only actual successful checks and source-backed results.
The shopper does not supply an app URL or run a local app.

An operator deliberately using another compatible service can override the
bundled connection with `HOUSTON_SERVICE_URL` or `--base-url`. Precedence is
explicit flag, environment setting, then bundled configuration. The tools refuse
credentials, query strings and fragments in addresses; HTTPS is required except
for loopback HTTP. A missing/malformed configuration fails before a request and
belongs to the maintainer. No unconfigured run silently targets a local web app.

Ordinary current shopping returns faithful product/store business facts under
the applicable Public API display terms and your request. It needs no separate
provider review or approval flag solely because an assistant participates.
Unknown general provider settings alone do not force count-only output.
`shopping.py --summary-only` is optional; `--data-use-approved` remains accepted
as an optional compatibility acknowledgement and grants no rights. Read
`references/source-permissions.md` in full for private-data, customer-activity,
storage and reuse limits; keep private agreements and credentials out of chat.
The assistant resolves a concrete incompatible use without repeating unchanged
setup. Stored directory and price/history rights remain separate: full
`promotions.py` output requires its client acknowledgement of actual retained-data
rights, an implementation safeguard rather than supplier-required provider review.
Summary still makes a service read and cannot authorize a prohibited path.

#### Shared-service privacy and use

aipersonalized operates the default shared service. Your assistant sends the
ZIP, chosen store, grocery search terms, selected product/item IDs and quantities
needed for your request to that service. For current shopping, the service sends
the needed store and product lookup inputs to Kroger and returns its results.
It calculates requested quantities itself. Stored-only requests read separately
permission-approved observations; they do not contact Kroger or add observations.
Neither route saves your shopping list or search history in the promotion database.

The companion tools save no shopping results and use no cookies, Cart session
or built-in AI service. Your assistant host and chosen model provider receive
the conversation and tool results through their own systems; their storage,
training and sharing controls are separate. Ordinary current business-fact
display has no blanket provider-review prerequisite; known incompatible storage,
customer-activity or reuse needs a specific resolution under the
[source-permission guide](source-permissions.md).
Do not send passwords, supplier keys, account records or payment information.

Cloudflare and hosting infrastructure process connection and request metadata
to deliver and protect the service. The gateway's service locations use failure
status and timing diagnostics rather than logging request bodies, search values,
client addresses or authorization headers. Container logs have size limits;
that does not establish a fixed retention period. Platform log settings and
deletion deadlines are not independently verified, and no zero-logging or
automatic deletion promise is made. Your host may also retain terminal output
or conversations. Keep private inputs out of public support reports; report
only the plugin version and fixed error category to the
[project maintainers](https://github.com/aipersonalized/houston-i-love-kroger-plugin).
Operators using another service address must supply their own accurate disclosure.

Use this service for bounded grocery shopping under the
[Kroger Terms](https://developer.kroger.com/terms) and
[acceptable-use policy](https://developer.kroger.com/documentation/public/getting-started/acceptable-use).
Do not harvest a catalog, track customer searches or locations, alter source
facts, compare competing retailers, or retain, resell or forward source records
beyond the permitted shopping task. The software's MIT license does not grant
rights to Kroger content. These notes are included here so companion use never
depends on opening the web app.

### 4. Optional terminal checks

These commands help a person or host maintainer check the portable tools. They
are not prerequisites the shopper must perform before asking the assistant.

1. Install [Python 3.12 or newer](https://www.python.org/downloads/) if your
   execution host needs it. Run `python --version` in PowerShell or Terminal.
   If your system uses `python3`, use that name throughout. Reopen the terminal
   after installation if the command is unavailable.
2. Open a terminal in `skills/houston-i-love-kroger/`, containing `SKILL.md`.
   There are no Python packages to install.
3. Inspect the commands and check the selected service:

   ```text
   python scripts/shopping.py --help
   python scripts/promotions.py --help
   python scripts/shopping.py status --json --no-input
   ```

   The tool verifies `X-Houston-Service: houston-i-love-kroger-shopping` and
   status's `service` identity/version. Missing or wrong identity is a
   compatibility failure. `configured: true` describes source setup rather than
   proof that a real source search succeeded. Certification/synthetic results
   remain test data; missing history permission need not block current shopping.
4. A synthetic preview makes no request and writes no result:

   ```text
   python scripts/shopping.py products --store TEST0001 --term milk --summary-only --dry-run --json --no-input
   ```

   Expect `status: preview`, `network: false` and `writes: false`, with no real
   offer or check-time claim. TEST0001 is synthetic. Real requests use confirmed
   stores and actual source product/item identities, not copied example IDs.

Machine mode emits one JSON object and never prompts. The clients follow no
redirects, use no ambient proxy or cookies, retry nothing automatically and save
no shopping results. Local qualification uses Python 3.14; other runtimes/hosts
need their own execution checks. Command details are in
`schemas/command-rules.md`, sections "Current-shopping CLI" and "Stored promotion CLI".

### 5. Explicitly request saved deals or dated history

Current shopping is the ordinary grocery route. To use collected data instead,
ask explicitly, for example: "Use saved observations for our chosen store and
show fresh collected milk deals," or "What past prices were recorded for this
package?" A stored-data failure never silently changes to current shopping.

For stored work the assistant:

1. Reuses the accepted exact store, or reads saved ZIP choices and waits for
   your exact selection. Saved choices carry dates and limited coverage; stale,
   missing and fresh-empty directories have different meanings.
2. Discovers readable completed topic labels when latest deals, stored prices
   or quantity estimates need them. An exact collected `topic` differs from a
   live grocery search term. Only relevant fresh topics support recommendations;
   missing/private/legacy labels are not guessed.
3. Uses `promotions.py latest` for qualifying collected deals, `prices` for
   collected package prices, or `estimate` for requested stored-price quantities.
   Regular-only prices are price facts, not promotions. A fresh completed topic
   can correctly contain no deals. `no_data`, `stale` and `permission_required`
   are separate data/authority gaps, not proof the store has no promotions.
4. Uses separate `search`/`retrieve` commands for requested dated observations.
   It preserves exact item/package, currency, observation dates and incomplete
   coverage. An old price is not today's offer or proof of an all-time low.
5. Preserves snapshot age/threshold, partial amounts, missing measure basis and
   currency qualifications. Uniform unknown currency allows only an unqualified
   numeric sum; mixed currencies have no combined total. Complete means line
   arithmetic coverage, never a guaranteed checkout cost.

Stored history starts empty until separate permitted operator collection exists.
Neither shopper searches nor these clients populate it. Stale/missing data is
returned to the operator; the assistant does not refresh it, invent older deals
or ask you to use the web app.

### 6. Recover while keeping the conversation intact

The assistant reports the fixed failure, what was actually checked and the
smallest resolving action. It preserves your requested groceries and any valid
store choice for a later resumed read.

| Result or gap | Meaning and next action |
|---|---|
| No host execution or permitted connector | The host needs a supported client capability. The installed skill alone cannot perform lookups. No browser workaround. |
| `service_configuration_invalid` | Maintainer restores the complete bundled connection, or operator fixes an intentional override. No shopper app-URL request. |
| Unreachable service, wrong identity or missing route | Operator checks the shared-service destination, version and deployment. No web-app endpoint fallback. |
| Concrete privacy/use conflict or stored-data permission gap | Resolve that specific issue privately; no blanket provider review for ordinary current facts. Never paste secrets or grants into chat. |
| Fresh empty result | The bounded query completed with no returned qualifying choices; it is not a service failure. |
| Missing or stale stored data | Explain exact store/topic/date gap; collection is separate operator work. |
| Wrong store, malformed response or incompatible version | Discard the result and report the compatibility problem; do not guess prices. |
| Rate limit or busy response | Respect its delay. The client does not retry or switch modes automatically. |

Exit 0 covers bounded available/empty results, complete/partial estimates and
previews. Exit 1 means request/format failure, 2 invalid input, and 3 a stated
permission/data/capability gap. Partial estimates retain their qualifications.
Keep raw responses, addresses, accounts, tokens and private agreements out of
public support reports. No recovery path asks you to open, install or use the
web app, obtain supplier credentials or set up a database.

## Key Concepts

- **Companion:** independent conversational client of the shared microservice.
- **Service connection:** bundled public destination with optional operator
  override; not a supplier credential, deployment receipt or permission grant.
- **Latest stored result:** a completed dated store/topic sample within the
  operator's freshness threshold; not a live checkout quote.
- **History result:** retained observations with dates and limited past coverage.

## Decision Criteria

Use current service searches for ordinary grocery/deal intent; use the explicit
stored routes for saved prices or history. Ask only for material shopping facts
or genuinely unresolved authority. An absent capability yields an exact gap,
never a shopper web-app task or a fabricated result.

## Constraints & Limits

Host discovery, cross-platform execution, live deployment and source rights each
need actual evidence. Optional upstream human/self-hosting manuals remain raw
reference material for maintainers, not companion shopper instructions. The
companion never uses the web app or directs a shopper there.

## Common Patterns

Grocery intent → reuse service/authority/store context → ask only missing ZIP or
exact choice → call bounded service searches → match packages → estimate only
requested quantities → explain useful picks, dates, coverage and remaining gaps.
