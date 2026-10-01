Go to Awwwards, pick a winning site you find genuinely impressive, and rebuild it pixel for pixel.

Context you should know: this is going into a video watched by a large audience. Your clone is put on screen next to the original site, against two other frontier models doing the same task, and your work will be credited to you by name. Every model gets this identical prompt. The comparison is literal: your build and the real site, side by side, at the same viewport, at full screen. The audience sees two things: paused frames (layout, type, colour, spacing, component states) and live scrolling and interaction (scroll feel, transitions, hover, entrances, canvas or WebGL work). Both count, and neither can be faked: your gate output is saved to disk and can be re-run.

**If time runs short, cut from the bottom of this list, never from the top:**
1. The first viewport at 1920×1080 and 1440×900: layout, type, colour, spacing, intro animation.
2. Every rest state of the landing route.
3. Motion and interactive states.
4. Tablet and mobile.
5. The polish pass.

Depth over breadth. One route cloned to a genuinely indistinguishable standard beats five routes that are approximately right.

## Ground rules

These win over everything below and over the methodology repo.

1. **Unattended.** Do not stop between stages, do not ask for approval, do not ask questions. Run start to finish and report only when it's done or when a terminal state (§5) stops you.
2. **Computed styles are the ground truth.** Read them off the live page with `getComputedStyle`. Never read a value off a screenshot. Screenshots are a visual reference only, and the original-versus-clone gate is never a pixel diff. (Diffing your own clone against its own earlier frames, to prove a later change moved nothing, is allowed.)
3. **Your own browser automation.** Headless Playwright or Puppeteer, installed and driven by you, replaces the Claude Chrome extension everywhere the methodology repo mentions it.
4. **No lifted assets.** Do not hotlink from the original, and do not ship or download its images, video, fonts or logo. Icons and logos count as images: redraw or substitute them. Regenerate imagery in code, use freely-licensed equivalents (record each licence), or author placeholders that match the original's role, aspect, average luminance and dominant hue for that slot, so the paused frame reads the same and text over it keeps its contrast. Fonts come from an open CDN. You may read the original's stylesheets and measure its images to take values from (colour, aspect, luminance): keep those evidence files in `WS/evidence` (see below), never reference or ship them. Write your own code from measured values: measured values are facts and stay identical, but do not ship the original's CSS, JS or markup. Checked at the end: no shipped file shares a SHA-256 with an evidence file, and nothing in the built output references the original's domain.
5. **Copy.** Keep the original's visible text, so layout and line breaks match. The README states that this is an unofficial rebuild made for a comparison exercise and is not affiliated with the original's owner.
6. **Honesty.** A gate is `PASS` only if its command output is saved under `WS/gates`. Never edit, delete, loosen or re-baseline an assertion to make it pass. Never call a frame pixel-identical while imagery or fonts are substituted; say what matches (layout, type metrics, colour, spacing, component states) and what is substituted. Report every gate that failed, was skipped or could not be measured. Verify everything yourself: re-run the gate, and never accept a delegated agent's report at face value.
7. **Servers.** Start dev and preview servers on fixed ports (`--strictPort`, `--host 127.0.0.1`), confirm the port is serving your build before trusting a capture (`curl -s <url> | grep -o "<title>.*</title>"`), and stop every server you started.

## Methodology

Clone `https://github.com/per-simmons/clone-app-pat-pro-public` and check out commit `2c03e02d7e1849374739b576b9a0734e6d7e94ab` (its head on 2026-09-30). Read that repo's `SKILL.md` and [`references/00-contract.md`](https://github.com/per-simmons/clone-app-pat-pro-public/blob/master/references/00-contract.md) before you do anything else, then each stage reference as you reach that stage (`01-recon.md` through `07-polish.md`). The contract defines the workspace layout, the artifact filenames, the stage inputs and outputs, the verification gate and the convergence loop. Follow it, with these exceptions, which win where they conflict:

- The stop-and-check-in gate is ignored (rule 1).
- Contract §3-F and §3-G tell you to download fonts and assets. Rule 4 replaces them.
- The Chrome extension is replaced by rule 3. The contract's "one Chrome, sequential browser stages" rule is lifted: Playwright contexts may run in parallel if each writes only its own files.
- The gate comparator is stricter than the contract's (see §5).
- `07-polish.md` still runs. One more pass follows it (§6). Where a stage reference disagrees with the contract, the contract wins (the contract says so itself). Known case: `07-polish.md` calls `assert-styles.mjs` with `--page`, `--url` and `--spec`, and reads a `diff/` folder; the script takes `--assertions`, `--clone-styles` and `--out`, and `metrics.json` sits in `06-qa/cycle-N` (contract §1 and §5).

