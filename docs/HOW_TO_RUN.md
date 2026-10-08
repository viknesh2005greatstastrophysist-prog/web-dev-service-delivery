# How to run the kit

Start with [the short production standard](../checklist/RELEASE_STANDARD.md). The current risk-v2 policy separates Diamond release outcomes from Gold quality and optional implementation/reference work. Reuse evidence across overlapping rows; preserve the exact policy snapshot for historical records.


## 1. What you need

On the machine where the agent works:

- An AI coding agent with a shell and file access that can run for a long time: Claude Code or Codex.
- A currently supported Node.js LTS line compatible with the pinned tooling, npm and git; Python 3.9+ for kit validation.
- Google Chrome installed. The agent installs Playwright and Lighthouse itself during its preflight.
- A full ffmpeg build (the scroll-craft contact sheet and video checks need it).
- `curl`, `openssl` and `dig`. The preflight also checks `actionlint` and a licence checker.
- Network access to Awwwards, the chosen site, GitHub and npm. Stock images come from CC0 sources, and a
  provider API key (Pixabay or Pexels, read from the environment) is optional.
- A budget. The job is large: expect a long session and a lot of tokens. Plan for the two-part run below.

## 2. Get the kit

```bash
git clone --recurse-submodules <this repository's URL> web-dev-service-delivery
```

If you cloned without `--recurse-submodules`:

```bash
git -C web-dev-service-delivery submodule update --init
```

Check that the files still agree:

```bash
python3 web-dev-service-delivery/scripts/check-kit.py
```

## 3. Prepare a folder for one client

Work outside this repository. One folder per client:

```bash
mkdir acme-site && cd acme-site
```

```bash
cp -R ../web-dev-service-delivery/examples/CLIENT_INPUT ./CLIENT_INPUT
```

Fill in `CLIENT_INPUT` with what the client has (every file is optional; see `CLIENT_INPUT/README.md`).
Do not commit the real `CLIENT_INPUT` anywhere public: photos can carry location data.

The operator fills `CLIENT_INPUT/release-profile.md` from the actual scope and existing inputs.
Use the [daily checklist workflow](CHECKLIST_WORKFLOW.md): review applicability, prepare grouped
procedures, capture exact-release evidence and generate the queue from the full release record.
Missing fields stay unknown; they cannot justify N/A, approval or a release claim.

## 4. Start the agent

Open your agent in the `acme-site` folder and give it a run message like this one (single run):

```text
Read /path/to/web-dev-service-delivery/prompt/PROMPT_awwwards_clone_swap_v6.md and do exactly what it says.
KIT_DIR=/path/to/web-dev-service-delivery
CLIENT_INPUT=./CLIENT_INPUT
```

Optional lines you can add to the run message:

