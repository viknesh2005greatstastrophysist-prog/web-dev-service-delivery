# Master prompt: Awwwards pixel rebuilds + scroll-craft dynamics layer (3 templates, any niche)

Use this file with a coding agent that has a shell, Node 20+, Python 3 with Pillow, a full ffmpeg build and installed Google Chrome. A local Codex CLI is optional (§4 has a fallback chain). Fill in §0.1 before starting. Validate the parameters in this order:

1. `NICHE` blank: ask for it once and stop. Do not invent the business category.
2. `SLUG` blank: derive it from `NICHE`. It must match `^[a-z0-9_]+$`.
3. `CUSTOMER` blank: write it in Stage 0.
4. `DEV_PORT` blank: use the first base in 5173, 5183, 5193, … whose six ports (dev `base` to `base+2`, preview `base-1000` to `base-998`) are all free. A port is free when `lsof -nP -iTCP:<port> -sTCP:LISTEN` prints nothing. `DEV_PORT` given and any of its six ports busy: report the busy ports and stop. Never kill a process you did not start.

The pipeline has two layers, and they never mix:

1. **The rebuild.** A pixel-for-pixel layout, type, colour and spacing rebuild of an award-winning Awwwards site, reskinned for an original fictional business. This layer is judged by computed styles and side-by-sides against the live original. Nothing in layer 2 is allowed to move a single rest-state pixel.
2. **The dynamics layer (scroll-craft).** A final add-on pass that smooths the scroll and refines the motion using the scroll-craft skill: scroll feel, easing, cue timing, dead-scroll removal, parallax depth, pointer response, reduced motion and touch. It changes *how the page gets from one frame to the next*, never *what the frames are*.

**Precedence when instructions conflict:** this file, then the upstream methodology contract (`00-contract.md`), then the scroll-craft docs. Inside this file, §2d (overrides) and §3 (originality) win over everything else.

---

## 0. Mission

### 0.1 Parameters (fill these in)

| Parameter | Value | Notes |
|---|---|---|
| `NICHE` | `<e.g. dental clinics>` | The business category, in plain words |
| `SLUG` | `<e.g. dental>` | Must match `^[a-z0-9_]+$`; used in folder names |
| `CUSTOMER` | `<optional, e.g. families choosing a local dentist>` | Who hires this business. If blank, the agent writes it in Stage 0 |
| `DEV_PORT` | `<e.g. 5173>` | Template N uses `DEV_PORT + N - 1` for dev and `DEV_PORT - 1000 + N - 1` for preview. Pick a base no other running template uses |
| `SKILL_SRC` | `/Users/vik/Downloads/scrollcraft (2)/scroll-craft` | Where the scroll-craft skill folder lives |

### 0.1b Conventions (used everywhere below)