Name the project folder after the target (call it `<name>`). Everything the methodology writes goes under `<name>/clone-workspace/<name>/`; call that `WS`. Put your own tools in `WS/tools` and gate outputs in `WS/gates`. Use the contract's viewport keys plus one: `desktop` 1920×1080, `laptop` 1440×900, `tablet` 768×1024, `mobile` 375×667, and name per-page artifacts `{page}--{viewport}`.

**Preflight, before stage 1.** Record in `WS/preflight.md`: Node, Python if you use it, ffmpeg, installed Google Chrome, and Playwright's own Chromium (`chromium.launch({ channel: 'chromium' })` must open a page; if it can't, install it and retest). Choose a dev port and a preview port and check both are free (`lsof -nP -iTCP:<port> -sTCP:LISTEN` prints nothing). If a required dependency can't be made available, report the blocker and what you completed. Never claim a gate you couldn't run.

## 1. Choose the target

Site of the Day, Site of the Month or a Developer Award winner on Awwwards. Open the candidate's own Awwwards page and record the award and its date from it, never from memory. Pick something you actually find impressive rather than something easy to match, and prefer a site whose identity includes real motion. It must be publicly reachable without a login or paywall, must load in headless Chromium, and must have a real site behind it, not just a video. If it fails any of that, pick another and record the swap.

