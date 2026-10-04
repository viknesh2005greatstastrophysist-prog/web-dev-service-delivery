# Web Dev Service Delivery

A kit for delivering client websites with an unattended AI coding agent. The agent picks an Awwwards
winner that suits the client, rebuilds its design system, layout, structure and motion as faithfully as
it can measure, swaps in the client's own content, audits the result against a production-grade
checklist, and hands over a package that a human deploys.

Status (2026-10-05): all 275 requirements are prioritized as Diamond, Gold, Silver or Bronze; release validation enforces the tier policy. A complete client delivery is still not verified end to end. See "Status and honest limits" below.

## What is in this repository

```
prompt/       The prompt you give the agent (one file, about 16,000 words)
checklist/    The production-grade checklist the prompt audits against (275 rows, 18 sections)
skills/       scroll-craft, the scroll and motion polish skill the prompt uses (MIT, Nate Herk)
vendor/       The upstream cloning methodology as a git submodule, pinned to the commit the prompt names
examples/     A starter CLIENT_INPUT folder to copy for each new client
scripts/      Document consistency and dependency-free release-evidence validation
tests/        Passing and adversarial fixtures for the release control
docs/         How to run it, decisions, legal notes, history, and every review and research note
archive/      Earlier editions of the prompt and checklist (superseded, kept for reference)
```

Start with the [tiered checklist](checklist/TIERS.md), then [HOW_TO_RUN](docs/HOW_TO_RUN.md). Read the [release evidence contract](docs/RELEASE_EVIDENCE.md) and [2026-10-02 audit](docs/reviews/production-audit-2026-10-02/AUDIT.md) before making a readiness claim.

## What a run does, end to end

1. **Choose a target.** An Awwwards Site of the Day, Site of the Month or Developer Award winner that fits the
   client's brief, outside the client's own industry and market, reachable without a login.
2. **Study it.** Every route in scope at four screen sizes plus 320 px: all states, the intro, hover and menus,
   motion recorded frame by frame, a baseline audit of the original (speed, accessibility, headers, its 404).
3. **Turn it into numbers.** Computed styles, spacing, type scale, easings and durations go into a locked
   assertion file whose hash is tracked, so a check can never be quietly loosened to pass.
4. **Rebuild it from scratch** with the agent's own code, matching the original's box tree and motion.
5. **Prove the match** against a private reference build that carries the original's own text and images, so any
   difference is a defect and not a content difference. A strict comparator, a per-frame motion gate, and a state
   walk of every menu and overlay run until they pass or the 10-cycle loop ends.
