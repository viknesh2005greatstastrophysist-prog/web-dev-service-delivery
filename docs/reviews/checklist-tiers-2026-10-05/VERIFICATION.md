# Verification, 2026-10-05

- Source base: origin/main `56d620ae89a1bcf06db349e8d1881e860954ad1e`.
- Catalogue: 275 original unique IDs, 18 sections; 150 Diamond, 79 Gold, 31 Silver, 15 Bronze. No row removed.
- `python3 scripts/check-kit.py`: all 60 checks passed; [full log](check-kit.txt).
- `python3 -m unittest discover -s tests -v`: all 50 tests passed; [full log](tests.txt).
- Tier renderer: second run preserved both output hashes.
- `git diff --check`: passed.
- Methodology submodule initialized at reviewed pin `2c03e02d7e1849374739b576b9a0734e6d7e94ab`.

Tests include every requested priority scope, Diamond failures, missing/mixed priorities, coordinated Diamond demotion, legacy gate compatibility, contracted optional work, invalid scope, false N/A, evidence integrity and the existing adversarial cases. Test records are synthetic. This verifies the kit changes, not the RIOA release or any website's legal/security/accessibility status.
