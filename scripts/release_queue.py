#!/usr/bin/env python3
"""Show an advisory work queue from the full release record; never approve a release."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import html
import json
from pathlib import Path
import sys

from release_gate import STATUSES, meaningful, priority_policy, read_record, sha256, specifications, timestamp

ROOT = Path(__file__).resolve().parents[1]
BUCKETS = ('Diamond work', 'Contracted work due at this milestone', 'Owner inputs',
           'Final-domain checks', 'Gold quality work', 'Scheduled and optional follow-ups')


def work_metadata(checklist, tiers, bundles):
    """Require a complete matching catalogue; organizational metadata cannot omit rows."""
    specs = specifications(checklist)
    register, bundle_record = read_record(tiers), read_record(bundles)
    if not isinstance(register, dict) or not isinstance(bundle_record, dict):
        raise ValueError('metadata must be JSON objects')
    rows = register.get('rows')
    if (type(register.get('schema_version')) is not int or register.get('schema_version') != 1 or
            register.get('policy_version') != priority_policy(checklist.read_text()) or
            not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows) or
            [r.get('id') for r in rows] != list(specs)):
        raise ValueError('tier metadata must match the complete ordered checklist')
    groups = bundle_record.get('bundles')
    if (type(bundle_record.get('schema_version')) is not int or bundle_record.get('schema_version') != 1 or
            not isinstance(groups, list) or len(groups) != 6 or
            not all(isinstance(b, dict) and meaningful(b.get('id')) and meaningful(b.get('title')) and
                    isinstance(b.get('groups'), list) and b['groups'] and
                    all(meaningful(g) for g in b['groups']) for b in groups) or
            len({b['id'] for b in groups}) != 6):
        raise ValueError('six distinct work bundles with named groups are required')
    result = {}
    for row in rows:
        key = row['id']
        names = [b['title'] for b in groups if row.get('group') in b['groups']]
        if (row.get('tier') not in {'diamond', 'gold', 'silver', 'bronze'} or
                specs[key][1] != row['tier'].title() or
                row.get('timing') not in {'prelaunch', 'cutover', 'postlaunch', 'recurring'} or not names):
            raise ValueError(f'{key}: mismatched tier/timing or no work bundle')
        result[key] = dict(row, bundles=names)
    return specs, result


def queue(record, checklist, tiers, bundles, now=None):
    specs, metadata = work_metadata(checklist, tiers, bundles)
    now = now or datetime.now(timezone.utc)
    if not isinstance(record, dict) or type(record.get('schema_version')) is not int or record.get('schema_version') != 1:
        raise ValueError('release record must be a schema_version 1 object')
    if record.get('checklist_sha256') != sha256(checklist):
        raise ValueError('record checklist fingerprint mismatch; do not migrate historical verdicts')
    release, rows = record.get('release'), record.get('rows')
    if not isinstance(release, dict) or not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise ValueError('release object and full row list are required')
    ids = [r.get('id') for r in rows]
    if (not all(isinstance(k, str) for k in ids) or len(ids) != len(specs) or
            len(set(ids)) != len(ids) or set(ids) != set(specs)):
        raise ValueError('release rows must contain every checklist ID exactly once')
    contracted = release.get('required_rows')
    if (not isinstance(contracted, list) or not all(isinstance(k, str) and k in specs for k in contracted) or
            len(set(contracted)) != len(contracted)):
        raise ValueError('release.required_rows must list unique known IDs or []')
    buckets = {name: [] for name in BUCKETS}
    counts = Counter()
    for row in rows:
        key, status = row['id'], row.get('status')
        cls, tier = specs[key]
        if not isinstance(status, str) or status not in STATUSES or type(row.get('applicable')) is not bool:
            raise ValueError(f'{key}: invalid status or applicability')
        if status == 'N/A':
            if (row['applicable'] or key in contracted or (cls.startswith('G') and key != 'LEG-07') or
                    not meaningful(row.get('predicate')) or not meaningful(row.get('reason'))):
                raise ValueError(f'{key}: N/A cannot waive a required or unreviewed row')
        elif not row['applicable']:
            raise ValueError(f'{key}: non-applicable rows must use evidenced N/A')
        counts[status] += 1
        if status in {'PASS', 'N/A'}:
            continue  # Recorded observations only; validity/truth belongs to release_gate and review.
        if tier == 'Diamond':
            bucket = BUCKETS[0]
        elif key in contracted:
            bucket = BUCKETS[1]
        elif status == 'OWNER-CONFIRM':
            bucket = BUCKETS[2]
        elif status == 'AWAITING-DEPLOY':
            bucket = BUCKETS[3]
        elif tier == 'Gold' and metadata[key]['timing'] != 'postlaunch':
            bucket = BUCKETS[4]
        else:
            bucket = BUCKETS[5]
        issues = [f'missing {field}' for field in ('reason', 'owner', 'next_action') if not meaningful(row.get(field))]
        try:
            if timestamp(row.get('review_by')) < now:
                issues.append('overdue review; reassess and preserve history')
        except ValueError:
            issues.append('missing/invalid review date')
        buckets[bucket].append(dict(row, tier=tier, timing=metadata[key]['timing'],
                                    bundles=metadata[key]['bundles'], record_issues=issues))
    return {'advisory_only': True, 'total_rows': len(rows), 'recorded_status_counts': dict(sorted(counts.items())),
            'notice': 'Not a release decision. PASS/N/A are recorded claims, not validated proof. '
                      'Run release_gate.py and inspect evidence, approvals, configuration and new risks.',
            'buckets': buckets}


def cell(value):
    value = html.escape(' '.join(str(value).split()))
    for char in '\\|`[]*':
        value = value.replace(char, '\\' + char)
    return value


def markdown(report):
    lines = ['# Daily release work queue', '', report['notice'], '',
             f"Full record: {report['total_rows']} rows. Recorded counts: " +
             ', '.join(f'{key} {value}' for key, value in report['recorded_status_counts'].items()) + '.', '',
             'Compare the private project profile and new serious risks before following this queue. '
             'Later Gold observations still block full Gold. Timing never waives Diamond.']
    for name, rows in report['buckets'].items():
        lines += ['', f'## {name}', '', '| ID / tier / status | Work bundles | Owner / review date | Next action / record gaps |',
                  '|---|---|---|---|']
        for row in rows:
            values = [f"{row['id']} / {row['tier']} / {row['status']}", '; '.join(row['bundles']),
                      f"{row.get('owner', '')} / {row.get('review_by', '')}",
                      f"{row.get('next_action', '')} / {'; '.join(row['record_issues'])}"]
            lines.append('| ' + ' | '.join(cell(v) for v in values) + ' |')
        if not rows:
            lines.append('| No recorded open work in this bucket | | | |')
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', type=Path)
    parser.add_argument('--checklist', type=Path, default=ROOT/'checklist/PRODUCTION_CHECKLIST_clone_swap.md')
    parser.add_argument('--tiers', type=Path, default=ROOT/'checklist/tiers.json')
    parser.add_argument('--bundles', type=Path, default=ROOT/'checklist/bundles.json')
    parser.add_argument('--format', choices=('markdown', 'json'), default='markdown')
    args = parser.parse_args()
    try:
        report = queue(read_record(args.record), args.checklist, args.tiers, args.bundles)
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        print(f'Cannot generate advisory queue: {error}', file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2) if args.format == 'json' else markdown(report), end='\n' if args.format == 'json' else '')
    return 0  # Success means view generated, never permission to deploy.


if __name__ == '__main__':
    sys.exit(main())
