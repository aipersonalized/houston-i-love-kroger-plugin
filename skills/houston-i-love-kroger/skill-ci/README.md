# Companion skill maintenance and qualification guide

## Who

People ask for grocery help in conversation; permitted agents call the shared
shopping microservice for current shopping or separate stored deals/history.
The companion and web app are independent consumers. The companion never uses
the web app or asks the shopper to open, install or use it, including on failure.
Maintainers
own source/contract reconciliation. An
independent reviewer assesses the actual candidate and evidence. If model trials
are explicitly requested later, an orchestrator assigns a fresh trial agent and
separate reviewer; the author does not call a static walkthrough a trial.

## What

Supported tasks include current ZIP choices, requested product/promotion
searches, exact product rechecks and fresh selected-quantity estimates. Stored
tasks remain setup help, saved ZIP choices, completed-topic discovery,
latest completed store/topic snapshots, stored
item price checks, requested-quantity/budget estimates and separate history
search/retrieval. The person confirms the exact returned store or reuses a valid
confirmation. Live shopping calls only the shared service, which can query the source;
stored mode never refreshes it. Neither mode starts collection or Cart.
A useful shopping answer explains supported discounts and low whole-package
prices separately, matching supplied preferences. It preserves store/topic,
snapshot/observation dates, age and bounded coverage, full source facts,
separate arithmetic and missing unit/history facts without a raw DTO dump.
Concrete private-data/use conflicts and missing stored rights block their
dependent exposure. Ordinary current business-fact display has no blanket
provider-review prerequisite. Required inputs and effects are owned by `SKILL.md` and its
procedures, not by a maintenance record.

## When

Review after a concrete failure, shared-service contract/source change, host/tool change,
new intended use or an explicit review request. Recheck permission when its
actual recipients, scope or validity change. Do not turn this into repeated
confirmation for unchanged established authority.

## Where

The retained design is `skill-ci/skill-design.md`; findings/source scope are in
`research/research-brief.md`. The selected first-party manuals are under
`research/official_docs`, with inventory and hashes. Commands are in
`schemas/command-rules.md`; scripts are locally self-contained. Synthetic static
cases are in `evals/scenarios.json`. Creator validation can write a local
report under the ignored `evaluations/` directory; generated reports and
private maintenance records are not part of the public skill. Return
deterministic source-tool results to the caller's designated record owner.

## Why

Exact store/topic identity, sample limits and incomplete source fields make an answer
misleading if context is dropped. Distinguish permitted current business facts
from private inputs, customer activity, retained copies and independent reuse;
check the actual issue rather than treating a provider's presence as a blocker. Old regular prices, package text or
synthetic fixtures cannot repair missing historical or normalized-unit facts.
Stale/no-data and fresh empty snapshots differ; none triggers live-source or
history fallback. A failed attempt does not refresh the last completed sample.

## How

For a revision, inspect the current design, source inventory, complete affected
sources and actual service/client implementation. Refresh the selected manuals using the
documented local CLI and reconcile changed instructions; hashes alone do not
prove comprehension. Preserve the development record and unrelated work.

Maintain this skill only inside the standalone plugin. When its public file set
changes, update the plugin packager's explicit allowlist and run its isolated
extraction tests. Ordinary use and offline documentation audit must work without
the app checkout; refreshing manuals requires an explicit `--repository` path.
Review the exact source and ZIP together before publication. Portable command
tests do not establish host-specific import, discovery or activation. Raw
upstream human/self-hosting manuals are maintainer references; they cannot
reintroduce shopper browser steps or app-installation recovery.

Run the creator's canonical artifact checks and workflow validator within the
authorized report-writing scope. Run local source-tool and promotion-client tests and review
their actual limits. Walk through the static scenarios, including returns and
resumption; report them as authored trace checks.

For requested model trials, supply realistic permitted installation/input/tool
context and natural task requests to fresh agents, without evaluation hints.
A separate reviewer checks available execution history, artifacts and outcome,
reports exact root causes and missing evidence, and returns fixes to their owner.
After corrections, repeat affected checks and only authorized trial cases. No
model tests, live searches or private account reads were performed by authoring.

## Quality Criteria

- Exact store/topic, source, snapshot/observation dates, freshness and limited
  coverage survive every handoff; request time never substitutes for observation.
- Full source facts and calculations are distinguishable; no silent truncation.
- Fresh empty, no completed collection, stale, permission-required and failed
  reads remain distinct. Missing unit basis and price qualification stay explicit.
- Setup facts, instructions and actual live success are not conflated.
- Ordinary grocery/deal intent routes directly to service tools without a
  technical invocation, shopper URL request or repeated unchanged setup review.
- The bundled connection and operator overrides select the service; the client
  verifies its response identity. A configured public URL is not a live receipt.
- A missing host client, unavailable service or missing data yields the exact
  dependency; no recovery path uses or recommends the web app.
- Current display uses its applicable Public API basis without a mandatory
  provider review or approval flag. Unknown general provider settings alone do
  not force summaries. Actual source/private-data/storage/reuse limits remain.
- Commands, paths, snapshots, documented exits and recovery match implementation.
- Useful shopping picks explain supported value versus low package outlay;
  unnamed/incomplete rows and stale/expired data never get invented recommendations.
- Price/quantity estimates use real source-backed arithmetic, distinguish
  complete line coverage from checkout cost, and disclose partial sums,
  unresolved lines and unknown/mixed currency/context without inference.
- A task finishes at its bounded current or stored result; no purchase,
  collection, Cart or silent source/history fallback follows.
- Current source/page/store/date/estimate bindings are checked, with unknown
  currency, unresolved groceries and nonexhaustive coverage explicit. Full
  current facts are the default; optional summaries omit records. The stored
  client's acknowledgement is an implementation safeguard for actual retained-data rights.

## Evaluation Evidence

Static and deterministic check results must identify their candidate and method.
The workflow report covers structure, links and recovery-section presence only.
The documentation audit covers the selected bytes/inventory, not legal rights,
hosted availability or agent compliance. Independent review and model/live
qualification remain separate gates. Any future evidence must say exactly what
ran; no passing source check substitutes for an unobserved session.

For the current-output correction, synthetic subprocess checks must cover stores,
products, deals, exact rechecks and estimates without an approval flag, full
validated named facts, optional summary stripping, unchanged status/error/private
field rejection and optional flag compatibility. These checks qualify the CLI,
not a human-facing agent result. Earlier fictional trials retain their actual
version and limits. A requested real conversational evaluation must show useful
source-backed choices through the authorized output path; local RAM/count-only
checks cannot establish that outcome.
