"""Mutation tests prove the structural checker rejects document regressions."""
from pathlib import Path
import shutil
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
        path.write_text(path.read_text().replace('(262 rows, 18 sections)', '(254 rows, 18 sections)'))
        self.assertRejected('README row count matches catalogue')

    def test_broken_entry_point_link_fails(self):
        path = self.root/'README.md'
        path.write_text(path.read_text()+'\n[Missing](docs/does-not-exist.md)\n')
        self.assertRejected('active Markdown file links resolve')


if __name__ == '__main__':
    unittest.main()
