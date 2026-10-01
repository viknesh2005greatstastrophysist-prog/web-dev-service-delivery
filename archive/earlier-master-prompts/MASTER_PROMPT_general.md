# Master prompt: Awwwards pixel rebuilds + scroll-craft dynamics layer (3 templates, any niche)

Paste this whole file into a coding agent (Claude Code or similar) that has a shell, Node 20+, Python 3 with Pillow, a full ffmpeg build, an installed Google Chrome, and a local Codex CLI. Fill in §0.1 first; everything else derives from it.

The pipeline has two layers, and they never mix:

1. **The rebuild.** A pixel-for-pixel layout, type, colour and spacing rebuild of an award-winning Awwwards site, reskinned for an original fictional business. This layer is judged by computed styles and side-by-sides against the live original. Nothing in layer 2 is allowed to move a single rest-state pixel.
2. **The dynamics layer (scroll-craft).** A final add-on pass that smooths the scroll and refines the motion using the scroll-craft skill: scroll feel, easing, cue timing, dead-scroll removal, parallax depth, pointer response, reduced motion and touch. It changes *how the page gets from one frame to the next*, never *what the frames are*.

---

## 0. Mission

### 0.1 Parameters (fill these in)

| Parameter | Value | Notes |
|---|---|---|
| `NICHE` | `<e.g. dental clinics>` | The business category, in plain words |
| `SLUG` | `<e.g. dental>` | Lowercase, underscores; used in folder names |
| `CUSTOMER` | `<optional, e.g. families choosing a local dentist>` | Who hires this business. If blank, the agent writes it in Stage 0 |
| `DEV_PORT` | `<e.g. 5173>` | Template N uses `DEV_PORT + N - 1` for dev and `DEV_PORT - 1000 + N - 1` for preview. Pick a base no other running template uses |
| `SKILL_SRC` | `/Users/vik/Downloads/scrollcraft (2)/scroll-craft` | Where the scroll-craft skill folder lives |

### 0.2 The job

For `NICHE`, build **three distinct website templates**. Each one rebuilds a **different** award-winning Awwwards site for an **original fictional business** in that niche.

- **At rest, the rebuild must be indistinguishable from the original** at the same viewport: layout, design system, spacing, type scale, colour tokens, image slots, breakpoints, component states. "At rest" means each section in its resolved frame (fully in view, reveals finished, pointer idle) and each interactive state after its transition has ended.
- **In motion, the rebuild is allowed to be better.** Once the rest-state gate is green, the scroll-craft dynamics layer makes scrolling smoother and the transitions between rest states richer and calmer. Every change it makes must land on exactly the original's end state.
- Brand, copy, logo, imagery and code are all your own.

This work goes into a public video comparison against other models, credited by name. Treat the comparison as literal: your build next to the real site, at the same viewport, at full screen. Paused, they must match. Scrolling, yours should feel easier.

Run **completely autonomously**. Don't stop between stages, don't ask for approval and don't ask questions. Report only when all three templates are finished and verified.

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
2. **Search Awwwards for winners only**: Site of the Day, Site of the Month, Honorable Mention or Developer Award. Nominees don't count. Open each candidate's Awwwards page and record the award and date from it; never cite an award from memory. Search the exact niche first, then walk down the adjacency list.
3. **Qualify each candidate.** It must be a real business in the niche or an adjacent category, public, with no login or paywall, and genuinely impressive rather than easy to match. State why it transfers to `NICHE`.
4. **The three targets must differ on at least 4 of scroll-craft's 6 fingerprint dimensions** (grammar, nav treatment, hero device, act-sequence shape, close pattern, signature move), checked pairwise. Classify each target's structure against `scroll-craft/references/uniqueness.md` §2 before committing. If two targets collide, swap one.
5. If a target turns out to be unclonable for a hard reason (down, gated, a video with no site behind it), pick another and record the swap.

For each chosen target, record in `outputs/TARGETS.md`: exact URL, award with link to its Awwwards page, niche match, why chosen, the scroll-craft grammar it maps to, its signature interaction, and the fictional brand.

**Fictional brands.** Invent names that don't belong to a real business in the niche or its adjacent categories (search the name before using it). Where the original has a giant wordmark or title, match its letter count and silhouette so it fills the same width. The brand's services should be the niche's real services, so the copy reads as a credible business of that kind.

