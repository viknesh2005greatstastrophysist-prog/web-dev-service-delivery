#!/usr/bin/env python3
"""Validate release evidence integrity and readiness, not the truth of test claims.

Python 3.9+, standard library only. See docs/RELEASE_EVIDENCE.md.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import socket
from urllib.parse import urlsplit
import ipaddress

STATUSES = {'PASS', 'FAIL', 'N/A', 'FIDELITY-EXCEPTION', 'AWAITING-DEPLOY',
            'OWNER-CONFIRM', 'NOT_RUN', 'UNAVAILABLE'}
PHASES = ('handover', 'launch', 'gold')
HEX64 = re.compile(r'[a-f0-9]{64}')
REVISION = re.compile(r'(?:[a-f0-9]{40}|[a-f0-9]{64})')
ROW = re.compile(r'^\| ([A-Z][A-Z0-9]*-\d{2}) \| .+ \| .+ \| ([GRC](?:-[LO])?) \|$')


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def catalogue(path):
    rows = {}
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not re.match(r'^\| [A-Z][A-Z0-9]*-\d', line):
            continue
        match = ROW.fullmatch(line)
        if not match:
            raise ValueError(f'malformed checklist row at line {number}')
        row_id, classification = match.groups()
        if row_id in rows:
            raise ValueError(f'duplicate checklist ID: {row_id}')
        rows[row_id] = classification
    if not rows:
        raise ValueError('checklist contains no rows')
    return rows


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key: {key}')
        result[key] = value
    return result


def read_record(path):
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_object)


def meaningful(value):
    return isinstance(value, str) and bool(value.strip()) and value.strip().lower() not in {
        'todo', 'tbd', 'unknown', 'fill', '[fill]', 'placeholder', 'n/a'}


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError('timestamp must be a string')
    date = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if date.tzinfo is None:
        raise ValueError('timestamp requires timezone')
    return date


def public_https(url):
    try:
        parsed = urlsplit(url)
        host = (parsed.hostname or '').rstrip('.').casefold()
        parsed.port  # Reject malformed port syntax even though no HTTP connection is made.
        if parsed.scheme != 'https' or not host or parsed.username or parsed.password:
            return False
        if parsed.query or parsed.fragment or '%' in host or host == 'localhost' or host.endswith(('.localhost', '.local', '.test', '.invalid', '.example')):
            return False
        try:
            return ipaddress.ip_address(host).is_global
        except ValueError:
            return '.' in host
    except (ValueError, TypeError):
        return False


def resolve_addresses(host):
    return sorted({item[4][0] for item in socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)})


def global_destination(url, resolver):
    if not public_https(url):
        return False
    try:
        host = urlsplit(url).hostname.rstrip('.').casefold()
        addresses = resolver(host)
        return bool(addresses) and all(ipaddress.ip_address(address).is_global for address in addresses)
    except (OSError, ValueError, TypeError):
        return False


def template(checklist):
    return {
        'schema_version': 1,
        'checklist_sha256': sha256(checklist),
        'release': {'revision': '', 'artifact_sha256': '', 'build_id': '',
                    'built_at': '', 'url': '', 'environment': 'local',
                    'a11y': 'on', 'content_status': 'CONTENT-PENDING',
                    'routes': [], 'states': [], 'viewports': []},
        'rows': [dict(id=key, applicable=True,
                      status='AWAITING-DEPLOY' if cls.endswith('-L') else
                      'OWNER-CONFIRM' if cls.endswith('-O') else 'NOT_RUN',
                      reason='Not yet verified', owner='', next_action='', review_by='',
                      verification='manual' if cls.endswith('-O') else 'automated',
                      tester='', checked_at='', release_revision='', artifact_sha256='',
                      build_id='', environment='local', url='', coverage=[], evidence=[])
                 for key, cls in catalogue(checklist).items()]
    }


def validate(record, checklist, evidence_root, phase='launch', now=None, resolver=resolve_addresses):
    errors, warnings = [], []
    now = now or datetime.now(timezone.utc)
    rowspec = catalogue(checklist)
    if not isinstance(record, dict):
        return {'decision': 'BLOCKED', 'errors': ['record must be an object'], 'warnings': []}
    if type(record.get('schema_version')) is not int or record.get('schema_version') != 1:
        errors.append('schema_version must equal 1')
    if record.get('checklist_sha256') != sha256(checklist):
        errors.append('checklist fingerprint does not match the reviewed snapshot')
    release = record.get('release')
    if not isinstance(release, dict):
        release = {}
        errors.append('release must be an object')
    for key, pattern in [('revision', REVISION), ('artifact_sha256', HEX64)]:
        if not isinstance(release.get(key), str) or not pattern.fullmatch(release[key]):
            errors.append(f'release.{key} must be a full lowercase hash')
    if not meaningful(release.get('build_id')):
        errors.append('release.build_id is required')
    built_at = None
    try:
        built_at = timestamp(release.get('built_at'))
        if built_at > now:
            errors.append('release.built_at is in the future')
    except ValueError:
        errors.append('release.built_at must be an ISO timestamp with timezone')
    if release.get('environment') not in {'local', 'staging', 'production'}:
        errors.append('release.environment is invalid')
    if release.get('a11y') != 'on':
        errors.append('deployed artifact must enable accessibility fixes')
    if release.get('content_status') not in {'CLIENT-COMPLETE', 'CONTENT-PENDING'}:
        errors.append('release.content_status is invalid')
    for dimension in ('routes', 'states', 'viewports'):
        values = release.get(dimension)
        if not isinstance(values, list) or not values or not all(meaningful(v) for v in values) or len(values) != len(set(values)):
            errors.append(f'release.{dimension} needs a nonempty unique string inventory')
    destination_global = release.get('environment') == 'production' and global_destination(release.get('url'), resolver)
    if phase != 'handover':
        if not destination_global:
            errors.append('launch requires production HTTPS resolving only to global addresses; local, unresolved or mixed DNS is blocked')
        if release.get('content_status') != 'CLIENT-COMPLETE':
            errors.append('launch requires approved CLIENT-COMPLETE content')
    if not meaningful(release.get('url')):
        errors.append('release.url is required')
    entries = record.get('rows')
    if not isinstance(entries, list):
        entries = []
        errors.append('rows must be a list')
    ids = [entry.get('id') for entry in entries if isinstance(entry, dict) and isinstance(entry.get('id'), str)]
    duplicates = sorted(k for k, count in Counter(ids).items() if count > 1)
    if duplicates:
        errors.append('duplicate row IDs: ' + ', '.join(duplicates))
    missing = sorted(set(rowspec) - set(ids))
    unknown = sorted(set(ids) - set(rowspec))
    if missing:
        errors.append('missing row IDs: ' + ', '.join(missing))
    if unknown:
        errors.append('unknown row IDs: ' + ', '.join(unknown))
    evidence_root = evidence_root.resolve()
    counts = Counter()
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get('id'), str):
            errors.append('each row must be an object with a string ID')
            continue
        key = entry['id']
        if key not in rowspec:
            continue
        cls = rowspec[key]
        status = entry.get('status')
        if not isinstance(status, str) or status not in STATUSES:
            errors.append(f'{key}: unknown status')
            continue
        counts[status] += 1
        applicable = entry.get('applicable')
        if type(applicable) is not bool:
            errors.append(f'{key}: applicable must be boolean')
        if status == 'N/A':
            if applicable is not False or (cls.startswith('G') and key != 'LEG-07'):
                errors.append(f'{key}: N/A cannot waive an unconditional required row')
            if not meaningful(entry.get('reason')) or not meaningful(entry.get('predicate')):
                errors.append(f'{key}: N/A needs an observed absence predicate and reason')
        elif applicable is not True:
            errors.append(f'{key}: non-applicable rows must use N/A')
        if status == 'AWAITING-DEPLOY' and not cls.endswith('-L'):
            errors.append(f'{key}: AWAITING-DEPLOY only applies to live rows')
        if status == 'OWNER-CONFIRM' and not cls.endswith('-O'):
            errors.append(f'{key}: OWNER-CONFIRM only applies to owner rows')
        if status == 'UNAVAILABLE' and key != 'SPD-21':
            errors.append(f'{key}: UNAVAILABLE only applies to field-data row SPD-21')
        resolved = status in {'PASS', 'N/A'}
        pending_allowed = phase == 'handover' and (
            (cls.endswith('-L') and status == 'AWAITING-DEPLOY') or
            (cls.endswith('-O') and status == 'OWNER-CONFIRM'))
        if not resolved:
            for field in ('reason', 'owner', 'next_action'):
                if not meaningful(entry.get(field)):
                    errors.append(f'{key}: unresolved result needs {field}')
            try:
                review_date = timestamp(entry.get('review_by'))
                if review_date < now:
                    errors.append(f'{key}: follow-up date is overdue')
            except ValueError:
                errors.append(f'{key}: unresolved result needs a review_by timestamp')
            if not pending_allowed and (phase == 'gold' or not cls.startswith('R')):
                errors.append(f'{key}: {status} blocks {phase}')
            else:
                warnings.append(f'{key}: {status}, follow-up required')
        # Every claimed observation must be bound to this artifact, even FAIL or N/A.
        observed = status not in {'AWAITING-DEPLOY', 'OWNER-CONFIRM', 'NOT_RUN'}
        if observed:
            for field, reference in [('release_revision', 'revision'), ('artifact_sha256', 'artifact_sha256'), ('build_id', 'build_id')]:
                if not meaningful(entry.get(field)) or entry.get(field) != release.get(reference):
                    errors.append(f'{key}: wrong or missing {field}')
            if entry.get('environment') != release.get('environment') or entry.get('url') != release.get('url'):
                errors.append(f'{key}: observation environment/URL does not match release')
            try:
                observed_at = timestamp(entry.get('checked_at'))
                if observed_at > now or (built_at and observed_at < built_at):
                    errors.append(f'{key}: evidence predates build or is in the future')
            except ValueError:
                errors.append(f'{key}: checked_at must include timezone')
            if not meaningful(entry.get('tester')):
                errors.append(f'{key}: named tester required')
            if entry.get('verification') not in {'automated', 'manual'}:
                errors.append(f'{key}: verification must be automated or manual')
            if cls.endswith('-O') and entry.get('verification') != 'manual':
                errors.append(f'{key}: owner evidence requires manual verification')
            if cls.endswith('-L') and status == 'PASS' and (not destination_global or entry.get('url') != release.get('url')):
                errors.append(f'{key}: live PASS requires production HTTPS evidence')
            coverage = entry.get('coverage')
            if not isinstance(coverage, list) or not coverage or not all(meaningful(v) for v in coverage):
                errors.append(f'{key}: explicit coverage is required')
            evidence = entry.get('evidence')
            if not isinstance(evidence, list) or not evidence:
                errors.append(f'{key}: nonempty saved evidence required')
                continue
            for item in evidence:
                if not isinstance(item, dict) or not meaningful(item.get('path')):
                    errors.append(f'{key}: invalid evidence reference')
                    continue
                relative = Path(item['path'])
                target = (evidence_root / relative).resolve()
                if relative.is_absolute() or evidence_root not in target.parents:
                    errors.append(f'{key}: evidence path escapes evidence root')
                    continue
                if not target.is_file() or target.stat().st_size == 0:
                    errors.append(f'{key}: evidence file missing or empty: {relative}')
                elif not isinstance(item.get('sha256'), str) or item['sha256'] != sha256(target):
                    errors.append(f'{key}: evidence hash mismatch: {relative}')
    decision = 'BLOCKED' if errors else {'handover': 'HANDOVER-READY', 'launch': 'LAUNCH-EVIDENCE-COMPLETE', 'gold': 'GOLD-EVIDENCE-COMPLETE'}[phase]
    return {'decision': decision, 'phase': phase, 'counts': dict(sorted(counts.items())),
            'errors': errors, 'warnings': warnings,
            'limitation': 'Validates evidence records and file integrity only. Human review must verify test truth, applicability, coverage and actual deployed artifact identity.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', type=Path)
    parser.add_argument('--checklist', type=Path, required=True)
    parser.add_argument('--evidence-root', type=Path)
    parser.add_argument('--phase', choices=PHASES, default='launch')
    parser.add_argument('--init', action='store_true')
    args = parser.parse_args()
    try:
        if args.init:
            with args.record.open('x', encoding='utf-8') as handle:
                json.dump(template(args.checklist), handle, indent=2)
                handle.write('\n')
            print('Created unverified release record. Fill from actual evidence; no readiness claimed.')
            return 0
        result = validate(read_record(args.record), args.checklist,
                          args.evidence_root or args.record.parent, args.phase)
        print(json.dumps(result, indent=2))
        return 1 if result['errors'] else 0
    except (OSError, ValueError, TypeError) as error:
        print(json.dumps({'decision': 'BLOCKED', 'errors': [str(error)]}, indent=2))
        return 1


if __name__ == '__main__':
    sys.exit(main())
