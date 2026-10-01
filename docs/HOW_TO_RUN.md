# How to run the kit

## 1. What you need

On the machine where the agent works:

- An AI coding agent with a shell and file access that can run for a long time: Claude Code or Codex.
- Node.js 18 or newer (the scroll-craft minimum; use an LTS release), npm and git.
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
If you do, the edits are saved aside and the recorded state is restored.

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
first three things a human must do to launch. If any gate is not PASS, it says so first.

## 7. What a human does after the run

From `<name>/app/docs/LAUNCH_CHECKLIST.md`, which lists each step with a way to confirm it:

1. Settle the rights question on the reference design (written permission from its creators, or advice from a
   US IP attorney), and have counsel review the draft legal pages. Read `docs/LEGAL_NOTES.md` first.
2. Have the client approve every drafted and stock slot and the brand shift. Complete the LICENSE grantor placeholder.
3. Create hosting and email-provider accounts, set the environment variables, and set `SITE_ENV=production` only once
   the content status is `CLIENT-COMPLETE`.
4. Add the DNS records from `docs/DNS.md` and follow the cutover plan.
5. Run `npm run audit:live -- https://the-client-site` and fix what fails.
6. Do the owner-only steps: a real screen-reader pass, monitoring and backups, Search Console, the takedown
   response plan, and the 7-day and 30-day reviews.

## 8. When the client sends more content later

Add the files to `CLIENT_INPUT` (or edit `content/site.json`) and run `npm run content:sync`. It never drafts
copy or fetches stock; it only applies what the client supplied and re-runs the overflow and contrast checks.

## 9. Troubleshooting

- The agent stops partway with a usage limit: use the two-part run, and resume part 2 in a fresh session.
- The agent cannot reach the target site or is blocked: the prompt records the swap and picks another target.
- The methodology submodule is empty: run the `git submodule update --init` command above, or let the agent clone it.
- A gate shows FAIL: read `WS/escalation.md` (what is left) and the visual review file `WS/gates/visual-review.md`.
- Gold speed targets missed on a motion-heavy site: expected sometimes. They appear as fidelity exceptions or FAIL
  rows with the measured value. Do not loosen the checklist to make a run look better.
