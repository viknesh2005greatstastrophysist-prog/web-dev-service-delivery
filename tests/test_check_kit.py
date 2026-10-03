"""Mutation tests prove the structural checker rejects document regressions."""
from pathlib import Path
import shutil
import json
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class KitConsistencyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('checklist', 'prompt', 'docs', 'scripts', 'tests', 'examples'):
            shutil.copytree(ROOT/name, self.root/name, ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copy(ROOT/'README.md', self.root/'README.md')
        (self.root/'skills').symlink_to(ROOT/'skills', target_is_directory=True)
        (self.root/'vendor').symlink_to(ROOT/'vendor', target_is_directory=True)

    def run_check(self):
        return subprocess.run([sys.executable, str(ROOT/'scripts/check-kit.py'), '--root', str(self.root)], capture_output=True, text=True)

    def assertRejected(self, marker):
        result = self.run_check()
        self.assertEqual(1, result.returncode, result.stdout+result.stderr)
        self.assertNotIn('Traceback', result.stderr)
        self.assertIn(marker, result.stdout)

    def test_valid_kit(self):
        result = self.run_check()
        self.assertEqual(0, result.returncode, result.stdout+result.stderr)

    def test_silent_row_removal_fails_inventory(self):
        path = self.root/'checklist/PRODUCTION_CHECKLIST_clone_swap.md'
        path.write_text('\n'.join(l for l in path.read_text().splitlines() if not l.startswith('| TYP-24 |'))+'\n')
        self.assertRejected('IDs exactly match stable inventory')

    def test_malformed_row_fails_without_traceback(self):
        path = self.root/'checklist/PRODUCTION_CHECKLIST_clone_swap.md'
        path.write_text(path.read_text().replace('| SPD-01 |', '| SPD-01 malformed |', 1))
        self.assertRejected('strict row grammar')

    def test_missing_finish_section_fails_without_traceback(self):
        path = self.root/'prompt/PROMPT_awwwards_clone_swap_v6.md'
        path.write_text(path.read_text().replace('## Finish', '## End'))
        self.assertRejected('required section exists: ## Finish')

    def test_stale_document_count_fails(self):
        path = self.root/'README.md'
        path.write_text(path.read_text().replace('(275 rows, 18 sections)', '(254 rows, 18 sections)'))
        self.assertRejected('README row count matches catalogue')

    def test_broken_entry_point_link_fails(self):
        path = self.root/'README.md'
        path.write_text(path.read_text()+'\n[Missing](docs/does-not-exist.md)\n')
        self.assertRejected('active Markdown file links resolve')

    def mutate_sources(self, mutate):
        path = self.root/'docs/reviews/instagram-addon-2026-10-03/lessons.json'
        record = json.loads(path.read_text())
        mutate(record)
        path.write_text(json.dumps(record))

    def test_missing_addon_is_rejected_without_traceback(self):
        (self.root/'checklist/VIDEO_LESSONS_ADDON.md').unlink()
        self.assertRejected('kit file exists: checklist/VIDEO_LESSONS_ADDON.md')

    def test_missing_supplied_clip_is_rejected(self):
        self.mutate_sources(lambda r: r['sources'].pop())
        self.assertRejected('exactly nine supplied IDs')

    def test_dangling_video_row_is_rejected(self):
        self.mutate_sources(lambda r: r['sources'][0]['rows'].append('BACK-99'))
        self.assertRejected('every mapped row exists')

    def test_source_url_mismatch_is_rejected(self):
        self.mutate_sources(lambda r: r['sources'][0].update(url='https://www.instagram.com/p/wrong/'))
        self.assertRejected('matching URLs')

    def test_malformed_provenance_is_rejected_without_traceback(self):
        path = self.root/'docs/reviews/instagram-addon-2026-10-03/lessons.json'
        path.write_text('{')
        self.assertRejected('readable provenance record')


    def test_missing_second_batch_carousel_is_rejected(self):
        path = self.root/'docs/reviews/instagram-batch2-2026-10-03/lessons.json'
        record = json.loads(path.read_text())
        record['sources'] = [x for x in record['sources'] if x['media_kind'] != 'carousel']
        path.write_text(json.dumps(record))
        self.assertRejected('all seven source IDs')

    def test_missing_carousel_slide_identity_is_rejected(self):
        path = self.root/'docs/reviews/instagram-batch2-2026-10-03/lessons.json'
        record = json.loads(path.read_text())
        next(x for x in record['sources'] if x['media_kind'] == 'carousel')['artifacts'].pop()
        path.write_text(json.dumps(record))
        self.assertRejected('media kinds and reviewed artifact identities')


if __name__ == '__main__':
    unittest.main()