- `TARGET_URL=https://...` to pin the reference (it is still checked against the prompt's rules).
- A contact URL or address for Wikimedia (the stock step skips Wikimedia without one).
- `RUN_PART=1` or `RUN_PART=2` for the two-part run (below).

Give the agent permission to run shell commands without asking; the prompt tells it never to stop for approval.

## 5. The two-part run (recommended for most models)

The whole job is large. Splitting it keeps each session inside a model's context and usage limits.

Part 1, the clone and its proof (sections 1 to 5 of the prompt):

```text
Read /path/to/web-dev-service-delivery/prompt/PROMPT_awwwards_clone_swap_v6.md and do exactly what it says.
KIT_DIR=/path/to/web-dev-service-delivery
CLIENT_INPUT=./CLIENT_INPUT
RUN_PART=1
```

It ends by committing both repositories and writing `WS/handoff.md`, then sends a short report.

Part 2, the swap and the shipping (sections 6 to 8 and Finish), in a fresh session in the same folder:

```text
Read /path/to/web-dev-service-delivery/prompt/PROMPT_awwwards_clone_swap_v6.md and do exactly what it says.
KIT_DIR=/path/to/web-dev-service-delivery
CLIENT_INPUT=./CLIENT_INPUT
RUN_PART=2
```

Part 2 reads the handoff, re-verifies it, and finishes the job. Do not edit the work between the parts.
If you do, preserve those edits and continue in an isolated checkout of the recorded state. Never silently reset the operator's work.

## 6. What you get

Inside the folder you started in, named after the client's brand (`<name>`):

- `<name>/app/`: the handover package, a git repository tagged `v1.0.0`. It installs and runs with one command
  and holds `README.md`, `docs/` (deploy, DNS, launch checklist, content gaps and notes, fidelity exceptions,
  provenance, handover, editing guide, maintenance, acceptance, draft legal pages), host configs, a CI workflow,
  `npm run content:sync` and `npm run audit:live`.
- `<name>/clone-workspace/<name>/` (called `WS`): the private build record. It holds captures of the original
  (screenshots, markup, stylesheets, text, images), the gate outputs and the reference build. Keep it private. It is
  never handed to the client and never published.

The agent's final message gives the target and award, the content status (`CLIENT-COMPLETE` or `CONTENT-PENDING`),
the gate table (PASS, FAIL, NOT_RUN or INHERITED), the fidelity exceptions, known gaps, the run command and the
first three things a human must do to launch. If any required gate is not PASS, it says so first. The [release evidence contract](RELEASE_EVIDENCE.md) defines the separate handover, launch and gold decisions; a finished run alone does not authorize launch.

## 7. What a human does after the run

From `<name>/app/docs/LAUNCH_CHECKLIST.md`, which lists each step with a way to confirm it:

1. Settle the rights question on the reference design (written permission from its creators, or advice from a
   US IP attorney), and have counsel review the draft legal pages. Read `docs/LEGAL_NOTES.md` first.
2. Have the client approve every drafted and stock slot and the brand shift. Complete the LICENSE grantor placeholder.
3. Complete pre-launch owner checks on the final artifact: physical devices and screen readers, account ownership/security,
   monitoring and isolated restore evidence, the takedown response plan, and explicit cutover approval with rollback triggers.
4. Configure hosting and applicable provider accounts and environment variables. Set `SITE_ENV=production` only once
   the content status is `CLIENT-COMPLETE`. Confirm the immutable accessible artifact and handover evidence before cutover.
5. Follow the approved DNS/cutover plan, preserving existing business email records. Deploy the verified artifact, then run
   `npm run audit:live -- https://the-client-site`, confirm actual final-domain contact delivery where applicable, and fix or roll back failures.
6. Complete remaining live owner checks, record Search Console status and validate the launch evidence before declaring the launch verified.
   Assign named follow-up dates. The recommended 7-day and 30-day reviews remain pending until they actually occur.

## 8. When the client sends more content later

Add the files to `CLIENT_INPUT` (or edit `content/site.json`) and run `npm run content:sync`. It never drafts
copy or fetches stock; it only applies what the client supplied and re-runs the overflow and contrast checks.

## 9. Troubleshooting

- The agent stops partway with a usage limit: use the two-part run, and resume part 2 in a fresh session.
- The agent cannot reach the target site or is blocked: the prompt records the swap and picks another target.
- The methodology submodule is empty: run the `git submodule update --init` command above, or let the agent clone it.
- A gate shows FAIL: read `WS/escalation.md` (what is left) and the visual review file `WS/gates/visual-review.md`.
- Gold speed targets missed on a motion-heavy site: expected sometimes. They appear as fidelity exceptions or FAIL
  rows with the measured value. Required misses block readiness; recording an exception does not waive them.

## Validate the release evidence

Use [RELEASE_EVIDENCE.md](RELEASE_EVIDENCE.md) to create the per-release record from actual tests. Run handover validation before delivery, then launch validation after approved deployment and final-domain checks. All host builds use `build:deploy` with accessibility fixes enabled. Preserve the same tested artifact throughout. A machine-valid record still needs human inspection.


## Prioritize the work

Use [TIERS](../checklist/TIERS.md) to work through Diamond first, then Gold, Silver and Bronze. Every row still gets a disposition; optional work is tracked, not deleted. The full catalogue supplies exact criteria. A conditional feature absent from the actual system can be N/A with evidence. No lower tier target waives Diamond. Keep prelaunch, controlled-cutover and future checks separate. Old release records remain tied to their old checklist hash; a new policy is not retroactive evidence of a pass.

## Before scaling a clone

Use [CLONE_WORKFLOW](CLONE_WORKFLOW.md) for pinned desktop/mobile/state contracts, actual
model records, generated-media content sync and stale-evidence checks. These controls supplement
the fifteen full fidelity gates and never replace the Diamond release floor.
