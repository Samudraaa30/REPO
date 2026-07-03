from backend.scanners.semgrep import run_semgrep
from backend.snippets.grouper import group_findings

findings = run_semgrep("repos/flask")

groups = group_findings(findings)

print(f"Unique Vulnerabilities: {len(groups)}")

for rule, items in groups.items():
    print(rule, len(items))