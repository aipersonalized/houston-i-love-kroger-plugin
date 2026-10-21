# Check the companion client and shared service connection

Establish whether the companion can complete the requested grocery task, or
name the exact host, service, permission or data gap. Keep the shopper's task in
the conversation. Never use the web app or ask the shopper to open, install or
use it, including when no client or usable data exists.

## Continued From

`SKILL.md` companion installation/recovery route or a failed current/stored
request. Setup-only requests finish here. Reuse valid installation, permitted
task scope and confirmed store rather than restarting setup for each grocery list.

## Resources

For plugin installation, read `references/user-guide.md` in full. Before service
status, read `references/api_reference.md` and `schemas/command-rules.md` sections
"Service connection", "Current-shopping CLI" and "Stored promotion CLI" in full.
For a concrete source-use or privacy issue, read `references/source-permissions.md`
in full. Upstream human/self-hosting manuals are not shopper recovery procedures.

## Step 1: Identify the requested result and available client

Distinguish plugin installation, connection diagnosis, an interrupted shopping
request and unsupported Cart/collection work. Check whether the assistant host
can execute Python 3.12+ or use an equivalent permitted service client. An
installed skill folder alone does not install a remote connector.

If the client capability is absent, explain which host execution/connector
capability is missing. Supply companion installation steps when requested and
stop dependent reads. Do not invent completed setup, direct supplier access or
a browser workaround. Cart, sign-in, checkout and collection are unsupported
companion operations; explain that limit without redirecting to the web app.

## Step 2: Use the bundled connection and inspect the requested mode

The tools automatically load `config/connection.json` inside the skill folder.
It selects `https://aipersonalized.io/api/houston-i-love-kroger/` as the public
service base. That configured destination does not establish that its live
deployment is available or qualified. Do not ask the shopper to supply an app
URL or run a local app. Only an operator choosing another compatible service
uses `HOUSTON_SERVICE_URL` or `--base-url`; the explicit flag takes precedence.

A missing/malformed connection reports `service_configuration_invalid` before
network access. Restore the complete plugin or return the configuration defect
to its maintainer. Do not guess a localhost address. Never request Kroger keys,
private service tokens, `.env` contents, a database mount or private grants.

For current shopping, run `python scripts/shopping.py status --json --no-input`
from the skill folder. The client checks the `X-Houston-Service` response header;
status must identify `service: {name: "houston-i-love-kroger-shopping", apiVersion: 1}`.
Wrong/missing identity is a compatibility gap, even when the endpoint returns
HTTP 200. Check configured/environment/capability facts. Configured does not
establish working supplier credentials; synthetic/certification data is not a
real offer. Missing stored-history permission does not block independently
permitted current shopping and never requires shopper database setup.
Ordinary current business-fact display needs no separate provider review or
approval flag; unknown general provider settings alone do not block it. Resolve
only a concrete protected-data, customer-activity, storage or reuse conflict.

For an explicitly stored task, run `python scripts/promotions.py status --json
--no-input`. This checks only stored-service permission/availability, not whether
the accepted store/topic has a fresh completed collection. Directory rights are
separate; judge a directory read by that operation's actual result. Instructions
given to a person are not completed installation or successful service access.

## Step 3: Resolve only the observed dependency

| Condition | Action |
|---|---|
| Missing Python or permitted client | Explain the host execution/connector gap; use the companion installation guide when requested. No browser fallback. |
| `service_configuration_invalid` | Maintainer restores the bundled connection; an operator checks an intentional service override. No shopper app-URL question. |
| Unreachable service or wrong/missing service identity | Report the connection/compatibility gap; operator checks the actual service route/version. Do not use the web app endpoint. |
| Current source unconfigured or a documented route absent | Operator repairs shared-service configuration/version. No history database or app installation is assigned to the shopper. |
| Missing current store or package | Return to `playbooks/live-shopping.md`; ask only the unresolved shopping input or reuse accepted IDs. |
| Stored `permission_required` or `recipient_permission_required` | Return the actual retained-data dependency to the operator. The stored client's acknowledgement gate is implementation policy, not a supplier requirement for provider review; it grants no rights or server bypass. No mode change. |
| Concrete current privacy/use conflict | Stop only the affected path and identify the incompatible processing or protected output; no blanket provider-review prerequisite or fabricated permission. |
| Stored mode missing store/topic | Use `playbooks/choose-store-and-topic.md`; stored choices, exact person choice and completed topics. |
| `no_data` / `no_completed_collection` | Explain the exact missing completed scope; collection is separate operator work. |
| `snapshot_not_readable` | Explain permission/retention prevents reading that sample; no older replacement. |
| `stale` | Report collection age/threshold and operator dependency; this reader cannot refresh it. |
| Fresh `available` with zero deals | Report the completed empty bounded topic; this is not a connection defect. |
| Invalid input or rejected cursor | Correct the field once; restart only the requested bounded read when its snapshot changed. |
| Busy/quota response | Respect its delay; do not loop, switch endpoints or restart services. |
| Unsupported/oversized/malformed response | Discard it; operator checks service API compatibility. |

Missing stored data never triggers live shopping, historical substitution or
collection. Do not initialize/populate a database or repeat unchanged failures.
A new historical request is a separate task, not repair for stale latest data.

## Step 4: Return the result and stop or resume the requested read

State checks actually run, the observed service/client state and the smallest
resolving action. For setup-only, stop. For an interrupted authorized shopping
task, return accepted task scope, confirmed store, requested groceries and
selected items, or the stored topic/history scope, to that read procedure.
Resume only after its actual dependency is resolved. A fixed status diagnosis
does not establish that a source lookup or agent task succeeded.

## Gotchas

- The companion and web app are independent consumers of one shared service.
- The public service connection contains no supplier or private storage token.
- Service status, source access, stored collection and source/recipient rights
  are distinct facts; valid existing authority does not need repeated approval.
- Plugin installation needs no AI-provider account or model SDK in the core.

## Checklist

- [ ] The requested task and host client capability are identified.
- [ ] The tools use their selected service connection and verify service identity.
- [ ] Status and actual source/data success are reported separately.
- [ ] Only genuinely missing inputs or changed authority became questions.
- [ ] No web-app use, shopper app setup, credentials or private database was required.

## Recovery from interruption

Reuse unchanged accepted setup, store, request and authority. Check only facts
invalidated by a changed client/service/recipient or failed request. Preserve
unknown outcomes and stop unchanged retries. No recovery path uses the web app,
direct supplier access, Cart or source collection.

## Handoff

Producer: companion setup/recovery. Receiver: caller or the interrupted requested
current/stored procedure. Deliver actual client/service checks, accepted scope
and any applicable recipient limits, source/data state and the unresolved dependency. The receiver
checks these facts before resuming. Stop at the requested setup result or exact
gap; no browser or app-installation handoff follows.
