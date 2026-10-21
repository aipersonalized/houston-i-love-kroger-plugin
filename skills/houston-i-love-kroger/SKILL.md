---
name: houston-i-love-kroger
description: "Help with Kroger groceries, good deals, package prices and shopping quantities, including ordinary grocery requests that do not name this skill. Infer the person's shopping intent, call the shared shopping microservice and explain useful returned choices. Confirm the exact store and preserve package preferences, dates and bounded coverage. Never use or send the shopper to the web app."
---

# Houston I Love Kroger

Help a person plan groceries through the shared shopping microservice: understand their list,
find and confirm their exact store, match returned packages, check current prices
and estimate requested quantities. Preserve a separate stored-only workflow for
collected deals and dated history, with collection dates and freshness.
The companion and web app are independent projects that consume the same
microservice. Infer grocery and deal intent from the conversation, call the
service tools yourself and return useful choices in the conversation. Never use
the web app or ask the shopper to open, install or use it, including on failure.
Current-shopping requests can make the service contact Kroger; stored reads
never refresh the source. Neither starts collection or Cart.

**Readiness:** standalone plugin with an API-version-1 portable core. The complete
plugin root includes its own README, license and tools; no app checkout or private
Kroger API technology skill is required. The bundled connection selects the
service; shoppers do not supply an app URL or deploy anything. Optional host import remains untested.
Deterministic CLI checks,
documentation integrity, actual installation availability and observed agent
performance are separate evidence. This skill does not establish live source
entitlement, source/recipient rights or deployment of a proposed public URL.

## Core Principles

- Bind every price to the exact accepted store and source retrieval time, or
  collected topic/snapshot/observation time in stored mode. No bounded search is
  every store promotion. Full promotion coverage remains an unmet requirement.
- Keep source descriptions and prices separate from calculated savings. Current
  regular price is never a substitute for a prior promotional price.
- Price checks preserve the selected item/package and source currency. Cost
  estimates need actual supported service arithmetic, requested quantities and
  explicit unresolved lines; missing currency/weight is never guessed.
- Use the applicable Public API display terms for bounded current shopping.
  Faithful product/store business facts can enter the requested conversation
  without a separate provider review or approval flag. Resolve concrete private
  data, customer-activity, storage or reuse conflicts; unknown general provider
  settings alone do not block ordinary display. Stored data needs its own rights.
- Keep fresh stored deals, a fresh empty result, stale data, no completed
  collection, empty history and absent permission distinct. A request timestamp
  does not make stored prices newly observed.

## Context Requirements

This skill requires:
- Python 3.12+ execution or an equivalent permitted client for the shared service
  API. Use the bundled `config/connection.json` automatically; an operator may
  override it with `HOUSTON_SERVICE_URL` or `--base-url`. Do not ask the shopper
  for an app URL. Configuration does not establish deployed service availability.
- A five-digit US ZIP for the chosen live or stored store-discovery mode, or an already accepted complete
  eight-character store ID. Show returned choices and ask which exact
  name/address the person wants; never choose the first result for them.
- Applicable source access and the person's requested purpose. Ordinary current
  display uses its Public API basis; private data, customer activity, retention
  and secondary use require their own applicable authority and privacy boundary.
  Stored reads additionally need actual retained-data rights; reuse valid scope.
- For latest deals/prices, a topic returned by stored completed-topic discovery
  or an already verified collection scope. For dated history, optional literal
  term, product/item IDs and UTC time bounds.
- For live shopping, requested groceries, quantities and any supplied budget,
  brands, package preferences and acceptable substitutions. Ask about material
  ambiguity; do not invent quantities, a budget or permission to substitute.

This skill produces:
- A useful current shopping list: named source-backed packages, requested
  quantities, supported numeric line/subtotals, unresolved items and source
  times/coverage. Missing currency prevents a verified monetary budget fit.
- Stored store choices with name/address, collection dates and limited search
  coverage, followed by the person's exact choice and completed-topic states.
- Latest collected deals or dated historical observations with full source facts,
  dates, unit/history limits and bounded coverage; or a precise stale, no-data,
  empty, permission or connection result with the next practical action.
- Price checks and requested-quantity estimates within supported collected scope,
  distinguishing known package prices, qualifying discounts, partial subtotals
  and unresolved quantities/currency/stock. Unsupported capabilities stay gaps.
