from backend.scanners.semgrep import run_semgrep

findings = run_semgrep("repos/flask")

print(f"\nTotal Findings: {len(findings)}\n")

for finding in findings[:5]:
    print(finding)