#!/usr/bin/env python3
"""Check a pinned sample contract before expansion; never authorize launch."""
import argparse
import json
from pathlib import Path
import sys
from urllib.parse import urlparse
from generated_media import file_record, fingerprint, text, validate as validate_media


def artifact_record(root, item):
    manifest = json.loads(file_record(root, item).read_text())
    files = manifest.get('files') if isinstance(manifest, dict) else None
    if not isinstance(files, list) or not files:
        raise ValueError('artifact manifest needs a nonempty files inventory')
    paths = []
    for entry in files:
        paths.append(file_record(root, entry))
    if len(set(paths)) != len(paths):
        raise ValueError('artifact manifest contains duplicate files')


def gate(contract_path, record, root, phase, pinned_sha256, app=None):
    if fingerprint(contract_path) != pinned_sha256:
        raise ValueError('acceptance contract changed from the pre-build pin')
    contract = json.loads(contract_path.read_text())
    for obj in (contract, record):
        if not isinstance(obj, dict) or type(obj.get('schema_version')) is not int or obj['schema_version'] != 1:
            raise ValueError('contract and record require schema_version 1')
    if record.get('contract_sha256') != pinned_sha256 or phase not in {'reference', 'adapted'}:
        raise ValueError('contract fingerprint or phase mismatch')
    samples, anchors, checks = contract.get('samples'), contract.get('anchors'), record.get('checks')
    if not all(isinstance(items, list) and items and all(isinstance(i, dict) for i in items)
               for items in (samples, anchors, checks)):
        raise ValueError('nonempty samples, anchors and checks required')
    ids = [s.get('id') for s in samples]
    if not all(text(i) for i in ids) or len(set(ids)) != len(ids):
        raise ValueError('sample IDs must be unique')
    contexts = set()
    captures = {}
    for sample in samples:
        viewports, states = sample.get('viewports'), sample.get('states')
        if (not text(sample.get('route')) or not text(sample.get('source_url')) or not text(sample.get('captured_at')) or
                not isinstance(viewports, list) or not viewports or
                not all(isinstance(v, list) and len(v) == 2 and all(type(n) is int and n > 0 for n in v) for v in viewports) or
                not any(v[0] <= 480 for v in viewports) or not any(v[0] >= 1024 for v in viewports) or
                len({tuple(v) for v in viewports}) != len(viewports) or
                not isinstance(states, list) or not states or not all(text(s) for s in states) or
                len(set(states)) != len(states) or 'rest' not in states or type(sample.get('motion')) is not bool):
            raise ValueError('sample needs source, desktop/mobile, distinct states and explicit motion')
        url = urlparse(sample['source_url'])
        if (url.scheme not in {'http', 'https'} or not url.hostname or url.username or url.password or
                any(c.isspace() for c in sample['source_url'])):
            raise ValueError('source_url must be an absolute HTTP(S) URL without credentials')
        capture = json.loads(file_record(root, sample.get('capture')).read_text())
        if (not isinstance(capture, dict) or capture.get('source_url') != sample['source_url'] or
                capture.get('captured_at') != sample['captured_at'] or
                not isinstance(capture.get('files'), list) or not capture['files']):
            raise ValueError('capture manifest must match the sample URL/date and list files')
        captures[sample['id']] = set()
        for entry in capture['files']:
            file_record(root, entry)
            captures[sample['id']].add((entry['path'], entry['sha256']))
        if sample['motion'] and not {'signature-motion', 'reduced-motion'} <= set(states):
            raise ValueError('motion sample lacks signature/reduced-motion coverage')
        contexts.update((sample['id'], tuple(v), state) for v in viewports for state in states)
    anchor_ids, coverage = set(), set()
    for anchor in anchors:
        key, viewport = anchor.get('id'), anchor.get('viewport')
        if not text(key) or key in anchor_ids or not isinstance(viewport, list):
            raise ValueError('invalid/duplicate anchor')
        context = (anchor.get('sample'), tuple(viewport), anchor.get('state'))
        if context not in contexts or not all(text(anchor.get(k)) for k in ('criterion', 'method', 'tolerance', 'kind')):
            raise ValueError(f'{key}: undeclared context or missing acceptance method')
        dependencies = anchor.get('dependencies')
        if not isinstance(dependencies, list) or not dependencies or not all(text(d) for d in dependencies):
            raise ValueError(f'{key}: dependencies required')
        if anchor['state'] in {'signature-motion', 'reduced-motion'} and anchor['kind'] != 'motion':
            raise ValueError(f'{key}: motion state requires motion evidence')
        file_record(root, anchor.get('source'))
        if (anchor['source']['path'], anchor['source']['sha256']) not in captures[anchor['sample']]:
            raise ValueError('anchor source is absent from its sample capture manifest')
        anchor_ids.add(key); coverage.add(context)
    if coverage != contexts:
        raise ValueError('required sample/state/viewport coverage missing from anchors')
    if any(c.get('phase') not in {'reference', 'adapted'} or not text(c.get('id')) or c['id'] not in anchor_ids for c in checks):
        raise ValueError('unknown phase or anchor in checks; no ignored results')
    artifacts = record.get('artifacts')
    phases = ['reference'] if phase == 'reference' else ['reference', 'adapted']
    if not isinstance(artifacts, dict):
        raise ValueError('artifact identities required')
    blockers = []
    for current in phases:
        artifact_record(root, artifacts.get(current))
        selected = [c for c in checks if c.get('phase') == current]
        keys = [c.get('id') for c in selected]
        if not all(text(k) for k in keys) or len(keys) != len(anchor_ids) or set(keys) != anchor_ids:
            raise ValueError(f'{current}: missing, duplicate or unknown checks')
        for item in selected:
            if item.get('artifact_sha256') != artifacts[current]['sha256']:
                raise ValueError(f"{item['id']}: stale {current} artifact evidence")
            if item.get('status') not in {'PASS', 'FAIL', 'NOT_RUN'}:
                raise ValueError('sample results must be PASS, FAIL or NOT_RUN')
            if item['status'] != 'PASS':
                if not all(text(item.get(k)) for k in ('reason', 'owner', 'next_action')):
                    raise ValueError('unresolved result needs reason, owner and next action')
                blockers.append(f"{current}:{item['id']}:{item['status']}")
            else:
                evidence = item.get('evidence')
                if not isinstance(evidence, list) or not evidence:
                    raise ValueError('PASS requires hashed evidence')
                for source in evidence:
                    file_record(root, source)
    if phase == 'adapted':
        acceptance = record.get('design_acceptance')
        if not isinstance(acceptance, list) or len(acceptance) != len(ids) or {a.get('sample') for a in acceptance if isinstance(a, dict)} != set(ids):
            raise ValueError('every sample needs its own design acceptance')
        for decision in acceptance:
            if (decision.get('artifact_sha256') != artifacts['adapted']['sha256'] or
                    not text(decision.get('reviewer'))):
                raise ValueError('design acceptance is stale or lacks reviewer')
            if decision.get('status') != 'ACCEPTED':
                blockers.append(f"design:{decision['sample']}:unaccepted")
            else:
                file_record(root, decision.get('evidence'))
        slots = contract.get('generated_slots')
        if not isinstance(slots, list) or not all(text(s) for s in slots) or len(set(slots)) != len(slots):
            raise ValueError('generated_slots must be explicit and unique, or []')
        model = contract.get('required_model')
        if model is not None and not text(model):
            raise ValueError('required_model must be a model ID or null')
        if app is None:
            raise ValueError('adapted gate needs --app to inspect generated inventory, including an empty declaration')
        site = json.loads((app/'content/site.json').read_text())
        manifest = json.loads((app/'content/image-manifest.json').read_text())
        registry = {'schema_version': 1, 'assets': []}
        if record.get('generated_registry') is not None:
            registry_path = file_record(root, record.get('generated_registry'))
            registry = json.loads(registry_path.read_text())
        result = validate_media(app, registry, site, manifest, model)
        if set(slots) != set(result['generated_slots']):
            raise ValueError('declared generated slots must match the final app exactly')
    return {'phase': phase, 'stage_complete': not blockers, 'blockers': blockers,
            'record_complete_for_samples': ids if phase == 'adapted' and not blockers else [],
            'production_clearance': False,
            'notice': 'Validates declared coverage and hashed records, not the truth of measurements. No whole-site, model-authenticity or launch certification.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('contract', type=Path); parser.add_argument('record', type=Path)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--contract-sha256', required=True)
    parser.add_argument('--phase', choices=('reference', 'adapted'), required=True)
    parser.add_argument('--app', type=Path)
    args = parser.parse_args()
    try:
        result = gate(args.contract, json.loads(args.record.read_text()), args.root, args.phase, args.contract_sha256, args.app)
        print(json.dumps(result, indent=2))
    except (OSError, ValueError, TypeError, KeyError, AttributeError, RecursionError) as error:
        print(f'Clone stage incomplete: {error}', file=sys.stderr); return 1
    return 0 if result['stage_complete'] else 1


if __name__ == '__main__':
    sys.exit(main())