**Niche rules.** Write `outputs/NICHE-RULES.md` before any copy exists. List the claims that are regulated, risky or misleading in this niche and ban them in all three templates. Typical families to check:
- outcome and performance promises (health results, financial returns, legal wins, savings, rankings)
- guarantees (price, timeline, refund, "100% satisfaction")
- credentials (real licences, regulator or association logos, certification marks, awards the fiction didn't win)
- safety, medical, legal or financial advice presented as real guidance
- anything that impersonates a real brand, person or place of business

---

## 2. Methodology (read first, follow it)

### 2a. The rebuild methodology

Clone `https://github.com/per-simmons/clone-app-pat-pro-public` into each template folder as `methodology/`. Read `SKILL.md` and `references/00-contract.md` before doing anything else, then each stage reference as you reach it (`01-recon.md` … `07-polish.md`).

The contract defines the workspace layout (`clone-workspace/<name>/00-config.json`, `01-recon/`, `02-extraction/`, `03-design-spec/`, `04-architecture/`, `06-qa/cycle-N/`, `09-polish/`), artifact filenames, stage inputs and outputs, the verification gate and the convergence loop. `methodology/scripts/assert-styles.mjs` is the gate.

### 2b. The scroll-craft skill (dynamics layer only)

Copy the skill folder from `SKILL_SRC` to `outputs/scroll-craft/`, intact. Write `outputs/.scrollcraft.json`:

```json
{ "workspace": "scrollcraft-workspace" }
```

so all three templates share one workspace (`outputs/scrollcraft-workspace/`) and one fingerprint registry. Then run, once:

```bash
node outputs/scroll-craft/scripts/doctor.mjs
node outputs/scroll-craft/scripts/workspace.mjs --ensure
```

Record the doctor output in `outputs/scrollcraft-workspace/doctor.txt`. A missing `KIE_AI_API_KEY` is fine (see §4). Any other required failure must be fixed, not worked around.

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
2. **Browsers.** Recon, extraction and the style gate use Playwright Chromium (`chromium.launch({ channel: 'chromium' })`), never the Chrome extension. **Computed styles read through `getComputedStyle` are the ground truth.** Screenshots are a visual reference only. Never build the style gate on a pixel diff. The scroll-craft harness (`shoot.mjs`) uses installed Google Chrome (it needs the h264 decoder); set `SCROLLCRAFT_CHROME` if doctor can't find it.
3. **No lifted assets.** Never hotlink or download the original's images, video, fonts or logo for use. This overrides contract §3-F/G. You *may* download the original's stylesheets **to read values from**; keep them in `02-extraction/` as evidence only, and never ship them.
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
- **Originality gate:** `python3 outputs/check-css-overlap.py <project> --list` must report `flagged: 0`. It flags `identical`, `same-body`, `same-set` (4+ equal declarations in any order) and `target-var` (a custom-property name the original defines). Renaming selectors on identical blocks is **not** a fix: re-author the rule (token-driven custom properties, composition, logical properties and shorthands, dropped redundant declarations), then re-run the style gate to prove no computed value moved.
- **Fonts:** pick the closest open font from Google Fonts or jsDelivr/Fontsource by **measuring** it against the live font: cap-height-normalised text width, x-height and uppercase width across about 30 candidates (`tools/fontmatch.mjs`). Alias the winner in `@font-face` with `size-adjust` when that improves the cap-height match. Record the numbers.

---

## 4. Imagery (Codex first, then fallbacks)

Use **Codex** (`/Applications/ChatGPT.app/Contents/Resources/codex exec`) with its built-in image tool when it's available, and the fallback chain in step 2 when it isn't. No stock downloads, none of the original's photography.

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
5. **`assets-src/process.py`:** centre-crops each PNG to its slot aspect (per-slot anchor override allowed), writes `site/public/images/<name>.jpg` (max 2400px long edge, q84) and `<name>-sm.jpg` (half size).
6. **Video only where the original scrubs or plays video.** If the original has a scroll-scrubbed hero or image sequence and `KIE_AI_API_KEY` is set, animate a Codex still with `node outputs/scroll-craft/scripts/kie.mjs shot …`, then encode with `bash outputs/scroll-craft/scripts/encode.sh` (desktop and `mobile` variants) so it scrubs rather than stutters. Cap it at 4 clips per template and log the spend. Without a key, use an image sequence or the still, and document it. Never add video where the original has none.
7. If generation is capped mid-set, reduce scope honestly (fewer projects, opposite-orientation crops of generated frames for variety) and document it.

---

## 5. Stack

- Vite + React 18 + TypeScript + GSAP (+ Lenis when the original uses smooth scroll, or when the dynamics layer adds it per §6 step 9), in `<project>/site`.
- `npm i -D playwright-core` in `<project>/site` (the scroll-craft harness resolves it from the cwd).
- `npm run dev` / `npm run preview` on the template's ports, with `--host 127.0.0.1`.
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
   - `build-assertions.mjs` emits `assertions.json`, one entry per viewport, state and selector, keyed `"<viewport>|<state>|<clone selector>"`. Tag every prop with a `layer`:
     - `"rest"`: colour, background, font size, weight, line height, letter spacing, padding, margin, radius, backdrop filter, position, z-index, cursor, rects, and the **final** transform and opacity of each state. These must match exactly, always.
     - `"motion"`: `transition-*`, `animation-*`, scroll-behavior and in-flight values. These match the original through step 8, then may change in step 9 only as recorded in `DYNAMICS.md`.
   - Cover every built component and state (earlier templates came to between 369 and 2,852 assertions).
4. **Architecture** (`04-architecture/file-tree.md`, `component-map.md`), then **build** in `site/`. Rebuild the target's own motion faithfully first. Don't pre-empt step 9.
5. **QA and convergence** (`06-qa/cycle-N/`)
   - `tools/read-styles.mjs` opens the site, **drives each state exactly as a user would** (moves the pointer, hovers, clicks, scrolls in steps, waits for transitions to end) and reads `getComputedStyle` for every asserted selector → `clone-styles.json`.
   - `node methodology/scripts/assert-styles.mjs --assertions … --clone-styles … --out metrics.json`.
   - Fix and loop until **0 failures on all layers and `npm run build` exits 0**. Contract convergence rules apply (stop if the loop stalls, cap at 10 cycles).
6. **Target validation (required)**
   - Run the same reader against the live original through a selector map (clone selector → original selector), scored with the **same** assertions, into `06-qa/target-validation/`.
   - Every mismatch means the spec recorded an authored value where the runtime computes something else (for example a JS-injected `* { cursor: none !important }`, or an unscoped variable falling back to black). Correct the assertion to the runtime value, change the clone to match, re-run both.
   - **Final state: the clone has 0 failures AND the original has 0 failures on the same assertion set.**
7. **Originality gate:** `check-css-overlap.py` reports `flagged: 0` (§3). Re-run the clone gate after any re-author.
8. **Eyeball pass (rest states)**
   - Side-by-sides (original | clone) at every breakpoint and every key state, **with the real generated photography**, taken at the recorded rest frames. Plus frame strips of the intro, transitions and scroll reveals.
   - Fix what the assertions can't see: clipping, stacking, remounts, timing, line breaks. Save to `09-polish/rest/`.
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

   **Implementation.** Write the layer in the site's own GSAP/TS code, following the device specs in `devices.md`. You may mount the untouched engine (`ScrollCraft.mount(root)`) for devices it does better (scrubbed media, cue windows, drift), but it has no `destroy()`, so mount it once on a root that persists across route changes and call `layout()` after each transition, rather than mounting per route. Keep the layer in its own folder (`site/src/dynamics/`) so it can be switched off with one flag for the step 10 diff.

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
    - Re-shoot the step 8 side-by-sides at the same rest frames; they must be visually identical to `09-polish/rest/`.
    - Measure document height and every section rect with the layer on and off; any difference over 1px fails.
    - Re-run `check-css-overlap.py`.
    - Append the template's row to `outputs/scrollcraft-workspace/FINGERPRINTS.md` (its dimensions are the target's), and confirm the three rows differ pairwise on at least 4 of 6.