Before recon, write `WS/SCOPE.md`: the exact URL, the award and date with a link to its Awwwards page, why you chose it, the routes in scope (default: the landing route only; add a deeper route only if the site's signature interaction lives there), and the states the comparison will show. "Every view" below means everything in `SCOPE.md`, and you claim nothing outside it.

## 2. Recon every view before you write code

Every route in scope, at all four viewports. Every interactive state: hover, focus, active, open menus, modals, scroll-triggered states, loading and intro sequences, page transitions, drag and gesture states. Also record:

- **Rest frames.** For every section and state, the scroll position and timestamp where it is resolved: fully in view, reveals finished, pointer idle. "At rest" everywhere below means these frames.
- **Motion baseline** (`motion-baseline.json`). For the intro, menu open and close, page transitions and scroll reveals: computed `transform` and `opacity` every ~80 ms, plus frames. For scroll-driven motion (parallax, pins, scrubs): the computed values at a fixed list of scroll offsets.
- **Canvas and WebGL surfaces.** Rect, what drives each one (time, scroll or pointer), how it behaves over time, and whether the surface is DOM or GPU-rendered.
- **Runtime-only behaviour.** Injected style tags, custom cursors that only appear after the first pointer move, consent banners (handle them the same way on both sites when capturing).
- `interaction-map.json` (contract §8) with an honest `unreached[]`, and `STATES-MANIFEST.md`.

Award sites are slow headless: use `waitUntil: 'load'`, 90 s timeouts, retries and 10 to 13 s settles. What you miss in recon you will not build.

## 3. Extract, specify, assert

Pull real computed values off the live page: computed-style archetypes per page × viewport, pseudo-elements, CSS variables, `@font-face` rules, the authored stylesheet rules (media queries, keyframes, easings), the full type scale, the colour palette with exact values, spacing, radii, shadows, borders, grid and container widths, measured breakpoints, and a fingerprint of the stack and scroll library. Measure motion numerically: durations, easings, staggers, distances, lerp and inertia constants, parallax factors, clamp bounds, the scroll library's settings. Never read a value off a screenshot.

Then write `DESIGN.md` (contract §4) and `assertions.json`: an array of `{selector, prop, expected, layer}`, one entry per viewport × state × selector × property.

- `selector` is `"<viewport>|<state>|<css selector>"`. `prop` is a kebab-case CSS longhand (`padding-left`, never `padding`).
- `layer: "rest"`: colour, background (gradients included), type metrics, padding, margin, radius, box-shadow, backdrop-filter, position, z-index, cursor, rects, and the final `transform` and `opacity` of each state.
- `layer: "motion"`: `transition-*`, `animation-*`, `scroll-behavior`.
- `layer: "substituted"`: values that differ by design: `font-family`, image URLs, and the glyph-run widths of text set in a substitute font. For text blocks, assert the line count at every viewport instead (`x-line-count` = block height ÷ line height), which is what makes "line breaks land in the same places" checkable. List every substituted value, with the original and clone values, in `WS/substitutions.json`.
- Coverage: your assertion builder prints `archetypes covered: X/Y` and `states covered: X/Y`. Both must be 100%.
- **Lock.** Write the SHA-256 of `assertions.json` to `WS/gates/assertions.lock`. Regenerate assertions only from a new measurement of the original, and log each change and its reason in `WS/assertion-changes.md`.

## 4. Rebuild it

Every page in scope, every component, every state, at every breakpoint, in a modern framework of your choice. The motion is part of the clone: rebuild the original's own scroll behaviour, page transitions, hover choreography, entrance animations and any WebGL or canvas work first, and only then anything else. For WebGL and canvas, author the effect yourself from what recon recorded. A static skin over a site whose whole identity is motion is a failed clone.

- **Fonts.** Choose the closest open font by measuring about 30 candidates against the live font (cap-height-normalised text width, x-height, uppercase width). Use `size-adjust` in `@font-face` where it improves the match. Record the numbers.
- **Imagery.** Write the shot list right after recon and build placeholders at every slot's aspect, so QA can run before the final images exist. Never upscale beyond a source's resolution, and never bake text into an image. Look at every generated image before using it.
- **Build discipline.** Never define components inside other components. Guard effects that run twice under React StrictMode in dev, and test `npm run dev` as well as the production build. A `position: fixed` element at `left: 50%` is capped at half the viewport: give a large centred title `width: max-content`. Write colour alpha as a decimal (`rgb(0 0 0 / 0.5)`), because a percentage can read back as 0.498.

## 5. Prove the match

**The comparator.** The contract names `assert-styles.mjs` as the gate, and you run it, but on its own it can pass a false match: it compares only the first number in any value that has units. Reproduced: a `padding` of `10px 60px` passes against an expected `10px 20px`, and a `box-shadow` with a different colour, offset and blur passes when its first number matches. So write `WS/tools/assert-strict.mjs`, which reads the same two JSON files plus each assertion's `layer` and compares token by token.

- Tolerances: `px` ±1, `em` and `rem` ±0.01, `%` ±0.5, opacity and colour alpha ±0.01. Colour channels, unitless numbers (`font-weight`, `z-index`), keywords and function names must match exactly, and a value with a different number of tokens fails. A selector or property missing from the clone's styles is a failure, never a skip. `substituted` entries are skipped and counted.
- Exit 0 only when `rest` and `motion` have zero failures.
- Smoke test before you use it, saved to `WS/gates/strict-smoke.txt`: the `padding` and `box-shadow` mismatches above must both fail (the upstream script passes them), and `400px` read as `400.9px` must pass.

Run both comparators and save both outputs. The strict one is the gate.

**Clone gate.** Drive each state exactly as a user would (move the pointer, hover, click, scroll in steps, wait for transitions to end), read `getComputedStyle` for every asserted key into `clone-styles.json`, and run the comparators. Iterate the convergence loop until there are zero `rest` and `motion` failures and `npm run build` exits 0.

**Target validation (required).** Run the same reader against the live original through a clone-selector to original-selector map, scored with the same assertions. Every mismatch means the spec recorded an authored value where the runtime computes something else (for example a JS-injected `cursor: none`, or an unscoped variable falling back to black). Correct the assertion to the runtime value (log it in `assertion-changes.md`), fix the clone to match, and re-run both. Final state: the clone has 0 failures and the original has 0 failures on the same `rest` and `motion` set. Record the URL, capture date, viewport, font-load state and interaction state with both runs. If the live site changes during your build, refresh the baseline and say so.

**Motion gate.** Replay each recorded motion sequence on the clone and sample every ~80 ms. For each property, normalise to the original's range: end values must match exactly, completion time must be within ±50 ms, and the deviation at matched timestamps must be at most 0.08 of the range. For scroll-driven motion, computed values at the same scroll offsets must meet the rest tolerances. Anything you cannot measure numerically (shader output, for example) goes in a list of unmeasured items with a frame-strip comparison instead.

**Convergence loop** (contract §6). At most 10 cycles. Two consecutive cycles with no drop in failures, from cycle 2, end the run as `STUCK`. Reaching the cap is `CEILING`. A blocked target or a build that won't compile is `HARD-BLOCKER`. On any of these, write `WS/escalation.md` and say plainly what failed. Never present it as passing.

**Eyeball pass** (after the gate is green). Side-by-sides, original next to clone, at the recorded rest frames at all four viewports and every key state, plus frame strips of the intro, transitions and scroll reveals. Fix what the assertions cannot see: clipping, stacking, remounts, timing, line breaks. A long capture batch can catch a crossfade mid-transition, so re-shoot before you "fix". Save the clone's rest frames as PNGs in `WS/09-polish/rest` (reveals finished, pointer idle at (0, 0), `document.fonts.ready` resolved); §6 diffs against them.

## 6. Final polish pass with the scroll-craft skill (additive only)

Run this after §5 passes and before you write the final results into the README. It enhances what §1 to §5 built. It never removes, restyles or rebuilds any of it, and if nothing needs fixing it changes nothing.

The skill is at `/Users/vik/Downloads/scrollcraft (2)/scroll-craft` (call it `SKILL_SRC`). Use it only to find and fix roughness in scroll feel, motion and interaction. The repo's own Stage 9 polish (`07-polish.md`) still runs first, unchanged. This pass comes after it, and may write under `WS/09-polish/scrollcraft` (call it `POLISH`) even though `07-polish.md` says to write nothing else.

Read from the skill: its `SKILL.md` (Bootstrap and Step 5 only), `verify.md`, the sections of `devices.md` for devices the page actually uses plus its cue contract (§2), `taste.md` (Motion, and States and content) and `approved-collection.md` §7. The references are in the `references` folder of `SKILL_SRC` and the scripts in its `scripts` folder. Skip everything else: SKILL.md Steps 0 to 4, uniqueness and fingerprints, `worldflight.md`, asset generation, `scrollcraft.css`, and any edit of `scrollcraft.js`. Those exist for designing new pages. Here the original wins over the skill.

**Invariants** (checked and evidenced in the report, not promised):
1. Snapshot first. Before changing anything, copy the project source (without `node_modules` or build output) to `POLISH/baseline` and confirm the rest PNGs from §5 exist.
2. The gate does not move. After the pass, the same unedited assertions (the lock hash still matches) give zero `rest` and `motion` failures, the motion gate still passes with deviations no larger than before, and the build is clean. Everything the gate asserts, including CSS `transition-*` and `animation-*`, is off limits. A fix that moves one is reverted.
3. The rest state does not move. Re-shoot the rest frames after the pass: zero differing pixels (mask video, canvas and WebGL regions identically in both captures), and document height and every section rect within 1px of baseline. This compares the clone with its own earlier frames, so it does not conflict with ground rule 2.
4. Nothing is added or removed: sections, routes, pins, copy, images, video, nav, menus, footer. No asset generation.
5. If no fix is kept, the project is byte-identical to the baseline snapshot and only the report remains.

**Method.**
1. Set up outside the project. In `POLISH` run `npm init -y && npm i playwright-core` (the harness resolves it from the working directory), and set `SCROLLCRAFT_HOME` to an absolute path inside `POLISH` so nothing lands in your project. Run `doctor.mjs` (in the `scripts` folder of `SKILL_SRC`) from `POLISH` and save the output. It needs installed Google Chrome (set `SCROLLCRAFT_CHROME` if it isn't found) and a full ffmpeg build for the contact sheet. Fix any `required` failure. A missing KIE key is fine.
2. Instrument without touching the project. The harness only walks pages that carry its hooks. Copy `shoot.mjs` into `POLISH` as `shoot-clone.mjs` (leave the skill's own copy alone) and add a `page.addInitScript` that stamps the following, using your clone's selectors from extraction:
   - `data-sc-act="flow"` on each section root; `pin`, `pan` or `scrub` instead on sections the original pins, pans or scrubs (`flow` sections get no dead-scroll check).
   - `data-sc-copy` on text over media.
   - `data-sc-verify-state` on fixed stages, canvases and WebGL layers, set to a rounded signature of what actually paints, never raw scroll progress; `data-sc-verify-hold="true"` only during a genuine resolved hold.
   - the class `sc-ready` on `<html>` once the intro has ended and fonts have loaded (the harness times out after 15 seconds without it).
3. Serve the production build, never `file://`, and confirm the port is yours (ground rule 7).
4. Baseline run, from `POLISH`: `node shoot-clone.mjs --url <url> --out baseline/desktop`, then again with `--width 390 --height 844 --out baseline/mobile`, then with `--reduced-motion --out baseline/reduced`. Read every `sheet.png` and `report.json`.
5. The harness cannot judge smoothness. Scroll the clone cold once and note every stutter, lurch, pop-in, snap and place where scrolling fights the input. For each animated section, capture a strip of the clone and of the original at the same viewport and scroll offsets.
6. Write `findings.md`: every harness finding (dead scroll, cues that never peak, contrast failures, console errors, failed requests, broken images), every keyboard, reduced-motion and touch problem, and every smoothness defect. Class each one `defect` (the clone is broken or rougher than the original), `inherited` (the original shows the same defect at the same viewport and offset; keep both frames as evidence and leave it) or `not verifiable` (say why). Only defects are fixed.

**Allowed fixes.** Each must trace to a defect in `findings.md`.
- Scroll smoothing. If the original uses a smooth-scroll library, tune it. Otherwise add smoothing only if the clone's wheel or trackpad scrolling stutters. Touch keeps native momentum. Keyboard, space, Page Down, anchor links (offset under a fixed nav) and scroll restoration keep working. No snapping or scroll-jacking the original doesn't do. Plain native scroll under `prefers-reduced-motion`.
- Dead scroll: give the span something that resolves to the original's end state (a cue, light parallax, a reveal). Never change heights.
- JS-driven motion that stutters or snaps (lerp, tweens, drag inertia, cursor follow, page transitions): retune easing and timing, keeping start and end states. Copy reaches full opacity, holds long enough to read, and never re-hides on scroll-up.
- Reduced motion: fewer and gentler, not zero. Keep the opacity that carries meaning, drop position changes, keep all content reachable.
- Robustness: console errors, failed requests, broken images, focus landing on invisible controls, keyboard open and close of menus, and forms (no personal data in the URL, no false "sent" state).

Put new code in its own module (`src/polish`), switchable with `?polish=off` read once at boot, so one build serves both the before and after captures. Edit an existing file only when a defect cannot be fixed additively, and log the file and the reason.

**Loop and report.** After each batch of fixes: rebuild, re-run the harness (desktop, mobile, reduced), re-run the gates, re-shoot the rest frames, and re-measure heights and rects. Revert any batch that regresses any of them. At most 3 cycles; whatever remains is listed as open. Target: zero dead scroll, zero cues that never peak, zero contrast failures, and zero console errors and failed requests, apart from `inherited` items. Write `POLISH/polish-report.md` with the findings table and classes, a change table (defect, change, before and after evidence), the gate numbers before and after, the rest-frame diff result, open items, and what a real phone could show that headless Chrome cannot (`verify.md`, "The phone is a different machine"). If nothing needed fixing, the report says "No change required" and lists the checks that were run.

## 7. Ship it runnable

A real project that installs and runs with one documented command (for example `npm install && npm run dev`). Its README names:
- the target URL, the award and its date (linked to the Awwwards page), why you chose it, the routes in scope, and the unofficial-rebuild statement from rule 5;
- what you substituted, as a table (fonts with the measured numbers, every image and how it was made, logos and icons, licences);
- the gate table below with each gate's status and output path, and the final assertion results, taken from the run made after the polish pass;
- a short "Polish pass" section with the headline results from `polish-report.md`;
- known gaps, including everything unmeasured and what a real phone might show that headless Chrome cannot.

## Finish

Each gate is `PASS`, `FAIL`, `NOT_RUN` or `INHERITED` (an item the original shows identically, with evidence), with the path of its saved output.

1. Strict comparator on the clone, polish on: 0 failures on `rest` and `motion`. Upstream `assert-styles.mjs` output saved beside it.
2. The same assertions on the live original: 0 failures.
3. `assertions.lock` matches the last hash in `assertion-changes.md`.
4. Motion gate passes, or the unmeasured items are listed with frame strips.
5. `npm run build` exits 0. `npm run dev` answers `GET /` with 200 within 30 seconds, and a headless load of `/` records 0 console errors and 0 failed requests.
6. No shipped file shares a SHA-256 with an evidence file, and the built output never references the original's domain.
7. Polish pass: rest frames identical (0 differing pixels), document height and section rects within 1px, `polish-report.md` written.
8. Every `interaction-map.json` entry is rebuilt and behaves in the clone, or is listed in `unreached[]` and the README.
9. The README is complete and matches the saved outputs.

DONE when all nine are `PASS` or honestly listed, the clone runs from the documented command, reproduces the original's motion and interactive states, and holds up next to the real site at full screen. Your final message gives: the target and award (linked), the gate table, what you substituted, the known gaps, and the run command. If any gate is not `PASS`, say so first.

Work completely autonomously. Do not ask for anything until it's finished.
