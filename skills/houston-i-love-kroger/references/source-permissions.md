# Use source data for the requested shopping task

## Detailed Content

Distinguish ordinary current display from retained datasets, private records and
customer activity. The [Public API acceptable-use policy](https://developer.kroger.com/documentation/public/getting-started/acceptable-use)
permits faithful product and store display with relevant field filtering. Under
the [Terms](https://developer.kroger.com/terms), applicable additional API terms
control a conflict. This supports the companion's bounded same-shopper current
display on a contextual reading; it is not a general reuse or API-resale grant.
API availability, customer consent and policy files do not expand that scope.

Read the bundled [shared-service privacy and use disclosure](user-guide.md#shared-service-privacy-and-use)
for the default operator's data flow, hosting-log limits and support boundary.
No web-app visit is required. A different service operator must provide an
accurate policy for its own installation; this disclosure is not a source grant.

For the source questions, read
`research/official_docs/pages/KROGER_PERMISSION_REQUEST.md` in full. The request document is not itself a permission grant. For history's implemented default gate,
read `research/official_docs/pages/HISTORY.md` section "1. Understand the source requirement".

The shared service makes no built-in AI request. The companion calls only its
public API; current calls can query Kroger, while stored reads never refresh it.
Neither mode uses the web app or sends the shopper there, including on failure.

For ordinary current shopping:

1. Use the person's grocery request and permitted ZIP/store inputs for that
   task. Return faithful product/package facts, prices and store business
   names/addresses in the conversation. These business facts are not automatically
   the person's private address, account, profile or behavioral history.
2. No separate supplier approval, provider-specific review or local model is
   required solely because an assistant participates. Unknown general provider
   settings alone do not force summary mode. `shopping.py` returns validated
   current facts by default; `--summary-only` is an optional diagnostic choice.
   Its accepted `--data-use-approved` flag is optional compatibility syntax,
   not a review token or permission grant.
3. Preserve actual access, source facts, request bounds and user privacy. Stop a
   concrete incompatible use: protected-value exposure, retained catalog copies,
   customer-search/location tracking or storage, or unauthorized secondary use.
   Resolve only the facts that affect that issue; do not assume incompatibility
   from a provider's name or demand private agreements in chat.

The AUP's customer-search/frequent-view and customer-location restrictions are
distinct from its product/store display permission. Terms section 5e still
limits permanent copies, caches and specified redistribution absent an applicable
basis. The examined public texts prescribe no named-provider review procedure
or express model-training rule. Training or independent reuse can nevertheless
involve restricted copies, datasets or customer activity; ordinary display does
not authorize those uses. A known incompatible processing path remains a real
issue, not an exception created by this guide.

Stored directory collection/display/agent access and product-history access are
separate purposes requiring actual retained-data rights. Check the requested
operation's grant and result. A product-history gap does not reject an independently
permitted stored ZIP directory, and a directory grant does not grant price access.
`promotions.py` requires `--data-use-approved` for full stored records as an
implementation safeguard acknowledging the applicable retained-data scope. That
flag neither creates rights nor bypasses server policy; it is not a
supplier-mandated bespoke provider review. Reuse valid scope evidence, including
any actual recipient/field/retention limits, without exposing private agreements.

Apply the person's protected-value rules independently. Any provider may receive
public facts and permitted task results where those rules allow them. A tool
that exposes protected private inputs or source-private records is unsuitable:
use an available permitted adapter with a supported output boundary, or explain
that exact capability gap. Do not expose private records first and redact them
afterward. Preserve the requested groceries and valid store context; no web-app
handoff follows. Ordinary current access does not authorize collection/history.

## Key Concepts

- **User authorization:** which task and effects the person requested.
- **Source authority:** rights granted by the relevant data source or agreement.
- **Recipient:** every actual processor/viewer, including model/tool services.
- **Bounded permission result:** reviewed scope without disclosure of the
  underlying private agreement or customer information.

## Decision Criteria

| Known condition | Permitted next step | Limit |
|---|---|---|
| Ordinary bounded current shopping under applicable display terms | Return validated current business facts in the conversation without an approval flag | Preserve source facts, user privacy and bounded purpose; no independent reuse grant. |
| Concrete incompatible processing or protected output | Stop the affected path and resolve that specific issue | Optional diagnostics cannot authorize a prohibited path or replace useful shopping choices. |
| Actual stored grant covers the requested operation and recipients | Use full stored mode with its client acknowledgement | Honor the grant's fields, purpose, retention and validity; the flag grants none. |
| Stored rights are missing, expired, revoked or outside scope | Return the exact source dependency; fixed diagnosis when permitted | A prior response or current-display permission does not create retained-data rights. |
| Only synthetic fixture data is used | Clearly labeled deterministic development checks | Never call it live shopping evidence. |

## Constraints & Limits

Do not request agreement text, passwords, secrets or private customer inputs in
chat. Keep source text/prices unchanged and mark separate arithmetic. Do not
store search-derived behavior, create a catalog cache, compare competing
retailers, activate the history collector or send a permission inquiry as part of
ordinary reads. Stale/empty/no-data results never authorize live-source searches
or a collector fallback. A distinct task may authorize operator work; this skill does
not supply that authority or implement the collector.

## Common Patterns

An ordinary grocery request proceeds to bounded current service calls and useful
choices. A known customer-activity logger, permanent response archive or private
record exposure requires its own concrete resolution. A stored-history denial
remains a separate source/data gap. Reuse unchanged accepted scope, ask only for
material missing shopping facts, and never redirect the shopper to the web app.
