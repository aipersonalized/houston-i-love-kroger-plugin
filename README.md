# Houston I Love Kroger plugin

Tell your assistant what you need. It finds nearby Kroger stores, confirms your
location, searches suitable groceries and reports useful deals and price checks
through our shared microservice. Separate
commands read permission-approved stored deals and dated history. The plugin
does not call Kroger directly, collect history, or manage Cart or checkout.

This folder is the complete portable plugin. It includes its skill, Python tools,
manuals, schemas, synthetic tests and [MIT license](LICENSE). It has its own
[source repository](https://github.com/aipersonalized/houston-i-love-kroger-plugin),
separate from the app. You can extract its ZIP anywhere;
you do not need the app's source checkout, Node.js, a provider SDK, supplier keys,
or the privately maintained Kroger API technology skill.

## 1. Get the complete plugin

1. Click [Download plugin ZIP](https://github.com/aipersonalized/houston-i-love-kroger-plugin/releases/download/v0.2.0/houston-i-love-kroger-plugin.zip)
   and save `houston-i-love-kroger-plugin.zip`.
2. Extract all files. On Windows, right-click the ZIP and choose **Extract All**;
   on macOS, double-click it; on Linux, use your archive manager's extract action.
3. Open the resulting `houston-i-love-kroger-plugin` folder, which contains this README,
   and keep the complete folder together. Do not copy only `SKILL.md`: its scripts
   and manuals are required too. A checkout of the plugin's own repository can
   use its entire root folder instead.

The plugin and web app are independent clients of the same shared service.
Your assistant performs the shopping task and gives you the answer in the
conversation. No web-app visit, web-app installation or supplier key is required.

## 2. Make it available to your assistant

Use your assistant host's supported local-plugin or Agent Skills installation
method. The portable entry point is
[`skills/houston-i-love-kroger/SKILL.md`](skills/houston-i-love-kroger/SKILL.md).
Keep its complete folder together. If your host can read files but has no
importer, ask it to read that entry point explicitly; this is manual use.

An optional [Codex adapter](.codex-plugin/plugin.json) declares `skills: "./skills/"`.
Its format follows locally inspected installed Codex plugin manifests. Actual
host import, discovery and activation have not been tested. Other hosts can use
the same portable skill without that adapter. No host or model account is required
by the core tools; your assistant's own requirements remain separate.

## 3. Check the runtime and connection

1. Install [Python 3.12 or newer](https://www.python.org/downloads/) if needed.
   Open PowerShell on Windows or Terminal on macOS/Linux and run `python --version`.
   If your system uses `python3`, use that command throughout these instructions.
2. Open a terminal in this plugin folder. No Python packages need installation.
3. Keep the bundled [connection file](skills/houston-i-love-kroger/config/connection.json).
   Both tools load it automatically. It selects the project's shared service;
   ordinary users do not need to enter an address. Operators using their own
   compatible service can set `HOUSTON_SERVICE_URL` or pass `--base-url` with its
   complete service address ending in `/`. An explicit command override wins.
4. Read the [source-use guide](skills/houston-i-love-kroger/references/source-permissions.md).
   Ordinary current shopping returns faithful product/store business facts in
   the conversation without a separate provider review or approval flag.
   Private data, customer tracking, retained copies and independent reuse have
   separate limits; stored history needs actual retained-data rights.
   Keep agreements and credentials private.
   The bundled [shared-service privacy and use notes](skills/houston-i-love-kroger/references/user-guide.md#shared-service-privacy-and-use)
   explain the default operator's data flow and hosting-log limits without a
   web-app visit.

## 4. Check the tools

From this plugin folder:

```text
python skills/houston-i-love-kroger/scripts/shopping.py --help
python skills/houston-i-love-kroger/scripts/promotions.py --help
python skills/houston-i-love-kroger/scripts/shopping.py products --store TEST0001 --term apples --summary-only --dry-run --json --no-input
```

The last command uses synthetic identifiers and makes no request. Expect a
preview with network and writes false. Check the shared service with:

```text
python skills/houston-i-love-kroger/scripts/shopping.py status --json --no-input
```

Configured status is a setup fact, not proof of a successful supplier lookup.
Stored history can remain permission-required while current shopping works.

## 5. Plan groceries or read stored history

Ask your assistant: "Find stores for my ZIP and let me choose the location. Then
help me find apples, chicken, rice and paper towels, checking the packages with me."
Supply quantities and preferences when you have them. The assistant confirms your
exact store before products and asks about material package or substitution ambiguity.
Searches cover bounded returned pages; they do not establish storewide completeness.
Missing prices, currency, units or history remain gaps.

You can also ask: "What is cheap for breakfast this week?" or "Price-check
two of these and estimate the cost." Your assistant turns that request into
appropriate grocery searches, compares returned choices and explains its picks.
It asks only for material missing preferences or your exact store choice.

For saved observations, explicitly request stored deals or dated history. A stored
failure does not trigger a supplier refresh. Follow the full
[installation and use guide](skills/houston-i-love-kroger/references/user-guide.md)
for commands, expected results, permissions and recovery. The bundled
[API manual](skills/houston-i-love-kroger/research/official_docs/pages/API.md)
defines the supported service routes.

## Help and feedback

For connection failures, ask the service operator about the reported error.
For a missing local tool, restore the complete plugin or use a host that can run
its Python tools. Shopping stays in the conversation; the plugin never hands
you to the web app to finish the task. The tools follow no redirects, use no ambient
proxy or cookies, retry nothing automatically and save no shopping results.
Report only fixed status/error categories and the plugin version; keep raw source
rows, addresses, account data, tokens and private agreements out of public issues.

## Maintain or package a copy

From this folder, `python scripts/package_plugin.py --json` previews the fixed
allowlist without writing. To create a new ZIP in an existing output directory:

```text
python scripts/package_plugin.py --output houston-i-love-kroger-plugin.zip --json --no-input
python -B -m unittest discover -s tests
```

The builder refuses existing outputs and linked inputs. It includes only its
explicit public file list, with reproducible archive metadata. It does not package
the app checkout, a private API skill, local records, credentials, or caches.
Publication requires the project's exact-candidate licensing/legal review.
The repository's `.gitignore` is source-only and is not installed in the ZIP.
See [third-party notices](THIRD_PARTY_NOTICES.md) for the included-material scope;
the software license does not grant rights to supplier data or marks.

The installed documentation snapshot can be checked offline with:

```text
python skills/houston-i-love-kroger/scripts/refresh_docs.py --check --json --no-input
```

Only maintainers refreshing those manuals need an app source checkout. They must
explicitly pass `--repository PATH_TO_APP_CHECKOUT` with `--refresh`; ordinary
plugin use and offline snapshot checks have no checkout dependency. The snapshot
preserves original manual bytes for maintainers. Its web-app installation and
browser procedures are not companion shopping instructions.
