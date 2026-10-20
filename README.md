# Houston I Love Kroger plugin

Help a person choose their Kroger store, find requested groceries, check returned
packages and prices, and estimate quantities through the app's API. Separate
commands read permission-approved stored deals and dated history. The plugin
does not call Kroger directly, collect history, or manage Cart or checkout.

This folder is the complete portable plugin. It includes its skill, Python tools,
manuals, schemas, synthetic tests and [MIT license](LICENSE). It has its own
[source repository](https://github.com/aipersonalized/houston-i-love-kroger-plugin),
separate from the app. You can extract its ZIP anywhere;
you do not need the app's source checkout, Node.js, a provider SDK, supplier keys,
or the privately maintained Kroger API technology skill.

## 1. Get the complete plugin

1. Click [Download plugin ZIP](https://github.com/aipersonalized/houston-i-love-kroger-plugin/releases/download/v0.1.0/houston-i-love-kroger-plugin.zip)
   and save `houston-i-love-kroger-plugin.zip`.
2. Extract all files. On Windows, right-click the ZIP and choose **Extract All**;
   on macOS, double-click it; on Linux, use your archive manager's extract action.
3. Open the resulting `houston-i-love-kroger-plugin` folder, which contains this README,
   and keep the complete folder together. Do not copy only `SKILL.md`: its scripts
   and manuals are required too. A checkout of the plugin's own repository can
   use its entire root folder instead.

You can [open the app](https://aipersonalized.io/apps/houston-i-love-kroger/)
to use it directly. The commands below use that existing app's API-version-1
address. Installation does not start or deploy an app. To use another compatible
installation, pass its complete address with `--base-url`, including its app path
and final slash; a localhost address works only for an app on your own computer.

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

## 3. Install Python and choose the app URL

1. Install [Python 3.12 or newer](https://www.python.org/downloads/) if needed.
   Open PowerShell on Windows or Terminal on macOS/Linux and run `python --version`.
   If your system uses `python3`, use that command throughout these instructions.
2. Open a terminal in this plugin folder. No Python packages need installation.
3. Use `https://aipersonalized.io/apps/houston-i-love-kroger/` for this project's
   app, or supply your own compatible app's address with `--base-url`.
   [connection.example.json](config/connection.example.json) is reference
   documentation for these values; the tools do not automatically load that file.
4. Read the [recipient and source permission guide](skills/houston-i-love-kroger/references/source-permissions.md)
   before sending catalog records to an assistant or external model. A flag or
   working API does not establish those rights. Keep agreements and credentials private.

## 4. Check the tools

From this plugin folder:

```text
python skills/houston-i-love-kroger/scripts/shopping.py --help
python skills/houston-i-love-kroger/scripts/promotions.py --help
python skills/houston-i-love-kroger/scripts/shopping.py products --store TEST0001 --term apples --summary-only --dry-run --json --no-input
```

The last command uses synthetic identifiers and makes no request. Expect a
preview with network and writes false. Check the existing app's status with:

```text
python skills/houston-i-love-kroger/scripts/shopping.py status --base-url https://aipersonalized.io/apps/houston-i-love-kroger/ --json --no-input
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

For saved observations, explicitly request stored deals or dated history. A stored
failure does not trigger a supplier refresh. Follow the full
[installation and use guide](skills/houston-i-love-kroger/references/user-guide.md)
for commands, expected results, permissions and recovery. The bundled
[API manual](skills/houston-i-love-kroger/research/official_docs/pages/API.md)
defines the supported app routes.

## Help and feedback

For connection failures, verify the complete app URL and ask its operator about
configuration or permissions. The tools follow no redirects, use no ambient
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
preserves original manual bytes; links to the upstream project's publisher/app
installation material remain optional online references.
