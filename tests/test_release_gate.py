import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import release_gate as gate

ROOT = Path(__file__).resolve().parents[1]
CHECKLIST = ROOT / 'checklist/PRODUCTION_CHECKLIST_clone_swap.md'
NOW = datetime(2026, 10, 2, 12, tzinfo=timezone.utc)


class ReleaseGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        evidence = self.root / 'test-evidence.txt'
        evidence.write_text('Synthetic verification fixture, not a real website audit.\n')
        self.record = gate.template(CHECKLIST)
        release = self.record['release']
        release.update(revision='a'*40, artifact_sha256='b'*64, build_id='fixture-build-1',
                       built_at='2026-10-02T09:00:00Z', url='https://client.example.org',
                       environment='production', content_status='CLIENT-COMPLETE',
                       routes=['/', '/contact'], states=['rest', 'menu-open', 'form-error'],
                       viewports=['375x667', '1440x900'])
        for row in self.record['rows']:
            row.update(status='PASS', tester='Fixture reviewer',
                       checked_at='2026-10-02T10:00:00Z', release_revision=release['revision'],
                       artifact_sha256=release['artifact_sha256'], build_id=release['build_id'],
                       environment=release['environment'], url=release['url'],
                       coverage=['Fixture covers declared scope; production reviewer must inspect it'],
                       evidence=[{'path': evidence.name, 'sha256': gate.sha256(evidence)}])
            if row['id'] == 'LEG-07':
                row.update(status='N/A', applicable=False, reason='Retired row', predicate='Superseded by LEG-15')

    def result(self, phase='launch'):
        return gate.validate(self.record, CHECKLIST, self.root, phase, now=NOW, resolver=lambda host: ['8.8.8.8'])

    def row(self, key):
        return next(row for row in self.record['rows'] if row['id'] == key)

    def assertBlocked(self, fragment, phase='launch'):
        result = self.result(phase)
        self.assertEqual('BLOCKED', result['decision'])
        self.assertTrue(any(fragment in e for e in result['errors']), result['errors'])

    def pending(self, row, status):
        row.update(status=status, reason='Awaiting actual verification', owner='Delivery lead',
                   next_action='Run the documented check', review_by='2026-10-09T12:00:00Z')

    def test_complete_synthetic_record_passes_every_phase(self):
        for phase in gate.PHASES:
            with self.subTest(phase=phase):
                self.assertEqual([], self.result(phase)['errors'])

    def test_full_catalogue_and_existing_ids_remain(self):
        rows = gate.catalogue(CHECKLIST)
        self.assertEqual(270, len(rows))
        self.assertEqual(18, len({k.split('-')[0] for k in rows}))

    def test_missing_duplicate_unknown_rows(self):
        original = copy.deepcopy(self.record)
        self.record['rows'].pop()
        self.assertBlocked('missing row IDs')
        self.record = copy.deepcopy(original)
        self.record['rows'].append(copy.deepcopy(self.record['rows'][0]))
        self.assertBlocked('duplicate row IDs')
        self.record = original
        self.record['rows'].append({'id': 'BOGUS-01'})
        self.assertBlocked('unknown row IDs')

    def test_wrong_checklist_fingerprint(self):
        self.record['checklist_sha256'] = 'c'*64
        self.assertBlocked('fingerprint')

    def test_wrong_build_revision_and_artifact(self):
        for field in ('release_revision', 'build_id', 'artifact_sha256'):
            original = self.row('SPD-01')[field]
            self.row('SPD-01')[field] = 'wrong'
            self.assertBlocked(field)
            self.row('SPD-01')[field] = original

    def test_missing_tampered_empty_evidence(self):
        artifact = self.root / 'test-evidence.txt'
        artifact.write_text('Tampered')
        self.assertBlocked('hash mismatch')
        artifact.write_text('')
        self.assertBlocked('missing or empty')
        artifact.unlink()
        self.assertBlocked('missing or empty')

    def test_evidence_path_escape_and_symlink(self):
        self.row('SPD-01')['evidence'][0]['path'] = '../outside.txt'
        self.assertBlocked('escapes evidence root')
        outside = self.root.parent / (self.root.name + '-outside.txt')
        outside.write_text('outside')
        self.addCleanup(outside.unlink)
        (self.root / 'link.txt').symlink_to(outside)
        self.row('SPD-01')['evidence'][0]['path'] = 'link.txt'
        self.assertBlocked('escapes evidence root')

    def test_required_failure_exception_and_unrun_block(self):
        for status in ('FAIL', 'FIDELITY-EXCEPTION', 'NOT_RUN'):
            self.pending(self.row('SPD-01'), status)
            self.assertBlocked(f'{status} blocks')

    def test_unknown_and_inherited_are_not_passes(self):
        for status in ('INHERITED', 'pass', None, {'PASS': True}):
            self.row('SPD-01')['status'] = status
            self.assertBlocked('unknown status')

    def test_owner_cannot_be_automated(self):
        self.row('A11Y-18')['verification'] = 'automated'
        self.assertBlocked('owner evidence requires manual')

    def test_local_and_wrong_url_cannot_pass_live(self):
        self.row('HOST-01')['url'] = 'http://127.0.0.1:3000'
        self.assertBlocked('live PASS requires')
        self.assertBlocked('environment/URL')

    def test_production_host_canonicalization_and_dns(self):
        for url in ('https://localhost.', 'https://LOCALHOST.', 'https://example.org:bad'):
            self.assertFalse(gate.public_https(url))
        for answers in ([], ['127.0.0.1'], ['::1'], ['8.8.8.8', '10.0.0.1']):
            result = gate.validate(self.record, CHECKLIST, self.root, 'launch', now=NOW,
                                   resolver=lambda host: answers)
            self.assertEqual('BLOCKED', result['decision'])
        self.assertFalse(gate.global_destination('https://127.0.0.1.nip.io', lambda host: ['127.0.0.1']))
        def unavailable(host):
            raise OSError('DNS unavailable')
        self.assertFalse(gate.global_destination('https://client.example.org', unavailable))

    def test_fidelity_build_and_content_pending_block_launch(self):
        self.record['release']['a11y'] = 'off'
        self.assertBlocked('accessibility')
        self.record['release']['a11y'] = 'on'
        self.record['release']['content_status'] = 'CONTENT-PENDING'
        self.assertBlocked('CLIENT-COMPLETE')

    def test_handover_pending_does_not_pass_launch(self):
        for row in self.record['rows']:
            cls = gate.catalogue(CHECKLIST)[row['id']]
            if cls.endswith('-L'):
                self.pending(row, 'AWAITING-DEPLOY')
            elif cls.endswith('-O'):
                self.pending(row, 'OWNER-CONFIRM')
        self.record['release']['content_status'] = 'CONTENT-PENDING'
        self.assertEqual([], self.result('handover')['errors'])
        self.assertBlocked('blocks launch')

    def test_pending_status_cannot_hide_local_check(self):
        self.pending(self.row('SPD-01'), 'AWAITING-DEPLOY')
        self.assertBlocked('only applies to live', 'handover')
        self.pending(self.row('SPD-01'), 'OWNER-CONFIRM')
        self.assertBlocked('only applies to owner', 'handover')

    def test_na_requires_conditional_row_predicate_and_evidence(self):
        row = self.row('BACK-01')
        row.update(status='N/A', applicable=False, predicate='No forms/endpoints in reviewed inventory', reason='Static site')
        self.assertEqual([], self.result()['errors'])
        row.pop('predicate')
        self.assertBlocked('absence predicate')
        row = self.row('SPD-01')
        row.update(status='N/A', applicable=False, predicate='No desire to test', reason='Skipped')
        self.assertBlocked('unconditional required')

    def test_recommended_miss_and_field_unavailable_prevent_gold_only(self):
        for key, status in [('SPD-21', 'UNAVAILABLE'), ('SUS-01', 'FAIL')]:
            self.pending(self.row(key), status)
        self.assertEqual([], self.result('launch')['errors'])
        self.assertBlocked('blocks gold', 'gold')
        self.pending(self.row('SPD-01'), 'UNAVAILABLE')
        self.assertBlocked('only applies to field-data')

    def test_recommended_omission_requires_action_owner_and_date(self):
        self.row('SUS-01')['status'] = 'NOT_RUN'
        self.assertBlocked('unresolved result needs')
        self.pending(self.row('SUS-01'), 'NOT_RUN')
        self.row('SUS-01')['review_by'] = '2026-10-01T00:00:00Z'
        self.assertBlocked('overdue')

    def test_evidence_before_build_future_or_missing_timezone(self):
        for date in ['2026-10-01T00:00:00Z', '2030-01-01T00:00:00Z', '2026-10-02T10:00:00']:
            self.row('SPD-01')['checked_at'] = date
            self.assertBlocked('SPD-01:')

    def test_empty_scope_coverage_and_evidence_rejected(self):
        self.record['release']['routes'] = []
        self.assertBlocked('release.routes')
        self.row('SPD-01')['coverage'] = []
        self.assertBlocked('explicit coverage')
        self.row('SPD-01')['evidence'] = []
        self.assertBlocked('nonempty saved evidence')

    def test_malformed_record_types_fail_closed(self):
        for rows in [None, {}, [None], [{'id': []}], [{'id': 'SPD-01', 'status': []}]]:
            self.record['rows'] = rows
            self.assertEqual('BLOCKED', self.result()['decision'])

    def test_duplicate_json_keys_rejected(self):
        path = self.root / 'duplicate.json'
        path.write_text('{"rows": [], "rows": []}')
        with self.assertRaisesRegex(ValueError, 'duplicate JSON key'):
            gate.read_record(path)

    def test_cli_init_no_overwrite_and_unverified_record_exits_nonzero(self):
        path = self.root / 'release.json'
        command = [sys.executable, str(ROOT/'scripts/release_gate.py'), str(path), '--checklist', str(CHECKLIST)]
        self.assertEqual(0, subprocess.run(command+['--init'], capture_output=True).returncode)
        self.assertEqual(1, subprocess.run(command+['--init'], capture_output=True).returncode)
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
        self.assertEqual('BLOCKED', json.loads(result.stdout)['decision'])

    def test_cli_rejects_invalid_json(self):
        path = self.root / 'bad.json'
        path.write_text('{')
        result = subprocess.run([sys.executable, str(ROOT/'scripts/release_gate.py'), str(path), '--checklist', str(CHECKLIST)], capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
        self.assertEqual('BLOCKED', json.loads(result.stdout)['decision'])

    def test_checklist_empty_or_duplicate_rejected(self):
        path = self.root / 'checklist.md'
        path.write_text('No rows')
        with self.assertRaisesRegex(ValueError, 'no rows'):
            gate.catalogue(path)
        path.write_text('| SPD-01 | Test | Test | G |\n'*2)
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            gate.catalogue(path)


if __name__ == '__main__':
    unittest.main()