| Term | Meaning |
|---|---|
| `WORKROOT` | The directory that contains `outputs/`. Every relative path in this file is relative to it unless a step names another working directory. |
| `<project>` | A template folder: `outputs/awwwards_clone_<SLUG>`, `..._2` or `..._3`. |
| `<name>` | The template folder's basename. Its methodology workspace is `<project>/clone-workspace/<name>/`. |
| Viewport keys | `desktop` 1920×1080, `laptop` 1440×900, `tablet` 768×1024, `mobile` 375×667 (the contract's three plus `laptop`). Per-page artifacts are named `{page}--{viewport}`. |
| Working directory | `workspace.mjs` finds `.scrollcraft.json` only by walking **up** from the working directory. Run `doctor.mjs` and `workspace.mjs` from inside `outputs/`, and `shoot.mjs` from `<project>/site`. Run from `WORKROOT`, they silently resolve a different workspace. |
| Gate status | `PASS`, `FAIL`, `NOT_RUN` or `INHERITED`. A gate is `PASS` only if its command output is saved at `<project>/clone-workspace/<name>/gates/gate-<N>.txt`. |

### 0.2 Preflight and source control

Before Stage 0, from `outputs/`, check each item below and record the result in `outputs/METHOD_VERSIONS.md`. Keep these versions fixed through the comparison.

- `SKILL_SRC` holds `SKILL.md`, `engine/scrollcraft.js` and `scripts/doctor.mjs`. Record the scroll-craft release (the first `## ` heading of its `CHANGELOG.md`; the copy shipped with this file is release 0.3.0, packaged revision `0b816225945e45380397d6a0487efa3c98916858`).
- Methodology repo: clone `https://github.com/per-simmons/clone-app-pat-pro-public` and check out `2c03e02d7e1849374739b576b9a0734e6d7e94ab` (its HEAD on 2026-09-30). Use a different revision only if the user names one, and record it.
- Versions of Node, Python and Pillow, ffmpeg, Google Chrome and playwright-core.
- Playwright's own Chromium: `chromium.launch({ channel: 'chromium' })` must open a page. If it cannot, run `npx playwright-core install chromium` and retest. Installed Google Chrome (needed by `shoot.mjs` for h264) is a separate check.
- Codex: look for `codex` with `command -v codex`, then at `/Applications/ChatGPT.app/Contents/Resources/codex`. Record found or not found; not found is not a blocker.
- The shared helpers and per-template tools are not part of either download. Create each from its contract in Appendix B and run its smoke test before any gate relies on it.

If a required dependency cannot be made available, report the blocker and the completed artifacts instead of claiming a passed gate.

### 0.3 The job

For `NICHE`, build **three distinct website templates**. Each one rebuilds a **different** award-winning Awwwards site for an **original fictional business** in that niche.

- **At rest, match the original's measured structure and styling** at the same viewport: geometry, spacing, type scale, colour tokens, image-slot placement, breakpoints and component states. Original photography, copy, logos and proprietary fonts are deliberately replaced, so the full rendered frames cannot be pixel-identical. Report structural/style fidelity and content substitutions separately. "At rest" means each section in its resolved frame (fully in view, reveals finished, pointer idle) and each interactive state after its transition has ended.
- **In motion, the rebuild is allowed to be better.** Once the rest-state gate is green, the scroll-craft dynamics layer makes scrolling smoother and the transitions between rest states richer and calmer. Every change it makes must land on exactly the original's end state.
- Brand, copy, logo, imagery and code are all your own.

This work goes into a public video comparison against other models, credited by name. Compare the build and live source at the same viewport and full-screen scale. In paused frames, grade layout, typography metrics, colour, spacing and component states; visibly label the original content substitutions. In motion, grade scroll feel and transitions separately. Do not call the overall frame pixel-identical when imagery, copy or fonts differ.

After the required inputs are set, run autonomously across stages. Ask no routine check-in questions. If a template ends in an upstream terminal state other than `CONVERGED-PASS` (`STUCK`, `HARD-BLOCKER` or `CEILING`, contract §6), write `escalation.md` in its workspace, carry on with the other templates, and finish with a report that states exactly which templates and gates passed, failed or were not tested. Never present partial work as three verified templates.

---

## 1. The three templates

The three must be **distinct from each other**: different target sites, brands, names, palettes, logos, copy, fictional projects or clients, photo sets (no image reused across templates) and signature interactions.

| # | Folder | Ports (dev / preview) | Target | Fictional brand |
|---|---|---|---|---|
| 1 | `outputs/awwwards_clone_<SLUG>` | `DEV_PORT` / `DEV_PORT-1000` | chosen in Stage 0 | chosen in Stage 0 |
| 2 | `outputs/awwwards_clone_<SLUG>_2` | `DEV_PORT+1` / `DEV_PORT-999` | chosen in Stage 0 | chosen in Stage 0 |
| 3 | `outputs/awwwards_clone_<SLUG>_3` | `DEV_PORT+2` / `DEV_PORT-998` | chosen in Stage 0 | chosen in Stage 0 |

### Stage 0: choosing the targets

1. **Define the customer.** Write `CUSTOMER` (if blank) and a short adjacency list in `outputs/TARGETS.md`: the 4–6 categories that the same customer plausibly shops in when hiring this niche, ranked by closeness, each with one line on why. For example, a house painter's customer also hires tilers, builders and interior finishers; an accountant's also hires wealth managers, business advisers and law firms.
2. **Search Awwwards for winners only**: Site of the Day, Site of the Month, Site of the Year, Honorable Mention or Developer Award. Nominees don't count. Open each candidate's Awwwards page and record the award and date from it; never cite an award from memory. Search the exact niche first, then walk down the adjacency list.
3. **Qualify each candidate.** It must be a real business in the niche or an adjacent category, public, with no login or paywall, and genuinely impressive rather than easy to match. State why it transfers to `NICHE`.
4. **The three targets must differ on at least 4 of scroll-craft's 6 fingerprint dimensions** (grammar, nav treatment, hero device, act-sequence shape, close pattern, signature move), checked pairwise. Classify each target's structure against `scroll-craft/references/uniqueness.md` §2 before committing. If two targets collide, swap one. The registry (`outputs/scrollcraft-workspace/FINGERPRINTS.md`) may already hold rows from earlier runs. Never edit or delete a row. This run's gate is pairwise among its own three rows. If a target also shares 3 or more dimensions with an older row, note it in `TARGETS.md` as information, not a failure.
5. If a target turns out to be unclonable for a hard reason (down, gated, a video with no site behind it), pick another and record the swap.
6. Define the comparison scope before extraction: name the exact public route or routes and states the video will show. Start with one landing route per target; add a deeper route only when its signature interaction or the comparison requires it. Put the route and state inventory in `outputs/TARGETS.md`. Do not claim coverage of routes outside that inventory.

For each chosen target, record in `outputs/TARGETS.md`: exact URL, award with link to its Awwwards page, niche match, why chosen, the scroll-craft grammar it maps to, its signature interaction, and the fictional brand.

**Fictional brands.** Invent names that don't belong to a real business in the niche or its adjacent categories (search the name before using it). Where the original has a giant wordmark or title, match its letter count and silhouette so it fills the same width. The brand's services should be the niche's real services, so the copy reads as a credible business of that kind.

**Niche rules.** Write `outputs/NICHE-RULES.md` before any copy exists. List the claims that are regulated, risky or misleading in this niche and ban them in all three templates. Typical families to check:
- outcome and performance promises (health results, financial returns, legal wins, savings, rankings)
- guarantees (price, timeline, refund, "100% satisfaction")
- credentials (real licences, regulator or association logos, certification marks, awards the fiction didn't win)
- safety, medical, legal or financial advice presented as real guidance
- anything that impersonates a real brand, person or place of business

End `NICHE-RULES.md` with a fenced block tagged `banned`: one case-insensitive regular expression per line, covering every banned claim above. Gate 8 greps the built output with it.

---

## 2. Methodology (read first, follow it)

### 2a. The rebuild methodology

Clone `https://github.com/per-simmons/clone-app-pat-pro-public` into each template folder as `methodology/` at the preflight-recorded commit. Read `SKILL.md` and `references/00-contract.md` before doing anything else, then each stage reference as you reach it (`01-recon.md` … `07-polish.md`). The upstream workflow assumes a Chrome extension and copied source assets; the Playwright and original-asset restrictions in §2d require local adapter code. Build and smoke-test those adapters before recon and QA.

The contract defines the workspace layout (`clone-workspace/<name>/00-config.json`, `01-recon/`, `02-extraction/`, `03-design-spec/`, `04-architecture/`, `06-qa/cycle-N/`, `09-polish/`), artifact filenames, stage inputs and outputs, the verification gate and the convergence loop. `methodology/scripts/assert-styles.mjs` is the upstream comparator. This file's gate uses the stricter `outputs/assert-strict.mjs` (§6 step 5, §7, Appendix B) because the upstream script cannot see most compound-value mismatches.

### 2b. The scroll-craft skill (dynamics layer only)

Copy the skill folder from `SKILL_SRC` to `outputs/scroll-craft/`, intact. Write `outputs/.scrollcraft.json`:

```json
{ "workspace": "scrollcraft-workspace" }
```

so all three templates share one workspace (`outputs/scrollcraft-workspace/`) and one fingerprint registry. Then run, once:

```bash
cd outputs
node scroll-craft/scripts/doctor.mjs
node scroll-craft/scripts/workspace.mjs --ensure
```

`workspace.mjs` must print `<WORKROOT>/outputs/scrollcraft-workspace` and report that it resolved via `outputs/.scrollcraft.json`; any other path fails this step. Record the doctor output in `outputs/scrollcraft-workspace/doctor.txt`. A missing `KIE_AI_API_KEY` is fine (see §4). Any `required` failure must be fixed, not worked around. The `verify` checks (playwright-core, Chrome) must pass before step 9: playwright-core resolves from the working directory, so re-run `doctor.mjs` from `<project>/site` after `npm i -D playwright-core` and save it as `<project>/clone-workspace/<name>/doctor-site.txt`.

Read `scroll-craft/SKILL.md`, then these references **as they apply to motion**: `devices.md`, `feel.md`, `taste.md` (the Motion, Text over media and States sections), `hero-depth.md` (the choreography and mobile sections), `verify.md` and `approved-collection.md` §7.

### 2c. What scroll-craft is and is not used for here

scroll-craft is written for building original pages. Here it is **only the motion and scroll-feel layer on top of a pixel-exact rebuild**. So:

| scroll-craft governs | the rebuild governs (scroll-craft is ignored) |
|---|---|
| Scroll feel: smoothing, lerp, wheel and touch behaviour | Layout, grid, section order, section heights, document height |
| Easing curves, durations and stagger of transitions **between** rest states | Every rest-state computed value: colour, type, spacing, radius, shadow, position, z-index |
| Cue timing: when copy enters, that it reaches full opacity and holds | Which copy blocks exist and where they sit |
| Dead-scroll removal within a section's existing height | Adding or removing sections, pins or scroll length |
| Parallax depth, drift, reveal wipes, kinetic type, pointer tilt/magnet (in-between frames only) | The target's own signature interaction (rebuild it faithfully first; the layer may only smooth it) |
| Reduced-motion and touch behaviour | Nav model, menus, footers, closes, cursors (including a custom cursor if the original has one) |
| The feeling curve and one engineered peak, expressed through motion intensity | Grammar, page structure, fingerprint (these are the target's, not chosen) |
| Content rules for **authored** copy and imagery (see §3) | |

Skip, explicitly, because they would redesign the page: SKILL.md Steps 0–2 as design decisions (grammar choice, journey, signature-move invention, act planning), the taste floor for spacing, type and colour, the refuse list for structure and surfaces, `worldflight.md`, adding scrub video where the original has none, and the scroll-craft CSS engine file. When the original does something the refuse list forbids (custom cursor, eyebrows, glass nav, section numbers), **the original wins**. Log each conflict in `clone-workspace/<name>/09-polish/scrollcraft-conflicts.md`.

### 2d. Overrides (these win wherever they conflict with either repo)

1. **No stop-and-check-in gate.** Run the whole pipeline end to end. Under scroll-craft's rules this counts as explicit creative delegation: write briefs marked `Self-authored under explicit creative delegation`.
2. **Browsers.** Recon, extraction and the style gate use Playwright Chromium (`chromium.launch({ channel: 'chromium' })`), never the Chrome extension. **Computed styles read through `getComputedStyle` are the ground truth.** Screenshots are a visual reference only. Never build the original-versus-clone style gate on a pixel diff. (Pixel diffs of the clone against its own earlier frames are how step 10 and gate 5 prove the dynamics layer moved nothing.) The scroll-craft harness (`shoot.mjs`) uses installed Google Chrome (it needs the h264 decoder); set `SCROLLCRAFT_CHROME` if doctor can't find it.
3. **No lifted assets.** Never hotlink or ship the original's images, video, fonts or logo. This overrides contract §3-F/G. You *may* download the original's stylesheets, and the images that §4's tone-match measures, into `02-extraction/evidence/` **to read values from** (rules, luminance, hue, aspect). Evidence files are never referenced by `site/`, never copied into it and never committed. Gate 4 checks that no file under `site/public/` or `site/dist/` shares a SHA-256 with an evidence file.
4. **The scroll-craft engine is never edited** (its own rule) and is never allowed to change layout. See §6 step 9 for how it is used.

---

## 3. Content and originality policy (strict)

- Recreate the **design system, layout, spacing, type scale, colour tokens, breakpoints and component states** from measured values.
- **Brand, logo, every word of copy, project and client names, testimonials, client logos and imagery must be original.** Don't reproduce or closely paraphrase the original's text, and don't translate it if it's in another language: write fresh copy in English. Match its length and role so the layout reads the same and line breaks land in the same places at every breakpoint. People, addresses and contact details are fictional (use `.example` email domains, `555` phone numbers).
- **Copy rules** (scroll-craft's content refuse list, plus `NICHE-RULES.md`):
  - No em dashes anywhere visible. Use a period, comma, colon or parentheses.
  - No filler verbs: elevate, seamless, unleash, next-gen, revolutionize, supercharge.
  - Nothing banned in `NICHE-RULES.md`. Where the original has a stat slot, fill it with a structural fact of the fiction (year founded, locations, team size, projects completed), never an outcome or performance promise.
  - No text baked into generated images; no fake dashboards, screens, documents or packaging with legible content.
- **Write all CSS and JS from scratch.** Use your own class-name vocabulary (a brand prefix, or your own BEM), your own custom-property names, your own rule structure and declaration grouping. Measured values are facts and stay identical; the code expressing them is yours.
- **Originality check:** `python3 outputs/check-css-overlap.py <project> --list` must report `flagged: 0`. It flags `identical`, `same-body`, `same-set` (4+ equal declarations in any order) and `target-var` (a custom-property name the original defines). Renaming selectors on identical blocks is **not** a fix: re-author the rule (token-driven custom properties, composition, logical properties and shorthands, dropped redundant declarations), then re-run the style gate to prove no computed value moved. This checker is a heuristic for obvious CSS overlap, not proof of overall code or design originality; review shipped code and assets separately.
- **Fonts:** pick the closest open font from Google Fonts or jsDelivr/Fontsource by **measuring** it against the live font: cap-height-normalised text width, x-height and uppercase width across about 30 candidates (`tools/fontmatch.mjs`). Alias the winner in `@font-face` with `size-adjust` when that improves the cap-height match. Record the numbers.

---

## 4. Imagery (Codex first, then fallbacks)

Use **Codex** (`codex exec`, found in preflight) with its built-in image tool when it's available, and the fallback chain in step 2 when it isn't. No stock downloads, none of the original's photography.

1. **Write the shot list right after recon, before the build:** `<project>/assets-src/shotlist.json`

   ```json
   { "style": "Editorial photograph …, natural light, 35mm, muted colour grade. No text, no logos, no watermarks, no legible screens or documents.",
     "images": [ { "file": "hero.png", "aspect": "16:9", "role": "hero", "prompt": "… subject centred, generous margins …" } ] }
   ```

   - The `style` string is scroll-craft's **style preamble**: written once, reused verbatim in every prompt of that template, never paraphrased. That is what makes the set read as one shoot. Each template gets its own preamble, tuned to its target's photographic tone.
   - Prompts describe **original** editorial photographs of this niche's real work: the spaces, the people at work (no logos), the finished result, materials and details.
   - Each photo plays the **same role, aspect, tone, luminance and palette** as the original's image in that slot, so the rest-state frame matches and the text over it keeps the same contrast. Never depict the original's actual photos.
   - Cover every slot the build uses, with framing guidance so the crop survives.
   - If the dynamics layer will parallax a hero into planes (§6 step 9), also list the extra plates hero-depth.md calls for (clean plate plus subject on a flat keyable backdrop) and note which slot they composite back into. The composite at scroll 0 must equal the single-image rest frame.
2. **Generate, walking this fallback chain.** Before generating, check which generators this machine actually has and write the result to `assets-src/generator.json`. Use the first one that works; when one hits a usage limit mid-set, carry on with the next for the remaining files only (every runner skips files that already exist).
   1. **Codex:** `node outputs/gen-codex.mjs <project> --parallel 3`, if the Codex binary exists and a test call succeeds. It batches 3 images per run, skips existing files and stops cleanly on a usage limit. Codex renders only 1536×1024, 1024×1536 or 1024×1024 PNGs into `assets-src/images/`.
   2. **Gemini "Nano Banana":** `node outputs/gen-nanobanana.mjs <project>`, if `GEMINI_API_KEY` is in the env or `outputs/.env` (set by the user).
   3. **kie.ai stills:** `node outputs/scroll-craft/scripts/kie.mjs still "<style preamble>\n\n<prompt>" assets-src/images/<file> --ar <aspect>`, if `KIE_AI_API_KEY` is set and `kie.mjs probe` shows a balance. Log the spend.
   4. **No external generator: code-authored imagery.** Claude has no built-in image generation, so with none of the above it makes each image in code: `assets-src/draw/<name>.html` (SVG, canvas or CSS) rendered to PNG with Playwright at the slot's aspect, or `assets-src/draw/<name>.py` drawn with Pillow. Use the `canvas-design` or `algorithmic-art` skills if they're installed. These are not fake photos. They are abstract or architectural compositions (paint-like fields, material textures, light-and-shadow planes, line drawings of spaces, tonal gradients with grain) that match each slot's **aspect, average luminance, dominant hues and focal position** as measured from the original's image in that slot. That keeps the rest-state frame's tone and the contrast of text over it the same. The files go to the same `assets-src/images/<file>` paths, so `process.py` and the build need no changes. Record the measured luminance and hue for each slot against the original in `assets-src/tone-match.json`.

   Whatever produced each image, say so per file in the README substitutions table. If any template ships code-authored imagery, list it as a known gap: its side-by-sides will match in layout and tone but not in photographic content.
3. **Look at every generated image before using it** (scroll-craft rule). Reroll anything with warped hands, legible fake text, logos or the wrong luminance for its slot.
4. **`assets-src/make-placeholders.mjs`:** a gradient placeholder for every slot at the right aspect, with the final web filenames (`<name>.jpg` + `<name>-sm.jpg`), so build and QA can run before the images exist.
5. **`assets-src/process.py`:** centre-crops each PNG to its slot aspect (per-slot anchor override allowed), writes `site/public/images/<name>.jpg` (long edge `min(2400, source long edge)`, never upscaled; q84) and `<name>-sm.jpg` (half size).
6. **Video only where the original scrubs or plays video.** If the original has a scroll-scrubbed hero or image sequence and `KIE_AI_API_KEY` is set, animate a Codex still with `node outputs/scroll-craft/scripts/kie.mjs shot …`, then encode with `bash outputs/scroll-craft/scripts/encode.sh` (desktop and `mobile` variants) so it scrubs rather than stutters. Cap it at 4 clips per template and log the spend. Without a key, use an image sequence or the still, and document it. Never add video where the original has none.
7. If generation is capped mid-set, reduce scope honestly (fewer projects, opposite-orientation crops of generated frames for variety) and document it.

---

## 5. Stack

- Vite + React 18 + TypeScript + GSAP (+ Lenis when the original uses smooth scroll, or when the dynamics layer adds it per §6 step 9), in `<project>/site`.
- `npm i -D playwright-core` in `<project>/site` (the scroll-craft harness resolves it from the cwd).
- `npm run dev` / `npm run preview` on the template's ports, with `--host 127.0.0.1 --strictPort` so a busy port fails loudly instead of silently moving to the next one.
- Start servers as background processes and **stop every server you started** when you're done.

---

## 6. Pipeline for each template

Steps 1–8 build and prove the pixel-exact rebuild. Step 9 is the scroll-craft layer. Step 10 proves the layer didn't break step 8.

1. **Recon** (`01-recon/`)
   - Every route you'll build, at 1920×1080, 1440×900, 768×1024 and 375×667.
   - Every interactive state: hover, focus, active, open menus, overlays and modals, scroll-triggered states, loading and intro sequences, page transitions, drag or gesture states.
   - **Timed frame sequences** for motion: computed transform and opacity every ~80ms, plus JPEG frames, for the intro, menu open/close, page transitions and scroll reveals. These are the original's motion baseline (`01-recon/motion-baseline.json`); the dynamics layer is measured against them.
   - Also record the **rest frame** of every section and state: the scroll position and timestamp where it is resolved. These define "at rest" for the gate.
   - Targets can be slow headless: `waitUntil: 'load'`, 90s timeout, retries, 10–13s settles.
   - Write `sitemap.json`, `recon.json` (themes, measured breakpoints, framework fingerprint, scroll library if any), `interaction-map.json` (contract §8 schema, with an honest `unreached[]`) and `STATES-MANIFEST.md`.
2. **Extraction** (`02-extraction/`)
   - Fetch and pretty-print every stylesheet on every route (strip hashed module suffixes) to read authored rules, media queries, keyframes and easings.
   - Dump computed-style archetypes per page × viewport, deduped by signature, including pseudo-elements.
   - Pull CSS variables, `@font-face` rules and rects, and fingerprint the stack.
   - Measure motion **numerically**: durations, easings, stagger, distances, lerp and inertia time constants, parallax factors, clamp bounds, and the scroll library's settings.
3. **Design spec** (`03-design-spec/`)
   - `DESIGN.md` in contract §4 structure: visual theme → colours → typography → spacing → radii → shadows and effects → motion → states → breakpoints → assets → theme tokens → design guardrails → agent prompt guide, with evidence for each value.
   - `build-assertions.mjs` emits `assertions.json`: an array of `{ "selector", "prop", "expected", "layer" }`, one entry per viewport, state, selector and property. `selector` is `"<viewport>|<state>|<clone selector>"`. `prop` is a kebab-case CSS longhand (`padding-left`, not `padding`; `border-top-left-radius`, not `border-radius`). Tag every entry with a `layer`:
     - `"rest"`: colour, background, font size, weight, line height, letter spacing, padding, margin, radius, backdrop filter, position, z-index, cursor, rects, and the **final** transform and opacity of each state. These must pass within the tolerances in §7.
     - `"motion"`: `transition-*`, `animation-*`, scroll-behavior and in-flight values. These match the original through step 8, then may change in step 9 only as recorded in `DYNAMICS.md`.
     - `"substituted"`: values that differ from the original by design: `font-family`, `background-image: url(...)`, `content` text, and glyph-run widths of text whose copy or font was replaced. They are never compared against the original. List each in `03-design-spec/substitutions.json` (original value, clone value, reason) and copy the list into the README table. For text blocks, assert the **line count** at every viewport instead (derived prop `x-line-count` = block height ÷ line height); that is what makes "line breaks land in the same places" checkable.
   - Coverage: `build-assertions.mjs` prints `archetypes covered: X/Y` and `states covered: X/Y`, measured against `{page}.computed.json` and `STATES-MANIFEST.md`. Both must be 100%. Expect hundreds to a few thousand assertions; under about 300 usually means missing states.
4. **Architecture** (`04-architecture/file-tree.md`, `component-map.md`), then **build** in `site/`. Rebuild the target's own motion faithfully first. Don't pre-empt step 9.
5. **QA and convergence** (`06-qa/cycle-N/`)
   - `tools/read-styles.mjs` opens the site, **drives each state exactly as a user would** (moves the pointer, hovers, clicks, scrolls in steps, waits for transitions to end) and reads `getComputedStyle` for every asserted selector → `clone-styles.json`.
   - `node outputs/assert-strict.mjs --assertions … --clone-styles … --out metrics.json`. Do not use upstream `assert-styles.mjs` as the gate. It compares only the first number in a value that has units, so a `padding` of `10px 60px` passes against an expected `10px 20px`, and a `box-shadow` with a different colour, offset and blur passes if its first number matches (reproduced 2026-09-30). It also has no notion of layers. Still run it and save its output next to the strict result. Never edit it.
   - Fix and loop until **0 failures on the `rest` and `motion` layers and `npm run build` exits 0**. Upstream contract §6 governs the loop: at most 10 cycles; no drop in failures for two consecutive cycles from cycle 2 ends the template `STUCK`; reaching the cap ends it `CEILING`.
6. **Target validation (required)**
   - Run the same reader against the live original through a selector map (clone selector → original selector), scored with the **same** assertions, into `06-qa/target-validation/`.
   - Every mismatch means the spec recorded an authored value where the runtime computes something else (for example a JS-injected `* { cursor: none !important }`, or an unscoped variable falling back to black). Correct the assertion to the runtime value, change the clone to match, re-run both.
   - **Final state: the clone has 0 failures AND the original has 0 failures on the same `rest` and `motion` assertion set** (`substituted` entries are excluded from both runs). Record source URL, capture date, viewport, font-load state and interaction state with both runs. If the live original changes during the build, refresh the baseline and report the change; a stale capture cannot validate the current target.
7. **Originality gate:** `check-css-overlap.py` reports `flagged: 0` (§3), and no shipped file shares a SHA-256 with an evidence file (§2d.3). Re-run the clone gate after any re-author.
8. **Eyeball pass (rest states)**
   - Side-by-sides (original | clone) at every breakpoint and every key state, **with the final approved imagery** (generated photos or documented code-authored substitutes), taken at the recorded rest frames. Plus frame strips of the intro, transitions and scroll reveals.
   - Fix what the assertions can't see: clipping, stacking, remounts, timing, line breaks. Save to `09-polish/rest/`. The rest frames are PNGs at the four recon viewports with reveals finished, the pointer idle at (0, 0) and `document.fonts.ready` resolved, so that step 10 can pixel-diff them.
   - Tag the passing commit or copy `site/` to `09-polish/rest-baseline/` so step 10 has something to diff against.
9. **Dynamics layer (scroll-craft, final add-on)**

   Write `clone-workspace/<name>/09-polish/DYNAMICS.md` first, then implement. It contains:
   - **The motion brief**, marked `Self-authored under explicit creative delegation`: the feeling curve read off the original (one line per section: the emotion, then what on screen causes it), and **the one peak** (feel.md §1–2). The layer uses motion intensity to sharpen that curve: quieter before the peak, the most generous motion at the peak, a close that resolves and holds.
   - **A change table:** every motion change, with the section, the original's measured value from `motion-baseline.json`, the new value, and the scroll-craft rule behind it.

   What the layer may do, all within each section's existing height:
   - **Scroll feel.** If the original uses smooth scroll, keep its library and tune it; if it uses native scroll, add Lenis only if it makes wheel and trackpad scrolling calmer without lag. Either way: native momentum on touch (no `syncTouch` hijack), keyboard, Page Down, space and anchor links still work, anchors offset under a fixed nav, scroll restoration on back, and plain native scroll under `prefers-reduced-motion`. Never scroll-jack (no snapping the reader to sections unless the original snaps).
   - **Dead-scroll removal.** Where `shoot.mjs` reports dead scroll, give that span something to do: a cue, a light parallax, a ground drift toward the next section's colour, or a reveal. Never fix it by changing height.
   - **The cue contract** (devices.md §2): every piece of copy reaches full opacity, holds long enough to read, and never re-hides on scroll-up.
   - **Easing and timing** (taste.md §Motion): `transform`, `opacity` and `clip-path` only; never `transition: all`; ease-out curves such as `cubic-bezier(0.23, 1, 0.32, 1)` in place of weak built-ins or `ease-in` on UI; UI transitions under 300ms (hover 120–180ms); entrances from `scale(0.95)` never `scale(0)`; group staggers 30–80ms; press feedback on pressables; hover motion gated to `(hover: hover) and (pointer: fine)`.
   - **Depth.** Small parallax rates on hero planes and image cards (hero-depth.md choreography), lerped playheads for any scrubbed media (devices.md "The playhead is lerped"), pointer tilt or magnet on cards and CTAs. At scroll 0, pointer idle, every plane sits exactly on the original composition.
   - **Reduced motion:** fewer and gentler, not zero. Keep the opacity that carries comprehension, drop position changes.
   - **Smoothing the signature interaction** (drag inertia, cursor lerp, page-transition easing) only where the original's version stutters or snaps, and only if its start and end states are unchanged.

   What the layer may **not** do: change any `layer: "rest"` value, change a section's height or the document height by more than 1px, add or remove sections, pins, video or copy, alter the nav, menus or footer at rest, or load `scrollcraft.css` (it sets global `box-sizing`, `scroll-behavior` and `body` rules that would move rest values).

   **Implementation.** Write the layer in the site's own GSAP/TS code, following the device specs in `devices.md`. You may mount the untouched engine (`ScrollCraft.mount(root)`) for devices it does better (scrubbed media, cue windows, drift), but it has no `destroy()`, so mount it once on a root that persists across route changes and call `layout()` after each transition, rather than mounting per route. Keep the layer in its own folder (`site/src/dynamics/`) and switch it off at runtime with `?dynamics=off` (read once at boot, no rebuild), so one preview server serves both the on and off captures in step 10. Document the flag in the README.

   **Harness hooks** so `shoot.mjs` can walk the page (data attributes only; no computed value changes):
   - `data-sc-act="flow"` on each section root, or `pin` / `pan` / `scrub` where the original already pins, pans or scrubs.
   - `data-sc-copy` on each copy block over media, so contrast is measured per line on the composited frame.
   - `data-sc-verify-state` on fixed stages the engine doesn't drive (sticky galleries, canvases, drag boards), publishing a rounded signature of what actually paints (verify.md), never raw progress. `data-sc-verify-hold="true"` only during a genuine resolved hold.
   - Add `sc-ready` to `<html>` once the intro has finished and fonts are loaded (the harness waits up to 15s for it).

   **Verify the layer** against `vite preview`, never `file://`:

   ```bash
   cd <project>/site
   node ../../scroll-craft/scripts/shoot.mjs --url http://127.0.0.1:<preview port> --out ../clone-workspace/<name>/09-polish/lab/desktop
   node ../../scroll-craft/scripts/shoot.mjs --url http://127.0.0.1:<preview port> --out ../clone-workspace/<name>/09-polish/lab/mobile --width 390 --height 844
   node ../../scroll-craft/scripts/shoot.mjs --url http://127.0.0.1:<preview port> --out ../clone-workspace/<name>/09-polish/lab/reduced --reduced-motion
   ```

   Target: **0 dead scroll, 0 cues that never reach full opacity, 0 contrast failures.** A finding that the original also shows at the same scroll position (proven with the recon frame pair) and that the layer can't fix without moving a rest pixel is `inherited`: list it with the evidence, don't fake it green. Then read every `sheet.png`, do the feel check (feel.md §6: scroll cold, one word per section, diff against the brief's curve), and run the approved-collection §7 checks: console errors, failed requests, broken images, keyboard menu open and close, focus order, and forms (a contact, booking or quote form must never GET personal input into the URL and must never show a false "sent" state).

   Record frame strips of original vs clone for the intro, page transitions, three scroll reveals and the peak, at 1440×900 and 375×667, in `09-polish/dynamics/`.

10. **Re-prove the rest state.** With the dynamics layer on:
    - Re-run step 5 and step 6. **Both still 0 failures on every `layer: "rest"` assertion.** `layer: "motion"` diffs must each match a row in the DYNAMICS.md change table, and nothing else may differ.
    - Re-shoot the clone at the same rest frames with the layer on and pixel-diff against `09-polish/rest/`: **0 differing pixels**. Mask video, canvas and grain regions identically in both captures and list the masks in `DYNAMICS.md`. Any other difference fails: find the cause, do not raise a threshold.
    - Measure document height and every section rect with the layer on and off; any difference over 1px fails.
    - Re-run `check-css-overlap.py`.
    - Append the template's row to `outputs/scrollcraft-workspace/FINGERPRINTS.md` (its dimensions are the target's), and confirm the three rows differ pairwise on at least 4 of 6.
11. **Docs**
    - `clone-workspace/<name>/status.json`, `progress.md`, `final-report.md`.
    - `<project>/README.md`: target URL, award (linked to its Awwwards page), niche match and why it was chosen; how to run it; what was built; a substitutions table (fonts, images, brand, copy, code); the cycle table; the target-validation result; the originality checker line; the dynamics layer summary (the feeling curve, the peak, the change table, harness results for desktop, mobile and reduced motion, the toggle flag); scroll-craft conflicts; and an honest list of known gaps, including what a real phone might show that headless Chrome can't (verify.md "The phone is a different machine").

---

## 7. The gate (all conditions must hold)

**Comparison rules** (implemented by `assert-strict.mjs`, the only gate comparator): values are compared token by token. Lengths in `px` ±1, `em` and `rem` ±0.01, `%` ±0.5, opacity and colour alpha ±0.01. Colour channels, unitless numbers (`font-weight`, `z-index`, unitless `line-height`), keywords, function names and the token count must match exactly. A value with a different number of tokens than expected fails. `substituted` entries are skipped and counted. Record each gate in `status.json` as `PASS`, `FAIL`, `NOT_RUN` or `INHERITED`, with the path of its saved output (§0.1b); a gate with no saved output is `NOT_RUN`.

1. `assert-strict.mjs` on the clone **with the dynamics layer on**: 0 failed on `rest`, and every `motion` diff accounted for in DYNAMICS.md.
2. The same assertions on the live original: 0 failed.
3. `npm run build` exits 0. `npm run dev` answers `GET /` with 200 within 30 seconds, and a Playwright load of `/` (React StrictMode on) records 0 console errors and 0 failed requests.
4. `check-css-overlap.py`: flagged 0, and no shipped file shares a SHA-256 with an evidence file.
5. Clone rest frames with the layer on match `09-polish/rest/` with 0 differing pixels (masks listed in `DYNAMICS.md`), and document height and every section rect stay within 1px of the layer-off values. This before/after check says nothing about clone-versus-original content pixels, which differ by design.
6. `shoot.mjs` on desktop, mobile and reduced motion: 0 dead scroll, 0 never-full-opacity cues, 0 contrast failures, except `inherited` findings listed with evidence.
7. Feel check done and written into DYNAMICS.md; approved-collection §7 functional checks pass.
8. No copy breaks `NICHE-RULES.md` or the §3 copy rules. Grep `dist/` (HTML, JS and CSS, including the `&mdash;` entity and the `\u2014` escape) and the source copy for U+2014, the §3 banned words (case-insensitive, any inflection) and every regex in the `banned` block of `NICHE-RULES.md`: 0 matches.
9. The three FINGERPRINTS rows differ pairwise on at least 4 of 6 dimensions.
10. Every `interaction-map.json` entry is rebuilt and behaves in the clone, or is listed honestly in `unreached[]` and the README.

---

## 8. Lessons learned (avoid these bugs)

**From the rebuilds**
- **Never define React components inside other components.** A parent re-render remounts every child and orphans imperative or rAF refs (the canvas stopped panning). Memoize page components, and wrap callbacks passed from `App` in `useCallback`.
- **StrictMode runs effects twice in dev.** Guard timelines started from async callbacks with a `cancelled` flag, because a killed GSAP timeline can still be `play()`-ed. Wrap `gsap.from()` in `gsap.context(...)` with `ctx.revert()` on cleanup. Always check `npm run dev`, not only the production build.
- **A `position: fixed` element at `left: 50%` is capped to half the viewport.** If a big centred title clips, give it `width: max-content`.
- **Probe runtime-only behaviour on the target:** injected style tags, custom-cursor elements that only appear after the first pointer move, and idle, hover-link, hover-media, pressed and drag states.
- **Colour serialisation:** `rgb(0 0 0 / 50%)` can read back as alpha 0.498. Write alpha as a decimal (`/ 0.5`).
- **Brand words drive layout.** When a giant wordmark or title dominates, choose an original word with a similar length and silhouette, and measure its width against the original's.
- **Screenshot timing can lie.** A long capture batch can catch a crossfade mid-transition. Re-shoot before "fixing".
- **Verify everything yourself.** Re-score every agent's `clone-styles.json` and `target-styles.json` with the gate script, check which folder the latest run actually wrote to, and run the originality checker. Don't accept a report at face value.

**From scroll-craft**
- **The harness photographs whatever answers on the port.** Confirm the preview server is this template's build before trusting a sheet (verify.md "The harness will photograph the wrong site").
- **Bundled Chromium has no h264.** Scrub clips silently fall back to posters and the run "passes". `shoot.mjs` needs installed Chrome.
- **`playwright-core` resolves from the cwd.** Run `shoot.mjs` from `site/`, where it's installed.
- **A missing `sc-ready` class times the harness out.** Add it after the intro and fonts, not on mount.
- **Publishing raw progress in `data-sc-verify-state` hides real dead scroll.** Publish rounded rendered values.
- **Lenis and `scrollTo`:** the harness jumps with `behavior: "instant"`. Confirm frames actually moved; if Lenis fights the jump, have the dynamics layer listen for native scroll and sync, rather than disabling Lenis for the harness.
- **Parallax that is right mid-scroll can be wrong at rest.** Anchor every rate so the offset is zero at the section's rest frame, not at the top of the document.
- **Disable pointer lock and capture in every automated context**; synthetic pointer input must stay virtual.
- **A green harness is not a real phone.** Say so in the report, and ship `scroll-craft/references/device-diag.html` next to the build if a phone defect is ever reported.

---

## 9. Orchestration (three templates at once)

- The orchestrator runs Stage 0 (customer, adjacency list, target selection, the pairwise fingerprint check and `NICHE-RULES.md`) for all three before any build starts.
- Template 1 can be built directly by the orchestrator. If the active runtime permits delegated agents, templates 2 and 3 may run in parallel, one per folder with separate ports, each given this file plus its row from `outputs/TARGETS.md` and `outputs/NICHE-RULES.md`. Otherwise build them sequentially. The verification and reporting gates are the same either way.
- The orchestrator owns image generation (it checks which generators exist once, walks the §4 fallback chain as soon as each `shotlist.json` appears, then tells the agent to run `process.py`), any KIE spend, the shared FINGERPRINTS registry, the independent verification in §8, and the final summary.
- Agents must not start step 9 until their own steps 5–8 are green, and must not touch another template's folder or port.
- If an agent stops (a rate limit, for example), inspect its folder state and resume it from where it stopped with explicit remaining tasks.

---

## 10. Final report format

For each template:
- the target and award
- the brand
- the pages built
- the image count and which generator made them (Codex / Gemini / kie.ai / code-authored), plus any clips, with spend
- the clone and original gate numbers, rest and motion
- the checker line
- gates 1 to 10, each as `PASS`, `FAIL`, `NOT_RUN` or `INHERITED`, with the path of its saved output
- the dynamics layer: peak, change count, harness results (desktop / mobile / reduced), feel-check diff
- the dev command and URL
- known gaps, including every failed or untested gate and the visible differences caused by original content substitutions

Close with a one-table summary of all three.

---

### Appendix A: tools used

**Shared, in `outputs/`:**
- `gen-codex.mjs`: Codex image runner
- `gen-nanobanana.mjs`: Gemini fallback
- `check-css-overlap.py`: originality gate
- `assert-strict.mjs`: the gate comparator
- `TEMPLATE_BRIEF.md`: the per-agent brief
- `TARGETS.md`, `NICHE-RULES.md`: Stage 0 output
- `scroll-craft/`: the skill (`scripts/doctor.mjs`, `workspace.mjs`, `shoot.mjs`, `kie.mjs`, `encode.sh`; `engine/scrollcraft.js`; references)
- `scrollcraft-workspace/`: shared workspace and `FINGERPRINTS.md`

**Per template, in `<project>/tools/`:**
- `recon-shoot.mjs`, `probe.mjs`, `intro.mjs`: recon (named to avoid confusion with the scroll-craft harness `shoot.mjs`)
- `build-assertions.mjs`: writes `assertions.json` and `substitutions.json`
- `extract.mjs`: computed archetypes
- `fontmatch.mjs`: font metrics
- `read-styles.mjs`: the QA reader, with clone and target modes
- `cshoot.mjs`: clone frames

**Per template, in `<project>/assets-src/`:**
- `shotlist.json`
- `generator.json`: which generator was available and used, per file
- `make-placeholders.mjs`
- `process.py`
- `draw/` + `tone-match.json`: only when falling back to code-authored imagery

**Per template, in `clone-workspace/<name>/09-polish/`:**
- `DYNAMICS.md`, `scrollcraft-conflicts.md`, `rest/`, `rest-baseline/`, `dynamics/`, `lab/{desktop,mobile,reduced}/`

---

### Appendix B: tool contracts

None of these ship with scroll-craft or the methodology repo. Write each to its contract, run its smoke test, save the output to `outputs/tool-smoke/<tool>.txt`, and only then use it as a gate. Tools without an entry here (`recon-shoot.mjs`, `probe.mjs`, `intro.mjs`, `extract.mjs`, `cshoot.mjs`, `make-placeholders.mjs`, `process.py`) have no separate contract: they write the files named in §4 and §6.

- **`outputs/assert-strict.mjs`**
  - Command: `node outputs/assert-strict.mjs --assertions <a.json> --clone-styles <c.json> --out <metrics.json> [--layer <rest, motion or all>]`
  - Reads: `a.json`, an array of `{selector, prop, expected, layer}`; `c.json`, `{ "<selector>": { "<prop>": "<computed value>" } }`.
  - Writes: merges `style_assertions` into `metrics.json` with `total`, `passed`, `failed`, `skipped_substituted`, `failures[]` and the same counts per layer. Prints one summary line per layer.
  - Exit: 0 when the selected layers have 0 failures (default `rest` and `motion`); 1 on failures; 2 on unreadable input. A selector or prop missing from `c.json` is a failure, never a skip.
  - Smoke test: a fixture where `padding` is expected as `10px 20px 10px 20px` and read as `10px 60px 10px 60px`, and `box-shadow` differs in colour, offset and blur, must report at least 2 failures (upstream `assert-styles.mjs` reports 0 on the same fixture). A `width` of `400px` read as `400.9px` must pass.
- **`<project>/tools/build-assertions.mjs`**
  - Reads `02-extraction/fragments/*`, `STATES-MANIFEST.md` and the clone-to-original selector map.
  - Writes `03-design-spec/assertions.json` and `03-design-spec/substitutions.json`; prints `archetypes covered: X/Y` and `states covered: X/Y`. Exit 1 if either is below 100%.
- **`<project>/tools/read-styles.mjs`**
  - Command: `node tools/read-styles.mjs --mode <clone or target> --url <base url> --assertions <a.json> [--selector-map <map.json>] --out <styles.json>`
  - Drives each state exactly as a user would, then reads `getComputedStyle` (plus derived `x-line-count`) for every asserted key. Writes `{ "<selector key>": { "<prop>": "<value>" } }`. In `target` mode it maps clone selectors to original selectors first.
  - Exit 1 if any asserted key could not be read.
- **`outputs/check-css-overlap.py`**
  - Command: `python3 outputs/check-css-overlap.py <project> [--list]`
  - Compares the authored CSS (`<project>/site/src/**/*.css` and `<project>/site/dist/assets/*.css`) against the original's evidence in `02-extraction/evidence/` and `all-styles.json`.
  - Flag kinds: `identical` (same selector and same declaration block after whitespace and case normalisation); `same-body` (same declaration block under a different selector); `same-set` (4 or more equal declarations in any order); `target-var` (a custom-property name the original defines).
  - Prints one line per flag (`<kind> <file>:<selector>`), and a last line `flagged: N`. Exit 0 only when N is 0.
  - Smoke test: a scratch stylesheet with one copied evidence rule, one reordered copy of another, and one copied variable name must produce three flags.
- **`outputs/gen-codex.mjs`** and **`outputs/gen-nanobanana.mjs`**
  - Command: `node outputs/gen-codex.mjs <project> --parallel 3` (`gen-nanobanana.mjs <project>` takes no `--parallel`).
  - Reads `assets-src/shotlist.json`. For every file missing from `assets-src/images/`, prompts `style + "\n\n" + prompt`. Codex renders at 1536×1024, 1024×1536 or 1024×1024, whichever is nearest the `aspect`. Skips files that exist. Appends one entry per file to `assets-src/generator.json`.
  - Exit 0 when the set is complete; 3 on a usage limit or quota stop (files already written are kept); 1 on any other error. `gen-nanobanana.mjs` reads `GEMINI_API_KEY` from the environment or `outputs/.env`.
  - Smoke test: a one-image shot list.
- **`<project>/tools/fontmatch.mjs`**
  - Command: `node tools/fontmatch.mjs --original <font-family as rendered> --candidates <comma list or auto>`
  - Renders the live original's font and each candidate in Playwright, measures cap-height-normalised text width, x-height and uppercase width, and writes a ranked `03-design-spec/fontmatch.json`. Prints the winner and a suggested `size-adjust`.
- **`outputs/TEMPLATE_BRIEF.md`** (one per delegated agent): this file's §2 to §8 and §10, plus that template's row from `TARGETS.md`, its six ports, the path of `NICHE-RULES.md`, and the rule "do not touch another template's folder or ports".
