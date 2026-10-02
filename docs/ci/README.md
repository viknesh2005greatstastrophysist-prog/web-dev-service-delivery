# Activate kit CI

Status: prepared and reviewed, not active. The configured GitHub OAuth token rejected the workflow push because it lacks `workflow` scope. The local 42 consistency checks and 31 tests passed; no hosted CI result is claimed.

A repository maintainer with workflow write permission can activate the exact proposal:

```bash
mkdir -p .github/workflows
cp docs/ci/verify-kit.yml .github/workflows/verify-kit.yml
python3 scripts/check-kit.py
python3 -m unittest discover -s tests -v
git add .github/workflows/verify-kit.yml
git commit -m "Activate delivery kit verification workflow"
git push
```

For the configured GitHub CLI OAuth login, obtain the missing permission with `gh auth refresh -h github.com -s workflow` and complete GitHub's authorization flow before pushing. This is an account authorization step, not a permission the code can grant itself.

Inspect the Actions run for the actual pushed commit and record its outcome. The workflow uses read-only repository permissions, a pinned checkout action, a public pinned submodule and Python's standard library. It does not deploy a client site or use provider secrets. Retain the template as the reviewable source; if it changes, update the active copy too.