11. **Docs**
    - `clone-workspace/<name>/status.json`, `progress.md`, `final-report.md`.
    - `<project>/README.md`: target URL, award (linked to its Awwwards page), niche match and why it was chosen; how to run it; what was built; a substitutions table (fonts, images, brand, copy, code); the cycle table; the target-validation result; the originality checker line; the dynamics layer summary (the feeling curve, the peak, the change table, harness results for desktop, mobile and reduced motion, the toggle flag); scroll-craft conflicts; and an honest list of known gaps, including what a real phone might show that headless Chrome can't (verify.md "The phone is a different machine").

---

## 7. The gate (all conditions must hold)

1. `assert-styles.mjs` on the clone **with the dynamics layer on**: 0 failed on `rest`, and every `motion` diff accounted for in DYNAMICS.md.
2. The same assertions on the live original: 0 failed.
3. `npm run build` exits 0, and `npm run dev` runs without errors.
4. `check-css-overlap.py`: flagged 0.
5. Rest-state side-by-sides saved and identical before and after the dynamics layer; document height and section rects unchanged (≤1px).
6. `shoot.mjs` on desktop, mobile and reduced motion: 0 dead scroll, 0 never-full-opacity cues, 0 contrast failures, except `inherited` findings listed with evidence.
7. Feel check done and written into DYNAMICS.md; approved-collection §7 functional checks pass.
8. No copy breaks `NICHE-RULES.md` or the §3 copy rules (grep the built output for em dashes and the banned phrases).
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
- Template 1 can be built directly by the orchestrator. Templates 2 and 3 run as **parallel background agents**, one per folder with separate ports, each given this file plus its row from `outputs/TARGETS.md` and `outputs/NICHE-RULES.md`.
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
- the dynamics layer: peak, change count, harness results (desktop / mobile / reduced), feel-check diff
- the dev command and URL
- known gaps

Close with a one-table summary of all three.

---

### Appendix: tools used

**Shared, in `outputs/`:**
- `gen-codex.mjs`: Codex image runner
- `gen-nanobanana.mjs`: Gemini fallback
- `check-css-overlap.py`: originality gate
- `TEMPLATE_BRIEF.md`: the per-agent brief
- `TARGETS.md`, `NICHE-RULES.md`: Stage 0 output
- `scroll-craft/`: the skill (`scripts/doctor.mjs`, `workspace.mjs`, `shoot.mjs`, `kie.mjs`, `encode.sh`; `engine/scrollcraft.js`; references)
- `scrollcraft-workspace/`: shared workspace and `FINGERPRINTS.md`

**Per template, in `<project>/tools/`:**
- `shoot.mjs`, `probe.mjs`, `intro.mjs`: recon
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