- For setup requests, ordered installation/configuration guidance and the actual
  checks performed, without credentials or an invented deployment claim.

## Use Cases and Scenarios

Match the first applicable situation. Read the named playbook in full.

| User situation | Purpose | Workflow | Expected result |
|---|---|---|---|
| Ask for groceries, good deals, nearby stores, current package prices or shopping quantities, without needing to name this skill | Infer shopping intent and call the shared service tools | read `playbooks/live-shopping.md` in full | Current bounded store choices, or person-confirmed exact store with useful matched deals/packages and qualified estimate; precise input/access gap when needed |
| Explicitly request saved ZIP/store choices, a stored directory, or completed collection topics | Find stored store choices and completed topic scopes | read `playbooks/choose-store-and-topic.md` in full | Exact person-selected store and relevant fresh topic, or precise directory/data gap |
| Explicitly check collected prices or estimate from saved observations | Use stored prices and source-verified estimate arithmetic | read `playbooks/price-check-and-estimate.md` in full | Dated price facts and qualified full/partial estimate, or exact input/data gap |
| Find or compare the latest collected deals for an accepted store and topic | Read the service's latest completed collection | read `playbooks/main-procedure.md` in full | Fresh dated deals, fresh empty result, stale/no-data result or a permission gap |
| Search or retrieve dated past observations | Read retained history separately from latest deals | read `playbooks/stored-promotions.md` in full | Dated source observations or an explicit permission/availability gap |
| Install the companion, check its service connection, recover a failed request or ask for unsupported Cart/collection actions | Establish the companion's actual client/service capability | read `playbooks/setup-and-recovery.md` in full | Working prerequisite checks or the exact host, service or unsupported-operation gap; no web-app handoff |

## Scenario Workflows

### Current shopping

| Order | Read in full and execute | Accepted result |
|---|---|---|
| 1 | `playbooks/live-shopping.md` | Person-confirmed exact store, bounded matched groceries and qualified estimate or explicit gap. |

### Stored store and topic choices

| Order | Read in full and execute | Accepted result |
|---|---|---|
| 1 | `playbooks/choose-store-and-topic.md` | Confirmed stored location and relevant completed-topic states. |

### Stored price checks and estimates

| Order | Read in full and execute | Accepted result |
|---|---|---|
| 1 | `playbooks/price-check-and-estimate.md` | Dated package facts and qualified requested quantities or unresolved lines. |

### Latest stored deals

| Order | Read in full and execute | Accepted result |
|---|---|---|
| 1 | `playbooks/main-procedure.md` | Fresh completed-topic deals, bounded empty result or explicit data/permission gap. |

### Dated observations

| Order | Read in full and execute | Accepted result |
|---|---|---|
| 1 | `playbooks/stored-promotions.md` | Dated selected history with source and store bindings preserved. |

### Plugin installation and recovery

| Order | Read in full and execute | Accepted result |
|---|---|---|
| 1 | `playbooks/setup-and-recovery.md` | Actual connection checks or the smallest stated installation dependency. |

### Procedure Sequence

| Stage / owner | Prerequisite and output | Receiving check | Next / return / stop |
|---|---|---|---|
| Live shopping, `playbooks/live-shopping.md` | Bundled service connection and inferred permitted current request → live ZIP choices → person's exact store → bounded product searches → matching packages → requested selected-product estimate | Check service identity, store/term/source/date/page bindings, quantities, package preferences, arithmetic, unknown currency/basis and unresolved lines | Finish requested shopping answer without a blanket provider-review gate; optional dated history is separate; a failed stored read never enters this route automatically |
| Setup, `playbooks/setup-and-recovery.md` | Companion client and its selected service configuration → verified service identity/status or exact dependency | Accept usable service connection and the requested operation's actual scope; stored rights stay separate | Resume the requested read only; setup-only stops; no shopper web-app task |
| Store/topic choice, `playbooks/choose-store-and-topic.md` | ZIP or accepted store and permitted recipients → stored directory → person's exact choice → completed topics | Check directory date/coverage, confirmed store and each topic's freshness/state | Continue the requested deal/price/estimate task; dated history needs the accepted store only |
| Latest deals, `playbooks/main-procedure.md` | Accepted store/topic/recipient → latest completed snapshot → bounded report | Caller checks snapshot age, scope, source facts and result state | Complete, or return connection to setup and missing store/topic to its owner |
| Price check/estimate, `playbooks/price-check-and-estimate.md` | Accepted store/topic/item and requested quantities → stored-price read and supported estimate | Caller checks source identity, currency, quantity, line arithmetic, partial totals and exclusions | Complete with qualified costs or explicit unresolved lines; never live fallback |
| Dated history, `playbooks/stored-promotions.md` | Accepted store/recipient and history scope → bounded search or selected record | Caller checks observation dates and query/store binding | Complete; no automatic fallback between history and latest |

