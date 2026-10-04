#!/usr/bin/env python3
"""Render the operating view from reviewed assignments; never classify by keyword."""
import json
from collections import Counter
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'checklist/PRODUCTION_CHECKLIST_clone_swap.md'
register = json.loads((ROOT / 'checklist/tiers.json').read_text())['rows']
assert all(r['tier'] in ('diamond', 'gold', 'silver', 'bronze') for r in register), 'tiers must be lowercase'
assignments = {r['id']: r for r in register}
assert len(assignments) == len(register), 'duplicate tier assignment'
lines, requirements, ids = [], {}, []
for line in source.read_text().splitlines():
    m = re.match(r'^\| ([A-Z][A-Z0-9]*-\d{2}) \|', line)
    if m:
        key = m[1]
        ids.append(key)
        row = assignments[key]
        line = re.sub(r' (Diamond|Gold|Silver|Bronze) \|$', '', line).rstrip()
        if not line.endswith('|'):
            line += ' |'
        line += ' ' + row['tier'].title() + ' |'
        # Canonical requirements may contain pipes inside backticks.
        requirements[key] = line.split(' | ')[1]
    elif line == '| ID | Requirement and pass criterion | Verify | Class |':
        line += ' Tier |'
    elif line == '|---|---|---|---|':
        line += '---|'
    lines.append(line)
assert ids == [r['id'] for r in register], 'tier inventory/order mismatch'
source.write_text('\n'.join(lines) + '\n')
counts = Counter(r['tier'] for r in register)
intro = '''# Production priorities: Diamond, Gold, Silver, Bronze

These are agency priorities, not third-party certifications. Use this view to decide what to do next; use the linked full catalogue for the exact criterion and evidence method. All 275 IDs remain. A shorter operating view must not erase a failed check.

| Tier | Meaning | Gate |
|---|---|---|
| Diamond | Essential journeys, accessibility, security, privacy, legal duties, truthful content and safe release | Every applicable item must pass. No waiver. |
| Gold | Smooth, reliable experience, performance and delivery quality | Diamond plus Gold for Gold completion. |
| Silver | Useful enhancements, maintenance improvements and optional scope | Prioritized backlog; adds to Diamond and Gold. |
| Bronze | Specialist polish, reference comparisons and legacy bookkeeping | Retained when useful or contracted; never a weaker safety standard. |

## How to use it

1. Inventory routes, data flows, providers, jurisdictions and contracted features. Unknown applicability is unresolved, not N/A. Privacy review includes hosting logs and processors even on a cookieless site.
2. Clear Diamond before claiming launch completeness. Review core navigation, readable mobile content, keyboard/assistive access, real form delivery, secrets, access controls, TLS, truthful claims, privacy and rights, recovery and exact deployment identity.
3. Prepare final-domain probes and rollback before controlled cutover; final-domain Diamond checks run immediately afterwards. Until then the cutover is provisional. Handover readiness is not launch approval.
4. Work through Gold next. Record optional misses with an owner, reason, next action and date. Contracted features remain delivery obligations even if their generic priority is Silver or Bronze.
5. Keep future field metrics, 7/30-day reviews and recurring checks pending until actually observed. Timing is scheduling metadata, never an exemption from Diamond.

Tier is separate from applicability and evidence status. `G` is always applicable, `C` conditional, `R` an enhancement whose absence needs evidence for N/A. `-L` requires production-domain evidence; `-O` needs named human evidence. No fake PASS, fabricated approval or downgrade to get a green dashboard. An uncovered critical defect or applicable legal duty is Diamond regardless of its row label. Split mixed requirements before any later demotion; their highest-risk clause controls today.

The [release contract](../docs/RELEASE_EVIDENCE.md) explains phases and compatibility. The [row review](../docs/reviews/checklist-tiers-2026-10-05/ROW_REVIEW.md) records mixed requirements and review limits; [sources](../docs/reviews/checklist-tiers-2026-10-05/SOURCES.md) distinguish standards from house choices. Existing website evidence is not retroactively passed by this revision.
'''
out = [intro, '\n## Inventory\n', '| Tier | Rows |', '|---|---:|']
for tier in ('diamond', 'gold', 'silver', 'bronze'):
    out.append(f'| {tier.title()} | {counts[tier]} |')
for tier in ('diamond', 'gold', 'silver', 'bronze'):
    out.extend([f'\n## {tier.title()}\n', '| ID | Purpose and priority reason | When |', '|---|---|---|'])
    for row in register:
        if row['tier'] == tier:
            anchor = row['id'].split('-')[0].lower()
            # GitHub row links target the line in the complete catalogue.
            line_number = next(i for i, line in enumerate(lines, 1) if line.startswith('| '+row['id']+' |'))
            out.append(f"| [{row['id']}](PRODUCTION_CHECKLIST_clone_swap.md#L{line_number}) | {row['rationale']} | {row['timing']} |")
(ROOT / 'checklist/TIERS.md').write_text('\n'.join(out) + '\n')
print(dict(counts))