6. **Swap the content in.** The client's copy, photos and video where supplied; otherwise copy drafted from the
   brief, CC0 stock media, or marked placeholders. Testimonials, client names, statistics and awards are never
   drafted or stocked. A brand shift (derived or the client's palette and typefaces) is on by default.
7. **Production loop.** The agent audits against the checklist and fixes failures without breaking the match.
8. **Polish** the scroll feel with the scroll-craft skill, additively.
9. **Hand over** a git repository with docs, host configs for Netlify, Cloudflare Pages, Vercel and nginx, a CI
   workflow, draft legal pages, a `content:sync` script and an `audit:live` command a human runs after deploying.
10. **Report** 15 fidelity/workflow gates and a separate production evidence decision. Handover is not launch approval; required production defects cannot pass as inherited.

## What "clone" means here

It is a close reproduction of the original's design system, layout, structure and motion, measured and not
eyeballed, with the client's content in it. It is not inspiration and it is not a redesign. It is never a
literal pixel diff, and the prompt forbids calling the result pixel-identical.

What matches the original: colours, type scale, spacing, grid, radii, component states, layout at four sizes,
motion timing and trajectories.

What differs by design:
- all text, images, video, logo and brand names (the client's own);
- commercial fonts, replaced by the closest open-licensed face unless the client owns a licence;
- the brand shift (palette and typefaces), on by default;
- launch essentials the original lacks (legal links, consent banner, form messages, a credits page);
- invisible production fixes, and accessibility fixes in every deployed build.

Limits: shader output needs frame review; real devices and assistive technology need human evidence. Playwright can test Chromium, Firefox and WebKit when installed; WebKit emulation is not physical iOS Safari.

## Legal position in one paragraph

Replacing content does not establish permission to reproduce a reference design. Copyright, trade dress,
licences and hosting terms need assessment for the actual project; the kit cannot estimate the likelihood
of a claim or a takedown.
Read `docs/LEGAL_NOTES.md`. The prompt makes the reference design's rights an explicit launch step, and the
recommended answer is written permission from its creators or advice from a US IP attorney. This is not legal advice.

## Status and honest limits

- The prompt and checklist were reviewed by Opus six times (a full review of the clone-and-swap edition, a gold
  standard review, and short reviews of the run-parts section and the US legal edits). All were static reviews:
  files read, sources fetched, small scripts run. Reports are in `docs/reviews/`.
- v6 has not been run end to end. An earlier edition run by another flagship model produced a working site but
  260 geometry failures and several visible defects (invisible menu text, a collapsed backdrop). Each was turned
  into a rule or a gate, but only a real run will show what else is missing.
- The job is large (a 16,000-word prompt, a 21,000-word checklist). If a model runs out of context or hits usage
  limits, use `RUN_PART=1` then `RUN_PART=2` (see `docs/HOW_TO_RUN.md`).
- Strict speed budgets can be unreachable for a motion-heavy reference. Gold budget misses block Gold completion; Diamond failures block launch;
  a fidelity exception records the shortfall and does not waive the production requirement.
- Things only a person can do remain: deploying, DNS and accounts, legal review, a screen-reader pass, and the
  permission question on the reference design.

The [video lessons add-on](checklist/VIDEO_LESSONS_ADDON.md) maps the first nine Instagram sources into eight new requirements and existing checks. The [second-batch companion](checklist/VIDEO_LESSONS_BATCH2.md) integrates seven more sources and five further requirements. See the [dated review](docs/reviews/instagram-addon-2026-10-03/REVIEW.md) for accepted lessons, rejected claims and viewing limits.

## Editing the kit

1. Change the prompt and the checklist together; they cite each other by row ID and section number.
2. Keep existing row IDs stable. New rows take the next free number in their section; update `checklist/row-ids.txt`, the documented count and tests together. Never remove a row to hide a failure.
3. Run `python3 scripts/check-kit.py` and `python3 -m unittest discover -s tests -v`. Both must pass. The [CI template](docs/ci/README.md) runs these on pushes and pull requests once activated; activation currently needs GitHub workflow permission. Neither proves a client site is ready.
4. Update `checklist/tiers.json` and the Tier column together. Run `python3 scripts/render-tiers.py` to rebuild the tier view.
5. No em dashes or en dashes in the prompt or the checklist (the check enforces it).
6. Get an independent review for any change to a gate, a build rule or the legal wording. Earlier reviews caught
   real blockers that the author missed every time. `docs/reviews/` shows how they were run.
7. Record the change and the reason in `docs/HISTORY.md`.

## Third-party material and licences

- `skills/scroll-craft/` is MIT, copyright 2026 Nate Herk (`skills/scroll-craft/LICENSE`). Source:
  https://github.com/nateherkai/scroll-craft, packaged revision 0b816225945e45380397d6a0487efa3c98916858.
- `vendor/clone-app-pat-pro-public` is a git submodule of https://github.com/per-simmons/clone-app-pat-pro-public,
  pinned to commit 2c03e02d7e1849374739b576b9a0734e6d7e94ab. That repository has no licence file, so it is
  referenced and not copied into this one.
- This kit itself has no licence file yet. Until one is chosen it is for your team's internal use. Choose a
  licence before sharing it outside the team.
