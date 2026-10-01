Go to Awwwards, pick a winning site you find genuinely impressive, and rebuild it pixel for pixel.

Context you should know: this is going into a video watched by a large audience, your clone is put on screen next to the original site against two other frontier models doing the same task, and your work will be credited to you by name. Every model gets this identical prompt. The comparison is literal — your build and the real site, side by side, at the same viewport.

**First, read the methodology.** Clone `https://github.com/per-simmons/clone-app-pat-pro-public` and read `SKILL.md` and [`references/00-contract.md`](https://github.com/per-simmons/clone-app-pat-pro-public/blob/master/references/00-contract.md) before you do anything else, then the stage references as you reach each stage. The contract defines the workspace layout, the artifact filenames, the stage inputs and outputs, the verification gate, and the convergence loop. Follow it. [`scripts/assert-styles.mjs`](https://github.com/per-simmons/clone-app-pat-pro-public/blob/master/scripts/assert-styles.mjs) is the gate.

Two overrides to what that repo says, and they win where they conflict:

- **Ignore the stop-and-check-in gate.** That repo was written for an interactive session with a human. You are running unattended. Do not stop between stages, do not ask for approval, do not ask questions. Run the whole pipeline start to finish and report only when it's done.
- **Use your own browser automation** — headless Playwright or Puppeteer, installed and driven by you — anywhere the repo says to use the Claude Chrome extension. The contract's real rule is unchanged and it is the one that matters: **computed styles read off the live page are the ground truth.** Read them through the CSSOM. Screenshots are a visual reference only; never build the gate on a pixel diff.

Requirements:

1. **Pick your own target on Awwwards** — Site of the Day, Site of the Month, or a Developer Award winner. Pick something you actually find impressive rather than something easy to match. It must be publicly reachable without a login or paywall. Record the exact URL, the award, and why you chose it in the project README. If a site turns out to be unclonable for a hard reason — it's down, it's gated, it's a video with no site behind it — pick another and note the swap.

2. **Recon every view before you write code.** Every route, every breakpoint, every interactive state — hover, focus, active, open menus, modals, scroll-triggered states, loading and transition states. The repo's `01-recon.md` covers this. What you miss in recon you will not build.

3. **Extract, don't guess.** Pull real computed values off the live page: the full type scale, the color palette with exact values, spacing, radii, shadows, borders, grid and container widths, breakpoints, easing curves and durations, font families and weights. `02-extraction.md` and `03-design-spec.md` are the shape of this. Never read a value off a screenshot.

4. **Rebuild it.** Every page, every component, every state, at every breakpoint. The motion is part of the clone — scroll behavior, page transitions, hover choreography, entrance animations, any WebGL or canvas work. A static skin over a site whose whole identity is motion is a failed clone.

5. **No lifted assets.** Do not hotlink from the original and do not download its images, video, or fonts. Regenerate imagery in code, substitute freely-licensed equivalents, or author placeholders that match the original's role, aspect, and color. Fonts come from an open CDN, matching the metrics as closely as you can. Say what you substituted in the README.

6. **Prove the match.** Run the verification gate: read the clone's computed styles, compare them to the extracted design tokens with [`scripts/assert-styles.mjs`](https://github.com/per-simmons/clone-app-pat-pro-public/blob/master/scripts/assert-styles.mjs), and iterate the convergence loop until there are zero style-assertion failures and the project builds clean. Then eyeball your clone against the real site at the same viewport, at every breakpoint, and fix what your eye catches that the assertions didn't.

7. **Ship it runnable.** A real project — a modern framework is fine — that installs and runs with a documented command, plus a README naming the target URL, the award it won, what you substituted, and your final assertion results.

8. **Depth over breadth if you have to choose.** One page cloned to a genuinely indistinguishable standard beats five pages that are approximately right.

9. **Final polish pass with the scroll-craft skill (additive only).** After requirement 6 passes, and before you write the final assertion results into the README, run the polish pass described under "Requirement 9 in detail" below. It enhances what requirements 1 to 8 built. It never removes, restyles or rebuilds any of it, and if nothing needs fixing it changes nothing.

**Requirement 9 in detail: the polish pass.**

The scroll-craft skill is at `/Users/vik/Downloads/scrollcraft (2)/scroll-craft` (call it `SKILL_SRC`). Use it only to find and fix roughness in scroll feel, motion and interaction. The repo's own Stage 9 polish (`07-polish.md`) still runs first and is unchanged. This pass comes after it, and may write under `clone-workspace/<name>/09-polish/scrollcraft/` even though `07-polish.md` says to write nothing else.

Read from the skill: `SKILL.md` (Bootstrap and Step 5 only), `references/verify.md`, the sections of `references/devices.md` for devices the page actually uses plus its cue contract (§2), `references/taste.md` (Motion, and States and content) and `references/approved-collection.md` §7. Skip everything else: SKILL.md Steps 0 to 4, uniqueness and fingerprints, `worldflight.md`, asset generation, `scrollcraft.css`, and any edit of `engine/scrollcraft.js`. Those exist for designing new pages. Here the original wins over the skill.

**Invariants.** These are checked and evidenced in the report, not promised.

1. Snapshot first. Before changing anything, copy the project source (without `node_modules` or build output) to `clone-workspace/<name>/09-polish/scrollcraft/baseline/`, and save baseline rest frames as PNGs at every breakpoint you recorded (reveals finished, pointer idle, fonts loaded).
2. The gate does not move. After the pass, the same unedited assertions give zero failures and the build is clean. Never add, delete, loosen or re-baseline an assertion. Every value the gate asserts, including CSS `transition-*` and `animation-*`, is off limits. A fix that moves one is reverted.
3. The rest state does not move. Re-shoot the baseline frames after the pass: zero differing pixels (mask video, canvas and WebGL regions identically in both captures), and document height and every section rect within 1px of baseline. This compares the clone with its own earlier frames, so it does not conflict with "never build the gate on a pixel diff".
4. Nothing is added or removed: sections, routes, pins, copy, images, video, nav, menus, footer. No asset generation.
5. If no fix is kept, the project is byte-identical to the baseline snapshot and only the report remains.

**Method.**

1. Set up outside the project. In `clone-workspace/<name>/09-polish/scrollcraft/` run `npm init -y && npm i playwright-core` (the harness resolves it from the working directory), and set `SCROLLCRAFT_HOME` to an absolute path inside that folder so nothing lands in your project. Run `node "<SKILL_SRC>/scripts/doctor.mjs"` from there and save the output. It needs installed Google Chrome (set `SCROLLCRAFT_CHROME` if it is not found) and a full ffmpeg build for the contact sheet. Fix any `required` failure. A missing KIE key is fine.
2. Instrument without touching the project. The harness only walks pages that carry its hooks. Copy `scripts/shoot.mjs` into the polish folder as `shoot-clone.mjs` (leave the skill's own copy alone) and add a `page.addInitScript` that stamps the following, using your clone's selectors from extraction:
   - `data-sc-act="flow"` on each section root; `pin`, `pan` or `scrub` instead on sections the original pins, pans or scrubs (`flow` sections get no dead-scroll check).
   - `data-sc-copy` on text over media.
   - `data-sc-verify-state` on fixed stages, canvases and WebGL layers, set to a rounded signature of what actually paints, never raw scroll progress; `data-sc-verify-hold="true"` only during a genuine resolved hold.
   - the class `sc-ready` on `<html>` once the intro has ended and fonts have loaded (the harness times out after 15 seconds without it).
3. Serve the production build, never `file://`, and confirm the port is yours before trusting a run: `curl -s <url> | grep -o "<title>.*</title>"`.
4. Baseline run, from the polish folder: `node shoot-clone.mjs --url <url> --out baseline/desktop`, then again with `--width 390 --height 844 --out baseline/mobile`, then with `--reduced-motion --out baseline/reduced`. Read every `sheet.png` and `report.json`.
5. The harness cannot judge smoothness. Scroll the clone cold once and note every stutter, lurch, pop-in, snap and place where scrolling fights the input. For each animated section, capture a strip of the clone and of the original at the same viewport and scroll offsets.
6. Write `findings.md`: every harness finding (dead scroll, cues that never peak, contrast failures, console errors, failed requests, broken images), every keyboard, reduced-motion and touch problem, and every smoothness defect. Class each one `defect` (the clone is broken or rougher than the original), `inherited` (the original shows the same defect at the same viewport and offset; keep both frames as evidence and leave it) or `not verifiable` (say why). Only defects are fixed.

**Allowed fixes.** Each must trace to a defect in `findings.md`.

- Scroll smoothing. If the original uses a smooth-scroll library, tune it. Otherwise add smoothing only if the clone's wheel or trackpad scrolling stutters. Touch keeps native momentum. Keyboard, space, Page Down, anchor links (offset under a fixed nav) and scroll restoration keep working. No snapping or scroll-jacking the original doesn't do. Plain native scroll under `prefers-reduced-motion`.
- Dead scroll: give the span something that resolves to the original's end state (a cue, light parallax, a reveal). Never change heights.
- JS-driven motion that stutters or snaps (lerp, tweens, drag inertia, cursor follow, page transitions): retune easing and timing, keeping start and end states. Copy reaches full opacity, holds long enough to read, and never re-hides on scroll-up.
- Reduced motion: fewer and gentler, not zero. Keep the opacity that carries meaning, drop position changes, keep all content reachable.
- Robustness: console errors, failed requests, broken images, focus landing on invisible controls, keyboard open and close of menus, and forms (no personal data in the URL, no false "sent" state).

Put new code in its own module (`src/polish/`), switchable with `?polish=off` read once at boot, so one build serves both the before and after captures. Edit an existing file only when a defect cannot be fixed additively, and log the file and the reason.

**Loop and report.** After each batch of fixes: rebuild, re-run the harness (desktop, mobile, reduced), re-run the gate, re-shoot the rest frames, and re-measure heights and rects. Revert any batch that regresses any of them. At most 3 cycles; whatever remains is listed as open. Target: zero dead scroll, zero cues that never peak, zero contrast failures, and zero console errors and failed requests, apart from `inherited` items. Write `clone-workspace/<name>/09-polish/scrollcraft/polish-report.md` with the findings table and classes, a change table (defect, change, before and after evidence), the gate numbers before and after, the rest-frame diff result, open items, and what a real phone could show that headless Chrome cannot (verify.md, "The phone is a different machine"). Add a short "Polish pass" section to the README with the same headline results. If nothing needed fixing, the report says "No change required" and lists the checks that were run.

Work completely autonomously. Do not ask for anything until it's finished.

DONE when: the clone passes the style-assertion gate with zero failures, runs from a documented command, reproduces the original's motion and interactive states, and holds up next to the real site at full screen.

Also required for DONE: the polish pass in requirement 9 is finished, its report is written, and the gate still shows zero failures after it.
