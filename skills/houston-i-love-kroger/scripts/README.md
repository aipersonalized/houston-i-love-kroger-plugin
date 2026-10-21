# Companion tools

`shopping.py` lets assistants use the shared microservice's current-shopping API:
find stores, search requested groceries/promotions, recheck exact products and
freshly estimate selected quantities. Explicit requests can make the server
contact Kroger. No Cart, collection, supplier key or model SDK is needed.

`promotions.py` helps humans and assistants find stored store choices and collected
topics, read deals or dated history, check prices and estimate requested quantities
directly from the shared service. It never contacts
Kroger, starts collection or needs a database mount or supplier key. The other
commands maintain bundled documentation and do not query a shopping service.

## Quick Start

From the skill folder, run:

```text
python scripts/refresh_docs.py --check --json --no-input
```

Read `schemas/command-rules.md` in full before other operations. Paths in that
file resolve from the skill root, one folder above this directory.

For current shopping, run:

```text
python scripts/shopping.py --help
python scripts/shopping.py status --json --no-input
python scripts/shopping.py products --store TEST0001 --term milk --summary-only --dry-run --json --no-input
python scripts/shopping.py estimate --store TEST0001 --item 0000000000001 00001 2 --summary-only --dry-run --json --no-input
```

Both clients automatically load `config/connection.json` in the skill folder.
Operators can override the service with `HOUSTON_SERVICE_URL` or `--base-url`;
ordinary shoppers do not supply a URL or install a web app. Other IDs are synthetic
previews: no network or checked price/time. For a real task, use `shopping.py
stores --zip ZIP`, wait for the person's exact store choice, then `products
--store STORE --term TERM` or promotion-only `deals`. `product --store STORE
--product-id PRODUCT_ID` rechecks an actual thirteen-digit returned ID.
`estimate --store STORE --item PRODUCT_ID ITEM_ID QUANTITY` accepts 1–10 pairs,
whole quantities 1–99. Validated current facts are returned by default;
--summary-only selects fixed diagnostics. Ordinary display needs no separate
provider review or approval flag. --data-use-approved remains an optional
compatibility acknowledgement and grants no rights. Private data, customer
activity, storage and reuse have separate limits. Follow
[the human guide](../references/user-guide.md) for full steps.

Current numeric estimates have unknown currency/purchase context, so they are
not a verified budget or checkout total. Missing groceries stay visible. Full
promotion coverage remains unmet; no command automatically changes modes.

To read stored deals, first check your actual installation:

```text
python scripts/promotions.py --help
python scripts/promotions.py status --json --no-input
```

The status command can report permission_required with exit 3; that is a
successful connection with missing product/history authority. Directory permission
is checked separately by `stores`. Preview the starting path using synthetic examples:

```text
python scripts/promotions.py stores --zip 00000 --summary-only --dry-run --json --no-input
python scripts/promotions.py topics --store TEST0001 --summary-only --dry-run --json --no-input
python scripts/promotions.py latest --store TEST0001 --topic milk --summary-only --dry-run --json --no-input
```

Expect preview status with network/writes false. For an actual read, supply the
configured shared service and use `stores --zip ZIP_CODE` for saved directory choices.
Ask the person which exact name/address they want, then use `topics --store
STORE_ID` for completed fresh/stale scopes. Replace synthetic TEST0001/milk in
the deal example with that accepted full store ID and relevant fresh topic.
These are database reads, never live ZIP lookups. After actual retained-data
rights cover the operation and recipients, omit --dry-run and use
--data-use-approved for records, or --summary-only for fixed state/count/freshness
facts. This stored-client safeguard is implementation policy, not a supplier
requirement for a bespoke provider review.

Latest available can contain fresh deals or a completed empty sample. no_data,
stale and permission_required are distinct exit-3 gaps with no deals; they never
trigger a live-source fallback. Read snapshot dates, age, the operator threshold
(default 24 hours) and coverage. These are collected observations, not live
checkout prices. Search dated history with `search --store STORE_ID --term TERM`.
For a known package price, use `prices --store STORE_ID --topic TOPIC` and select
an actual returned product/item. Estimate requested quantities with
`estimate --store STORE_ID --item TOPIC PRODUCT_ID ITEM_ID QUANTITY`, repeating
--item for up to 10 distinct selections and whole quantities 1–99. Supply the
same service connection and established data-output authority; use --dry-run to preview.
No caller prices are accepted. Complete/partial estimates preserve actual line
arithmetic, unresolved lines, currency/context gaps and excluded checkout costs.
`complete` means calculated line coverage, not a guaranteed checkout total.
Retrieve a specific permitted observation with `retrieve --store STORE_ID
--observation-id OBSERVATION_ID`; use IDs returned by your own search, the same
base URL and the same data-output choice. See
[the user guide](../references/user-guide.md)
for installation, complete steps and recovery. The promotion client never
prompts or writes data.

## What It Does

- Explicitly request bounded current stores/products/promotions through the shared service,
  recheck exact source IDs and estimate requested quantities without persistence.
- Read dated ZIP directory choices and completed topic states; the person
  confirms the exact store, and stale/missing data never causes a live lookup.
- Read bounded latest store/topic snapshots, search dated history and retrieve
  selected observations with no automatic retry, collection or local cache.
- Check stored regular/promo prices and estimate source-verified whole-unit
  quantities, preserving partial sums, missing currency and unresolved lines.
- Collect six explicitly selected public first-party app Markdown documents.
- Audit their inventory, exact bytes, identities, version, exclusions and hashes.
- Optionally compare the snapshot with an explicitly selected app checkout.
- Refresh the selected snapshot locally; never query a shopper, account or API.

## Requirements

Python 3.12 or newer, standard library only. Executed here with Python 3.14.
Keep the complete skill folder, including service_connection.py and config.
An equivalent permitted client can use the shared service contract. The companion
and web app are independent clients; no shopping path uses the web page or asks
the person to finish there. Documentation collection
requires ordinary local files, not linked paths.

If you want to run these optional maintenance commands:

1. Install Python from the [official Python downloads](https://www.python.org/downloads/)
   if it is not already installed. Open PowerShell on Windows or Terminal on
   macOS/Linux, then change into the companion's folder containing `SKILL.md`.
2. Run `python --version` and check that it reports 3.12 or newer. On macOS/Linux,
   use `python3 --version` if that is the installed command, and replace the
   initial `python` in every example here with `python3`.
3. If the command is missing after installation, close and reopen the terminal.
   For an audit failure, follow the returned recovery message and the command
   contract; do not delete unrelated files. Use the plugin's
   [help guidance](../../../README.md#help-and-feedback) if you need to report a
   problem, removing private paths, configuration and data before sharing output.

## Examples

Optional maintainer commands, run from the skill folder. Replace
`PATH_TO_APP_CHECKOUT` with the actual app source folder to collect or refresh
manuals; ordinary plugin use and offline `--check` need no app checkout:

```text
python scripts/fetch_docs.py --url repo:/ --output research/official_docs --repository PATH_TO_APP_CHECKOUT --json --no-input
python scripts/refresh_docs.py --check --repository PATH_TO_APP_CHECKOUT --json --no-input
python scripts/refresh_docs.py --refresh --repository PATH_TO_APP_CHECKOUT --json --no-input
python scripts/list_skill_steps.py
```

The final command is the read-only step utility. It prints Markdown playbook/step
headings; --json, --no-input, --no-color and --help are also supported. Fetch/audit commands support human
text, `--json`, `--no-input`, `--no-color`, `--verbose` and `--help`. They never
prompt. Help is plain text; JSON execution returns one object. See the command
rules for exits, file effects and recovery after interrupted writes.
