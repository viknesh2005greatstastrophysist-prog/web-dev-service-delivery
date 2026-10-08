# Clone proof and original generated media

Use this with the [daily release workflow](CHECKLIST_WORKFLOW.md), not as another production
checklist. The 275 stable rows and Diamond floor remain unchanged. The fifteen full fidelity
gates still apply to a commissioned clone. These smaller controls prevent expansion while
the representative sample is unresolved; they do not replace full-site testing.

## 1. Freeze the acceptance contract before building

Keep `clone-contract.json`, `clone-record.json`, source captures and generation records in the
private evidence workspace. Pin the contract's SHA-256 in the pre-build scope/handoff commit.
Pass that saved pin to the gate. Do not obtain a fresh pin after changing tolerances to fit
the candidate. An agreed scope change needs a new recorded version and affected comparisons.

Contract schema_version is 1. `samples` is a nonempty list. Each sample has `id`, `route`,
`source_url`, `captured_at`, distinct `viewports` including desktop and mobile, distinct `states`
including `rest`, a hashed `capture` manifest, and a boolean `motion`. The capture manifest
records the same source_url/captured_at and a nonempty files inventory of `{path, sha256}`.
URLs must be absolute HTTP(S) without credentials; each anchor source must be in its sample's
capture inventory. A motion sample also requires `signature-motion`
and `reduced-motion`. Include applicable menus, overlays and a reserved validation state.

`anchors` is a nonempty list. Every declared sample/viewport/state must have at least one anchor.
Each anchor has `id`, `sample`, `viewport`, `state`, `kind`, `criterion`, `method`, `tolerance`,
a nonempty `dependencies` list and `source: {path, sha256}`. Motion states use kind `motion`.
Paths are relative to the private workspace root and cannot escape it, including via symlinks.

Define useful anchors, not just one easy element per screen. Record source variability first.
Font size, alignment, line count, box geometry and motion endpoints need their own measures.
No blanket viewport-percentage tolerance or average score may hide a failed critical anchor.
Different truthful copy or licensed fonts can require an explicit design exception. Approval
of that exception does not prove the original geometry matched.

`generated_slots` is an explicit list exactly matching the final app, or [] when there is no
active generated media. The adapted gate requires --app even for an empty declaration.
`required_model` is the actual model ID required by the scope, or null for no specific model
claim. Do not normalize a display name into a supposedly observed provider model ID.

## 2. Close the reference sample before expansion

The record has schema_version 1, the pinned `contract_sha256`, `artifacts` and `checks`.
Each artifact is `{path, sha256}` pointing to a JSON manifest with a nonempty `files` list
of `{path, sha256}` entries. Inventory all scoped compiled files, fonts, content and media,
not only a server entry point. The gate rehashes both the manifest and its underlying files.
It cannot detect files deliberately omitted from an incomplete inventory; review coverage.

Each check has `id` matching an anchor, `phase` (`reference` or `adapted`), `status`
(`PASS`, `FAIL`, `NOT_RUN`) and `artifact_sha256` matching that phase's manifest. PASS needs
a nonempty `evidence` list of hashed files. Open results need `reason`, `owner`, `next_action`.
Missing source files do not erase available screenshots/DOM observations. Mark only unsupported
claims unresolved. A download 403 is not proof that every visual property is unknowable.

```sh
python3 scripts/clone_gate.py /private/clone-contract.json /private/clone-record.json \
  --root /private --phase reference --contract-sha256 <saved-pre-build-pin>
```

Nonzero exit means the sample is incomplete. Stop expansion; continue useful independent work
or produce a resumable partial handover. Never call that handover an accepted clone.

## 3. Generate for the scene, then fit the result

Approved client media takes precedence. For original AI imagery, use the installed image-generation
workflow and a supported authorized provider/tool. Do not substitute stock silently. If generation
or required model attribution is unavailable, record the gap and use an explicitly pending
placeholder for private preparation. No image generation is performed by these Python helpers.

The private registry has schema_version 1 and an `assets` list. Each asset supplies:

