# Independent review: clone workflow

Reviewed the named clone scripts, tests, workflow document, and prompt integration. No source files changed. The prompt and docs correctly say this is a sample gate and that it grants no production clearance.

## Findings

1. **[P1] Empty generated-slot scope bypasses media validation**: `scripts/clone_gate.py:107-120`. The adapted gate only loads `--app` and checks the registry under `if slots:`. With `generated_slots: []`, an adapted record can return `stage_complete: true` even when the app contains generated slots or a generated manifest entry with no valid registry/model receipt. `--app` is optional in this case. Require the app inventory to match the declared set exactly; an empty declaration should assert there are no generated entries. Add a negative fixture for undeclared generated media.

2. **[P2] Client precedence conflicts with final registry validation**: `scripts/generated_media.py:100-105,117-129`. `prepare_sync` preserves a client slot and leaves its generated asset in the supplied registry. `validate` then requires the site's generated-slot set to equal every registry asset, so the documented client-wins result fails final validation. The existing client test checks only preparation, not validation. Define how superseded assets remain archived versus active, then test the full prepare/validate path.

3. **[P2] Original media can be placed in the public tree**: `scripts/generated_media.py:56`. The helper checks only that the original is hashed under the app root. It accepts `public/original.png`, contrary to `docs/CLONE_WORKFLOW.md:70-80`, so static hosting exposes the original. Reject originals resolving inside `app/public`.

4. **[P2] Deeply nested JSON crashes both CLIs**: `scripts/clone_gate.py:137-139`; `scripts/generated_media.py:147-155`. `RecursionError` is outside both exception lists. I reproduced traceback output with a 1,100-level JSON array for each command. Bound JSON nesting or catch this error and return the normal incomplete result; add CLI regression coverage.

5. **[P2] Source URL is only checked for nonempty text**: `scripts/clone_gate.py:41,65`. A value such as `not-a-url` passes, and anchor source hashes are not linked to a sample capture record. Validate absolute HTTP(S) URLs and bind each sample's source metadata to a hashed capture manifest. This still cannot prove the capture came from that URL.

## Validator limits, not separate bugs

Hashes establish that files match declared hashes; they do not authenticate provider receipts, prove measurements, or prove inventory completeness. Rewriting a manifest and stale check references together can still manufacture a self-consistent record. The docs disclose these trust limits, so they should not be described as verified visual truth. This review did not inspect checklist ID/tier sources, so it does not attest to the 275-row invariant.