Direct read entry accepts current equivalent inputs; do not repeat setup, store
choice or authority already established. In stored mode, missing store/topic enters the stored
discovery procedure before the requested read. Changed store, topic, query,
recipient or installation invalidates dependent results. Read procedures are
alternatives; stale/empty data never triggers a live search, collector or hidden
history substitution. Never use the web app or send the shopper there, even
when the client, service, source authority or requested data is unavailable.

## Completion Criteria

- The requested live-shopping, stored-data or setup result exists and follows
  `schemas/output-contract.md`; no response from an old store/query is reused.
- Every price is traceable to its accepted store, source and retrieval or observation/snapshot
  time, with source facts and calculations distinguishable.
- Fresh empty, stale, no completed collection, unknown history, missing unit
  basis, test data and permission gaps remain visible. Stop at the bounded result.
- The shopper receives useful service-backed choices or an exact capability gap
  in the conversation; no web-app visit, installation or URL task is assigned.

## Supporting Resources

- Before receiving source records, read `references/source-permissions.md` in full.
- Before service requests or interpreting results, read `references/api_reference.md`
  in full; read `research/official_docs/pages/API.md` in full for exact fields,
  error categories and limits.
- Before returning a comparison, read `schemas/output-contract.md` in full.
- For companion installation and conversational use, read `references/user-guide.md` in full.
- Before documentation maintenance or the optional step-listing command, read
  `schemas/command-rules.md` in full.
- Before the promotion CLI, read `schemas/command-rules.md` section
  "Stored promotion CLI" in full. It needs no Kroger credential or direct
  database access; actual retained-data rights and its stored-client acknowledgement apply.
- Before the current-shopping CLI, read `schemas/command-rules.md` section
  "Current-shopping CLI" in full. `shopping.py` uses only fixed service routes;
  its store/product/estimate operations can cause bounded supplier reads.
- Before revising this skill, read `skill-ci/README.md`,
  `skill-ci/skill-design.md` and `research/research-brief.md` in full. The
  development project record has a separate writer and is not a shopping input.

## Critical Constraints

- Use only the shared shopping microservice's documented API. Never use the web
  app or ask the shopper to use, open or install it, including during recovery.
  Live source reads follow the current-shopping procedure for the grocery intent
  expressed by the person; no special technical invocation is needed. Never call
  Kroger directly, a collector, Cart, sign-in or checkout through this companion.
- Missing or stale data is an operator/data gap, not permission to refresh the
  source. No database mount, SQL, supplier credentials or model SDK is required.
- Ordinary same-shopper current display is supported by the applicable Public
  API terms, not a general downstream reuse grant. Do not invent a blanket
  provider-review requirement or assume rights for customer tracking, retained
  copies, source-private records or independent reuse; check the affected use.
- Keep protected values, credentials and raw private records outside model
  context. A tool that automatically exposes disallowed payloads is unsuitable.
- Preserve full source descriptions and IDs, missing facts and monetary units.
  Do not compare this feed with competing retailers or harvest it into a cache.
- Do not label an unqualified estimate as `$/oz`, `$/lb` or a known per-item
  measure, fabricate prior prices, or call a collected low an all-time low.

## Recovery States

- **Completed:** the requested task and applicable checks are satisfied; live
  claims describe only the actual session and response observed.
- **Completed with gaps:** a useful bounded comparison or setup explanation is
  delivered with missing optional prices/history or untested conditions named.
- **Blocked:** required installation, exact store choice, permitted transport or
  source authority is absent. Give the smallest resolving action and stop the
  dependent operation while preserving useful permitted guidance.
