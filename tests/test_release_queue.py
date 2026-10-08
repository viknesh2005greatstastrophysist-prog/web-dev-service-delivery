"""Adversarial tests for complete, honest work views rather than release approval."""
import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import release_gate as gate
import release_queue as view

CHECKLIST = ROOT/'checklist/PRODUCTION_CHECKLIST_clone_swap.md'
TIERS = ROOT/'checklist/tiers.json'
BUNDLES = ROOT/'checklist/bundles.json'
NOW = datetime(2026, 10, 8, tzinfo=timezone.utc)


class ReleaseQueueTests(unittest.TestCase):
    def setUp(self):
        self.record = gate.template(CHECKLIST)

    def report(self, tiers=TIERS, bundles=BUNDLES):
        return view.queue(self.record, CHECKLIST, tiers, bundles, now=NOW)

    def row(self, key):
        return next(r for r in self.record['rows'] if r['id'] == key)

    def test_unverified_starter_keeps_every_diamond_and_all_275_ids(self):
        report = self.report()
        self.assertTrue(report['advisory_only'])
        self.assertEqual(275, sum(len(rows) for rows in report['buckets'].values()))
        self.assertEqual(gate.DIAMOND_FLOOR, {r['id'] for r in report['buckets']['Diamond work']})
        self.assertTrue(all(r['bundles'] for rows in report['buckets'].values() for r in rows))
        self.assertTrue(all(r['record_issues'] for rows in report['buckets'].values() for r in rows))

    def test_future_gold_and_unavailable_field_data_are_visible_without_completion(self):
        self.row('SEO-13')['status'] = 'NOT_RUN'
        self.row('SPD-21')['status'] = 'UNAVAILABLE'
        report = self.report()
        future = report['buckets']['Scheduled and optional follow-ups']
        self.assertTrue({'SEO-13', 'SPD-21'} <= {r['id'] for r in future})
        self.assertNotIn('decision', report)
        self.assertIn('Later Gold observations still block full Gold', view.markdown(report))

    def test_contracted_silver_is_due_work_not_optional_followup(self):
        self.record['release']['required_rows'] = ['SUS-01']
        report = self.report()
        self.assertEqual(['SUS-01'], [r['id'] for r in report['buckets'][view.BUCKETS[1]]])

    def test_recorded_passes_are_explicitly_unvalidated_and_never_approve(self):
        for row in self.record['rows']:
            row['status'] = 'PASS'
        report = self.report()
        self.assertEqual({'PASS': 275}, report['recorded_status_counts'])
        self.assertEqual(0, sum(len(rows) for rows in report['buckets'].values()))
        self.assertIn('not validated proof', report['notice'])
        self.assertNotIn('decision', report)

    def test_omitted_duplicate_unknown_or_wrong_snapshot_cannot_shrink_the_queue(self):
        original = copy.deepcopy(self.record)
        for mutation in ('missing', 'duplicate', 'unknown', 'fingerprint'):
            with self.subTest(mutation=mutation):
                self.record = copy.deepcopy(original)
                if mutation == 'missing': self.record['rows'].pop()
                elif mutation == 'duplicate': self.record['rows'][-1] = copy.deepcopy(self.record['rows'][0])
                elif mutation == 'unknown': self.record['rows'][-1]['id'] = 'UNKNOWN-99'
                else: self.record['checklist_sha256'] = '0'*64
                with self.assertRaises(ValueError): self.report()

    def test_na_cannot_hide_unconditional_or_contracted_work(self):
        for key in ('SPD-01', 'BACK-01'):
            with self.subTest(key=key):
                self.record = gate.template(CHECKLIST)
                self.row(key).update(status='N/A', applicable=False, reason='Absent', predicate='Observed absence')
                if key == 'BACK-01': self.record['release']['required_rows'] = [key]
                with self.assertRaises(ValueError): self.report()

    def test_overdue_work_is_flagged_and_input_is_preserved(self):
        self.row('SUS-01').update(owner='Operator', reason='Optional review', next_action='Reassess',
                                  review_by='2026-10-07T00:00:00Z')
        original = copy.deepcopy(self.record)
        report = self.report()
        row = next(r for r in report['buckets'][view.BUCKETS[-1]] if r['id'] == 'SUS-01')
        self.assertTrue(any('overdue' in issue for issue in row['record_issues']))
        self.assertEqual(original, self.record)

    def test_unmapped_bundle_group_is_rejected_and_diamond_timing_cannot_defer_it(self):
        with tempfile.TemporaryDirectory() as directory:
            tiers = Path(directory)/'tiers.json'
            register = gate.read_record(TIERS)
            register['rows'][0]['group'] = 'unmapped'
            tiers.write_text(json.dumps(register))
            with self.assertRaises(ValueError): self.report(tiers=tiers)
            register = gate.read_record(TIERS)
            next(r for r in register['rows'] if r['id'] == 'SEC-03')['timing'] = 'postlaunch'
            tiers.write_text(json.dumps(register))
            self.assertIn('SEC-03', {r['id'] for r in self.report(tiers=tiers)['buckets'][view.BUCKETS[0]]})

    def test_markdown_cannot_create_links_or_rows_from_record_text(self):
        self.row('SEC-01')['owner'] = '[click](javascript:bad) | <script>\n# injected'
        text = view.markdown(self.report())
        self.assertNotIn('[click]', text)
        self.assertNotIn('<script>', text)
        self.assertNotIn('\n# injected', text)

    def test_cli_needs_no_network_and_never_writes_its_input(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'release.json'
            path.write_text(json.dumps(self.record))
            before = path.read_bytes()
            result = subprocess.run([sys.executable, str(ROOT/'scripts/release_queue.py'), str(path),
                                     '--format', 'json'], capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertTrue(json.loads(result.stdout)['advisory_only'])
            self.assertEqual(before, path.read_bytes())
            path.write_text('{"rows":[],"rows":[]}')
            result = subprocess.run([sys.executable, str(ROOT/'scripts/release_queue.py'), str(path)],
                                    capture_output=True, text=True)
            self.assertEqual(1, result.returncode)
            self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
