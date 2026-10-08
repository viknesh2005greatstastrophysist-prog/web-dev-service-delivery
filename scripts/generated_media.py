#!/usr/bin/env python3
"""Validate original generated media, or prepare a content-sync update without writes.

The output is a proposed site/manifest pair. The app's content:sync commits it only
after its own build and render checks pass. This tool never generates or certifies images.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys


def text(value):
    return isinstance(value, str) and bool(value.strip())


def fingerprint(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def file_record(root, item):
    if not isinstance(item, dict) or not text(item.get('path')):
        raise ValueError('file requires path and sha256')
    path = (root / item['path']).resolve()
    if Path(item['path']).is_absolute() or not path.is_relative_to(root.resolve()):
        raise ValueError('file escapes its declared root')
    if not path.is_file() or fingerprint(path) != item.get('sha256'):
        raise ValueError(f"missing or changed file: {item['path']}")
    return path


def entries(app, registry, required_model=None):
    if not isinstance(registry, dict) or type(registry.get('schema_version')) is not int or registry['schema_version'] != 1:
        raise ValueError('generated registry requires schema_version 1')
    assets = registry.get('assets')
    if not isinstance(assets, list) or not all(isinstance(a, dict) for a in assets):
        raise ValueError('assets must be a list of objects')
    seen = set()
    normalized = {}
    for asset in assets:
        slot = asset.get('slot')
        if not text(slot) or slot in seen:
            raise ValueError('generated slots must be unique nonempty strings')
        seen.add(slot)
        for field in ('provider', 'prompt', 'requested_model', 'intended_use'):
            if not text(asset.get(field)):
                raise ValueError(f'{slot}: missing {field}')
        if asset['intended_use'] != 'concept-illustration':
            raise ValueError(f'{slot}: generated imagery is not verified client work')
        brief = asset.get('brief')
        fields = ('subject', 'camera', 'lighting', 'materials', 'composition', 'negative_space', 'mobile_crop')
        if not isinstance(brief, dict) or not all(text(brief.get(k)) for k in fields):
            raise ValueError(f'{slot}: incomplete scene brief')
        original = file_record(app, asset.get('original'))
        if original.is_relative_to((app / 'public').resolve()):
            raise ValueError(f'{slot}: original must stay outside public assets')
        observed = asset.get('observed_model')
        if observed is not None:
            if not text(observed):
                raise ValueError(f'{slot}: invalid observed_model')
            receipt = json.loads(file_record(app, asset.get('model_evidence')).read_text())
            if not isinstance(receipt, dict) or receipt.get('model') != observed:
                raise ValueError(f'{slot}: receipt contradicts observed_model or supplies no model')
        if required_model and observed != required_model:
            raise ValueError(f'{slot}: required model unverified or different; not a harm finding')
        variants = asset.get('derivatives')
        if not isinstance(variants, list) or not variants:
            raise ValueError(f'{slot}: responsive derivatives required')
        paths, profiles = set(), set()
        for variant in variants:
            path = file_record(app, variant)
            public = (app / 'public').resolve()
            if not path.is_relative_to(public) or variant.get('url') != '/' + path.relative_to(public).as_posix():
                raise ValueError(f'{slot}: derivative URL must resolve to its hashed public file')
            if variant['path'] in paths or variant.get('profile') not in {'desktop', 'mobile'}:
                raise ValueError(f'{slot}: duplicate path or invalid derivative profile')
            paths.add(variant['path']); profiles.add(variant['profile'])
            if (type(variant.get('width')) is not int or type(variant.get('height')) is not int or
                    min(variant['width'], variant['height']) <= 0 or not text(variant.get('crop')) or
                    not text(variant.get('url'))):
                raise ValueError(f'{slot}: derivative requires dimensions, crop and URL')
        if profiles != {'desktop', 'mobile'}:
            raise ValueError(f'{slot}: desktop and mobile derivatives required')
        # A public manifest needs lineage hashes, never the prompt or provider response.
        normalized[slot] = {'slot': slot, 'source': 'generated',
                            'original_sha256': asset['original']['sha256'],
                            'derivatives': copy.deepcopy(variants)}
    return normalized


def active_registry(site, registry):
    if (not isinstance(registry, dict) or not isinstance(registry.get('assets'), list) or
            not all(isinstance(a, dict) for a in registry['assets'])):
        raise ValueError('registry assets must be objects')
    retired = {a.get('slot') for a in registry['assets']
               if isinstance(site['slots'].get(a.get('slot')), dict) and
               site['slots'][a['slot']].get('source') == 'client'}
    return dict(registry, assets=[a for a in registry['assets'] if a.get('slot') not in retired]), retired


def prepare_sync(app, registry, site, manifest, required_model=None):
    """Pure preparation: preserve unsupplied slots and client media, fail before writes."""
    proposed, output = copy.deepcopy(site), copy.deepcopy(manifest)
    if not isinstance(proposed, dict) or not isinstance(proposed.get('slots'), dict):
        raise ValueError('content/site.json must have keyed slots')
    if not isinstance(output, dict) or not isinstance(output.get('images'), list):
        raise ValueError('image manifest must have an images list')
    active, retired = active_registry(proposed, registry)
    incoming = entries(app, active, required_model)
    changed = [key for key in sorted(retired) if any(isinstance(a, dict) and a.get('slot') == key and
                                                    a.get('source') == 'generated' for a in output['images'])]
    output['images'] = [a for a in output['images'] if not (isinstance(a, dict) and a.get('slot') in retired and
                                                         a.get('source') == 'generated')]
    for key, asset in incoming.items():
        slot = proposed['slots'].get(key)
        if not isinstance(slot, dict) or slot.get('kind') != 'image':
            raise ValueError(f'{key}: generated entry needs an existing image slot')
        if slot.get('source') == 'client':
            continue
        value = next(v['url'] for v in asset['derivatives'] if v['profile'] == 'desktop')
        replacement = dict(slot, source='generated', placeholder=False, value=value)
        prior = [a for a in output['images'] if isinstance(a, dict) and a.get('slot') == key]
        if slot != replacement or prior != [asset]:
            changed.append(key)
        proposed['slots'][key] = replacement
        output['images'] = [a for a in output['images'] if not isinstance(a, dict) or a.get('slot') != key] + [asset]
    return {'site': proposed, 'manifest': output, 'changed_slots': changed,
            'notice': 'Prepared only. Build and render checks must pass before content:sync commits this pair.'}


def validate(app, registry, site, manifest, required_model=None):
    if not isinstance(site, dict) or not isinstance(site.get('slots'), dict):
        raise ValueError('content/site.json must have keyed slots')
    if not isinstance(manifest, dict) or not isinstance(manifest.get('images'), list):
        raise ValueError('image manifest must have an images list')
    active, _ = active_registry(site, registry)
    expected = entries(app, active, required_model)
    generated = {key for key, value in site['slots'].items()
                 if isinstance(value, dict) and value.get('source') == 'generated'}
    if generated != set(expected):
        raise ValueError('generated slots and private registry must agree exactly')
    public = [a for a in manifest['images'] if isinstance(a, dict) and a.get('source') == 'generated']
    if len(public) != len(expected) or {a.get('slot') for a in public} != generated:
        raise ValueError('generated manifest inventory mismatch')
    for key, asset in expected.items():
        slot = site['slots'][key]
        if slot.get('kind') != 'image' or slot.get('placeholder') is not False or slot.get('value') not in {v['url'] for v in asset['derivatives']}:
            raise ValueError(f'{key}: generated slot uses an untracked value or placeholder')
        if next(a for a in public if a['slot'] == key) != asset:
            raise ValueError(f'{key}: generated manifest differs from verified lineage')
    return {'generated_slots': sorted(generated), 'recorded_model_matches_requirement': bool(required_model and generated),
            'notice': 'Hash and declared metadata validation only; not proof of provider authenticity, image dimensions, rights or visual quality.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('app', type=Path)
    parser.add_argument('registry', type=Path)
    parser.add_argument('--required-model')
    parser.add_argument('--prepare-sync', action='store_true')
    args = parser.parse_args()
    try:
        registry = json.loads(args.registry.read_text())
        site = json.loads((args.app/'content/site.json').read_text())
        manifest = json.loads((args.app/'content/image-manifest.json').read_text())
        function = prepare_sync if args.prepare_sync else validate
        result = function(args.app, registry, site, manifest, args.required_model)
        print(json.dumps(result, indent=2))
    except (OSError, ValueError, TypeError, KeyError, AttributeError, RecursionError) as error:
        print(f'Generated media incomplete: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
