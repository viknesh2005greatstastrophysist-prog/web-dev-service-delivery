# Local verification

Executed 2026-10-02 against the proposed production-audit changes, with CI supplied as an inactive template. Tests use synthetic records, not client evidence. Trailing console padding is removed below; result text is unchanged.

## `python3 scripts/check-kit.py`

Exit code: 0

```text
PASS  checklist: strict row grammar and nonempty catalogue
PASS  checklist: IDs exactly match stable inventory
PASS  README row count matches catalogue
PASS  checklist: no duplicate row IDs
PASS  checklist: every row has 4 cells
PASS  checklist: every row ends in a valid class (G, R or C, optional -L or -O)
PASS  checklist: IDs sorted within each section
PASS  every row ID cited in either file exists
PASS  prompt section list equals the checklist's headings
PASS  prompt section count word matches the list
PASS  prompt has numbered sections 1 to 8
PASS  every § reference points at a section 1 to 8
PASS  Finish lists gates 1 to 15 in order
PASS  Finish says 'all fifteen'
PASS  prompt has ground rules 1 to 10
PASS  checklist has rules of application 1 to 10
PASS  checklist 'rule N' references exist
PASS  no em or en dashes in the prompt or the checklist
PASS  no machine-specific absolute paths
PASS  kit file exists: skills/scroll-craft/SKILL.md
PASS  kit file exists: skills/scroll-craft/scripts/shoot.mjs
PASS  kit file exists: skills/scroll-craft/references/verify.md
PASS  kit file exists: skills/scroll-craft/LICENSE
PASS  kit file exists: checklist/PRODUCTION_CHECKLIST_clone_swap.md
PASS  kit file exists: examples/CLIENT_INPUT/brief.md
PASS  kit file exists: scripts/release_gate.py
PASS  kit file exists: tests/test_release_gate.py
PASS  kit file exists: docs/RELEASE_EVIDENCE.md
PASS  kit file exists: docs/ci/verify-kit.yml
PASS  methodology submodule is checked out (run: git submodule update --init)
PASS  methodology checkout matches reviewed pin
PASS  prompt names the reviewed methodology pin
PASS  prompt uses executable release record
PASS  prompt omits superseded policy: LCP minus TTFB
PASS  prompt omits superseded policy: else `build`
PASS  prompt omits superseded policy: For any other client the fidelity build ships
PASS  prompt omits superseded policy: ready for a human to deploy
PASS  deploy build is always accessible
PASS  active Markdown file links resolve: README.md
PASS  active Markdown file links resolve: docs/HOW_TO_RUN.md
PASS  active Markdown file links resolve: docs/RELEASE_EVIDENCE.md
PASS  active Markdown file links resolve: checklist/PRODUCTION_CHECKLIST_clone_swap.md

rows: 262   prompt words: 16068   checklist words: 20940
ALL CHECKS PASSED
```

## `python3 -m unittest discover -s tests -v`

Exit code: 0

```text
test_broken_entry_point_link_fails (test_check_kit.KitConsistencyTests) ... ok
test_malformed_row_fails_without_traceback (test_check_kit.KitConsistencyTests) ... ok
test_missing_finish_section_fails_without_traceback (test_check_kit.KitConsistencyTests) ... ok
test_silent_row_removal_fails_inventory (test_check_kit.KitConsistencyTests) ... ok
test_stale_document_count_fails (test_check_kit.KitConsistencyTests) ... ok
test_valid_kit (test_check_kit.KitConsistencyTests) ... ok
test_checklist_empty_or_duplicate_rejected (test_release_gate.ReleaseGateTests) ... ok
test_cli_init_no_overwrite_and_unverified_record_exits_nonzero (test_release_gate.ReleaseGateTests) ... ok
test_cli_rejects_invalid_json (test_release_gate.ReleaseGateTests) ... ok
test_complete_synthetic_record_passes_every_phase (test_release_gate.ReleaseGateTests) ... ok
test_duplicate_json_keys_rejected (test_release_gate.ReleaseGateTests) ... ok
test_empty_scope_coverage_and_evidence_rejected (test_release_gate.ReleaseGateTests) ... ok
test_evidence_before_build_future_or_missing_timezone (test_release_gate.ReleaseGateTests) ... ok
test_evidence_path_escape_and_symlink (test_release_gate.ReleaseGateTests) ... ok
test_fidelity_build_and_content_pending_block_launch (test_release_gate.ReleaseGateTests) ... ok
test_full_catalogue_and_existing_ids_remain (test_release_gate.ReleaseGateTests) ... ok
test_handover_pending_does_not_pass_launch (test_release_gate.ReleaseGateTests) ... ok
test_local_and_wrong_url_cannot_pass_live (test_release_gate.ReleaseGateTests) ... ok
test_malformed_record_types_fail_closed (test_release_gate.ReleaseGateTests) ... ok
test_missing_duplicate_unknown_rows (test_release_gate.ReleaseGateTests) ... ok
test_missing_tampered_empty_evidence (test_release_gate.ReleaseGateTests) ... ok
test_na_requires_conditional_row_predicate_and_evidence (test_release_gate.ReleaseGateTests) ... ok
test_owner_cannot_be_automated (test_release_gate.ReleaseGateTests) ... ok
test_pending_status_cannot_hide_local_check (test_release_gate.ReleaseGateTests) ... ok
test_production_host_canonicalization_and_dns (test_release_gate.ReleaseGateTests) ... ok
test_recommended_miss_and_field_unavailable_prevent_gold_only (test_release_gate.ReleaseGateTests) ... ok
test_recommended_omission_requires_action_owner_and_date (test_release_gate.ReleaseGateTests) ... ok
test_required_failure_exception_and_unrun_block (test_release_gate.ReleaseGateTests) ... ok
test_unknown_and_inherited_are_not_passes (test_release_gate.ReleaseGateTests) ... ok
test_wrong_build_revision_and_artifact (test_release_gate.ReleaseGateTests) ... ok
test_wrong_checklist_fingerprint (test_release_gate.ReleaseGateTests) ... ok

----------------------------------------------------------------------
Ran 31 tests in 1.699s

OK
```

## `git diff --check`

Exit code: 0

```text
(no diagnostics)
```