- `slot`, `provider`, `prompt`, `requested_model`, `observed_model` (null when unknown).
- `brief`: subject, camera, lighting, materials, composition, negative_space, mobile_crop.
- `intended_use: concept-illustration`. Other uses need a separately reviewed policy, not a
  fabricated client-work claim.
- `original: {path, sha256}` and `derivatives`, each with path, sha256, profile (`desktop` or
  `mobile`), positive integer width/height, crop description and public URL. Both profiles are
  required. Paths here are relative to the app root; originals stay outside public assets.
- When observed_model is supplied, `model_evidence` identifies a retained JSON provider/tool
  response exposing a matching `model` field. A request, filename or invented wrapper is not
  observed identity. If the provider exposes no model field, preserve null and disclose it.

The helper checks hashes and declared metadata. It does not authenticate provider records or
decode image dimensions. The app's processing/render checks must verify actual dimensions,
formats, crops, alt treatment and usefulness. Keep prompts, keys and responses private and
outside the deployed artifact. Hash-only public manifest entries carry no prompts or receipts.
Missing model evidence means the named-model requirement is unverified, not that an image is
unsafe or illegal. Origin, legal rights, truthful use and design quality need separate decisions.

Website-preview UI must come from real working builds. Generated illustrations cannot replace
functional controls or imply invented projects, testimonials, clients or measured outcomes.

## 4. Use the executable media path in content sync

The app's `content/site.json` has keyed `slots`; generated image slots use source `generated`.
The image manifest has an `images` list. The helper prepares both proposed outputs:

```sh
python3 scripts/generated_media.py /private/app /private/generated-media.json \
  --prepare-sync > /private/proposed-content.json
```

Client slots win; unsupplied slots remain unchanged. Empty input is a no-op. Malformed supplied
records fail before any app writes. Repeated unchanged input is idempotent. Integrate the returned
`site` and `manifest` in the app's existing `content:sync`: stage the pair, run build/decoder/render
checks, then commit together with rollback to the last good pair on failure. The helper itself
only reads and emits a proposal; a successful proposal is not a successful app build.

Validate the final deployed-content inputs using the complete retained registry:

```sh
python3 scripts/generated_media.py /private/app /private/generated-media.json \
  --required-model <actual-required-provider-model-id>
```

Generated slots, tracked URLs and public manifest entries must agree exactly. Private records
superseded by a client slot remain archived, but are excluded from active generation validation;
sync removes their generated public manifest entries. Model-specific
validation fails if any generated image lacks that observed model record. Do not put a pending
exact-model requirement into the record as verified. Regenerate source counts and approval notes.

## 5. Close the adapted sample, then expand

The adapted gate also checks the reference results. Every sample needs a separate
`design_acceptance` entry: sample, status (`ACCEPTED` or an unresolved value), reviewer,
artifact_sha256 and hashed evidence. This is the authorized scene review, not launch approval
or a mandatory new human request for each minor asset edit. Contractual client signoff remains
part of the independent release record.

For generated slots, the record additionally has a hashed `generated_registry`. The gate reads
the final app content and manifest and validates them against that registry and model requirement.

```sh
python3 scripts/clone_gate.py /private/clone-contract.json /private/clone-record.json \
  --root /private --app /private/app --phase adapted --contract-sha256 <saved-pre-build-pin>
```

Changing copy, fonts, media, layout or motion reopens affected comparisons and approvals.
Rebuild the artifact manifest, then record fresh checks; changing only the manifest hash in old
results is dishonest. Test final desktop/mobile crops, loading, contrast and motion together.
Static screenshots cannot pass motion. Unknown or rejected samples cannot average into PASS.

## 6. Bound cost and claims

Set a resource allowance before work. Track time, retries, corrections and gaps separately by
sample. At expiry preserve files, hashes, failed/unrun checks, owner, next action and resumption
conditions. One run proves bounded feasibility only. A clean replay tests reproducibility.

The gate's success validates declared record completeness for the named sample. It cannot prove
measurement truth, all pages, artistic quality, legal clearance or production readiness. Run the
fifteen full fidelity gates and independent release_gate.py phases for their respective claims.
