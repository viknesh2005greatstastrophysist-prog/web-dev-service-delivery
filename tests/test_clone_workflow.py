"""Adversarial fixtures for sample closure, stale files and generated-media sync.

Fixture bytes are synthetic. Passing them is not a website or image-generation test.
"""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from clone_gate import gate
from generated_media import entries, prepare_sync, validate


class CloneWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.file('source.txt', 'source capture fixture')
        self.capture = self.file('capture.json', json.dumps({'source_url': 'https://example.com',
                                                           'captured_at': '2026-10-08', 'files': [self.source]}))
        self.evidence = self.file('comparison.json', '{}')
        self.contract = {'schema_version': 1, 'generated_slots': [], 'required_model': None,
                         'samples': [{'id': 'home', 'route': '/', 'source_url': 'https://example.com',
                                      'captured_at': '2026-10-08', 'capture': self.capture,
                                      'viewports': [[1440, 900], [390, 844]],
                                      'states': ['rest'], 'motion': False}], 'anchors': []}
        for width, height in self.contract['samples'][0]['viewports']:
            self.contract['anchors'].append({'id': str(width), 'sample': 'home', 'viewport': [width, height],
                                            'state': 'rest', 'kind': 'layout', 'criterion': 'declared fixture bounds',
                                            'method': 'paired fixture observation', 'tolerance': 'fixed fixture bounds',
                                            'dependencies': ['layout'], 'source': self.source})
        self.record = {'schema_version': 1, 'artifacts': {}, 'checks': [], 'design_acceptance': []}
        for phase in ('reference', 'adapted'):
            file = self.file(f'{phase}.txt', phase)
            manifest = self.file(f'{phase}-manifest.json', json.dumps({'files': [file]}))
            self.record['artifacts'][phase] = manifest
            for anchor in self.contract['anchors']:
                self.record['checks'].append({'id': anchor['id'], 'phase': phase, 'status': 'PASS',
                                               'artifact_sha256': manifest['sha256'], 'evidence': [self.evidence]})
        self.record['design_acceptance'] = [{'sample': 'home', 'status': 'ACCEPTED', 'reviewer': 'fixture operator',
                                            'artifact_sha256': self.record['artifacts']['adapted']['sha256'],
                                            'evidence': self.evidence}]
        self.pin()
        self.asset = {'slot': 'hero', 'provider': 'fixture', 'prompt': 'fictional garden',
                      'requested_model': 'gpt-image-2', 'observed_model': None,
                      'intended_use': 'concept-illustration',
                      'brief': {k: 'fixture scene decision' for k in ('subject', 'camera', 'lighting', 'materials',
                                                                   'composition', 'negative_space', 'mobile_crop')},
                      'original': self.file('original.bin', 'synthetic fixture original'), 'derivatives': []}
        for profile in ('desktop', 'mobile'):
            self.asset['derivatives'].append(dict(self.file(f'public/{profile}.png', profile),
                                                  profile=profile, width=100, height=80,
                                                  crop='subject retained in fixture', url=f'/{profile}.png'))
        self.registry = {'schema_version': 1, 'assets': [self.asset]}
        self.site = {'slots': {'hero': {'kind': 'image', 'source': 'template', 'placeholder': True,
                                      'value': '/placeholder.png', 'alt': '', 'focal': [0.5, 0.5]},
                               'copy': {'kind': 'text', 'source': 'drafted', 'value': 'retain this'}}}
        self.manifest = {'images': [], 'icons': []}
        self.file('content/site.json', json.dumps(self.site))
        self.file('content/image-manifest.json', json.dumps(self.manifest))

    def file(self, name, value):
        path = self.root / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_text(value)
        return {'path': name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}

    def pin(self):
        self.path = self.root / 'contract.json'; self.path.write_text(json.dumps(self.contract))
        self.sha = hashlib.sha256(self.path.read_bytes()).hexdigest(); self.record['contract_sha256'] = self.sha

    def run_gate(self):
        return gate(self.path, self.record, self.root, 'adapted', self.sha, self.root)

    def test_complete_sample_never_grants_production_clearance(self):
        result = self.run_gate(); self.assertTrue(result['stage_complete']); self.assertFalse(result['production_clearance'])

    def test_contract_change_cannot_silently_widen_tolerance(self):
        self.contract['anchors'][0]['tolerance'] = 'widened'; self.path.write_text(json.dumps(self.contract))
        with self.assertRaisesRegex(ValueError, 'pre-build pin'): self.run_gate()

    def test_mobile_missing_from_anchor_plan_is_rejected(self):
        self.contract['anchors'].pop(); self.pin()
        with self.assertRaisesRegex(ValueError, 'coverage'): self.run_gate()

    def test_static_motion_claim_is_rejected(self):
        self.contract['samples'][0]['motion'] = True; self.pin()
        with self.assertRaisesRegex(ValueError, 'motion coverage'): self.run_gate()

    def test_missing_or_duplicate_comparison_is_rejected(self):
        for mutation in ('missing', 'duplicate'):
            with self.subTest(mutation=mutation):
                old = copy.deepcopy(self.record['checks'])
                if mutation == 'missing': self.record['checks'].pop()
                else: self.record['checks'].append(copy.deepcopy(self.record['checks'][-1]))
                with self.assertRaisesRegex(ValueError, 'checks'): self.run_gate()
                self.record['checks'] = old

    def test_not_run_with_disposition_blocks_expansion(self):
        self.record['checks'][-1].update(status='NOT_RUN', reason='not observed', owner='operator', next_action='capture mobile')
        self.assertFalse(self.run_gate()['stage_complete'])

    def test_extra_mislabeled_result_cannot_be_ignored(self):
        self.record['checks'].append(dict(self.record['checks'][-1], phase='misspelled', status='FAIL'))
        with self.assertRaisesRegex(ValueError, 'no ignored results'): self.run_gate()

    def test_changed_build_file_is_caught_even_if_manifest_was_not_rewritten(self):
        (self.root / 'adapted.txt').write_text('late change')
        with self.assertRaisesRegex(ValueError, 'changed file'): self.run_gate()

    def test_stale_comparison_or_design_acceptance_is_rejected(self):
        for target in (self.record['checks'][-1], self.record['design_acceptance'][0]):
            old = target['artifact_sha256']; target['artifact_sha256'] = '0' * 64
            with self.assertRaisesRegex(ValueError, 'stale'): self.run_gate()
            target['artifact_sha256'] = old

    def test_changed_source_capture_is_rejected(self):
        (self.root / 'source.txt').write_text('different source')
        with self.assertRaisesRegex(ValueError, 'changed file'): self.run_gate()

    def test_generated_sync_preserves_other_slots_and_is_idempotent(self):
        result = prepare_sync(self.root, self.registry, self.site, self.manifest)
        self.assertEqual(result['site']['slots']['copy'], self.site['slots']['copy'])
        second = prepare_sync(self.root, self.registry, result['site'], result['manifest'])
        self.assertEqual([], second['changed_slots'])
        self.assertEqual(result['site'], second['site'])
        self.assertEqual(result['manifest'], second['manifest'])
        self.assertFalse(validate(self.root, self.registry, result['site'], result['manifest'])['recorded_model_matches_requirement'])

    def test_client_media_wins_and_empty_sync_preserves_current_values(self):
        self.site['slots']['hero']['source'] = 'client'
        for registry in (self.registry, {'schema_version': 1, 'assets': []}):
            result = prepare_sync(self.root, registry, self.site, self.manifest)
            self.assertEqual(self.site, result['site']); self.assertEqual([], result['changed_slots'])
            self.assertEqual([], validate(self.root, registry, result['site'], result['manifest'])['generated_slots'])

    def test_client_replacement_retires_active_manifest_but_preserves_private_archive(self):
        generated = prepare_sync(self.root, self.registry, self.site, self.manifest)
        generated['site']['slots']['hero'].update(source='client', value='/real-client.png')
        result = prepare_sync(self.root, self.registry, generated['site'], generated['manifest'])
        self.assertEqual([], result['manifest']['images'])
        self.assertEqual('client', result['site']['slots']['hero']['source'])
        self.assertEqual([], validate(self.root, self.registry, result['site'], result['manifest'])['generated_slots'])

    def test_empty_declaration_cannot_hide_generated_app_inventory(self):
        result = prepare_sync(self.root, self.registry, self.site, self.manifest)
        self.file('content/site.json', json.dumps(result['site'])); self.file('content/image-manifest.json', json.dumps(result['manifest']))
        with self.assertRaisesRegex(ValueError, 'agree exactly'): self.run_gate()
        self.record['generated_registry'] = self.file('registry.json', json.dumps(self.registry))
        with self.assertRaisesRegex(ValueError, 'match the final app'): self.run_gate()

    def test_original_cannot_resolve_inside_public(self):
        self.asset['original'] = self.file('public/original.png', 'raw original')
        with self.assertRaisesRegex(ValueError, 'outside public'): entries(self.root, self.registry)

    def test_source_url_and_capture_metadata_are_bound(self):
        for field, value in [('source_url', 'not-a-url'), ('captured_at', 'different date')]:
            old = self.contract['samples'][0][field]; self.contract['samples'][0][field] = value; self.pin()
            with self.assertRaisesRegex(ValueError, 'HTTP|capture manifest'): self.run_gate()
            self.contract['samples'][0][field] = old; self.pin()
        self.contract['anchors'][0]['source'] = self.evidence; self.pin()
        with self.assertRaisesRegex(ValueError, 'sample capture'): self.run_gate()

    def test_deep_json_fails_both_clis_without_traceback(self):
        self.file('deep.json', '[' * 1100 + '0' + ']' * 1100)
        scripts = Path(__file__).resolve().parents[1] / 'scripts'
        commands = [[str(scripts/'generated_media.py'), str(self.root), str(self.root/'deep.json')],
                    [str(scripts/'clone_gate.py'), str(self.path), str(self.root/'deep.json'), '--root', str(self.root),
                     '--phase', 'adapted', '--contract-sha256', self.sha, '--app', str(self.root)]]
        for command in commands:
            with self.subTest(script=command[0]):
                result = subprocess.run([sys.executable] + command, capture_output=True, text=True)
                self.assertEqual(1, result.returncode); self.assertNotIn('Traceback', result.stderr)

    def test_malformed_sync_does_not_mutate_last_good_inputs(self):
        old = copy.deepcopy((self.site, self.manifest)); self.asset['derivatives'][0]['sha256'] = '0' * 64
        with self.assertRaises(ValueError): prepare_sync(self.root, self.registry, self.site, self.manifest)
        self.assertEqual(old, (self.site, self.manifest))

    def test_unknown_model_blocks_specific_model_claim_but_not_lineage(self):
        self.assertEqual(['hero'], list(entries(self.root, self.registry)))
        with self.assertRaisesRegex(ValueError, 'model unverified'): entries(self.root, self.registry, 'gpt-image-2')

    def test_receipt_must_match_observed_model(self):
        self.asset['observed_model'] = 'gpt-image-2'
        self.asset['model_evidence'] = self.file('receipt.json', '{"model":"other-model"}')
        with self.assertRaisesRegex(ValueError, 'contradicts'): entries(self.root, self.registry, 'gpt-image-2')
        self.asset['model_evidence'] = self.file('receipt.json', '{"model":"gpt-image-2"}')
        self.assertIn('hero', entries(self.root, self.registry, 'gpt-image-2'))

    def test_untracked_url_duplicate_slot_missing_crop_and_client_work_rejected(self):
        for field in ('url', 'duplicate', 'crop', 'use', 'escape', 'mobile'):
            registry = copy.deepcopy(self.registry); asset = registry['assets'][0]
            if field == 'url': asset['derivatives'][0]['url'] = 'https://reference.invalid/image.png'
            elif field == 'duplicate': registry['assets'].append(copy.deepcopy(asset))
            elif field == 'crop': asset['derivatives'][0]['crop'] = ''
            elif field == 'use': asset['intended_use'] = 'completed-client-project'
            elif field == 'escape': asset['original']['path'] = '../outside'
            else: asset['derivatives'].pop()
            with self.subTest(field=field), self.assertRaises(ValueError): entries(self.root, registry)

    def test_generated_inventory_cannot_be_omitted_or_mislabeled(self):
        result = prepare_sync(self.root, self.registry, self.site, self.manifest)
        with self.assertRaisesRegex(ValueError, 'agree exactly'):
            validate(self.root, {'schema_version': 1, 'assets': []}, result['site'], result['manifest'])
        result['site']['slots']['hero']['value'] = '/untracked.png'
        with self.assertRaisesRegex(ValueError, 'untracked'): validate(self.root, self.registry, result['site'], result['manifest'])

    def test_adapted_gate_checks_generated_registry_and_model(self):
        self.contract.update(generated_slots=['hero'], required_model='gpt-image-2'); self.pin()
        result = prepare_sync(self.root, self.registry, self.site, self.manifest)
        self.file('content/site.json', json.dumps(result['site'])); self.file('content/image-manifest.json', json.dumps(result['manifest']))
        self.record['generated_registry'] = self.file('registry.json', json.dumps(self.registry))
        with self.assertRaisesRegex(ValueError, 'model unverified'): self.run_gate()
        self.contract['required_model'] = None; self.pin()
        self.assertTrue(self.run_gate()['stage_complete'])

    def test_cli_malformed_record_fails_without_traceback(self):
        self.file('bad.json', '[]')
        script = Path(__file__).resolve().parents[1] / 'scripts/clone_gate.py'
        result = subprocess.run([sys.executable, str(script), str(self.path), str(self.root/'bad.json'),
                                 '--root', str(self.root), '--phase', 'adapted', '--contract-sha256', self.sha], capture_output=True, text=True)
        self.assertEqual(1, result.returncode); self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()
