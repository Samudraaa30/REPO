import json
import subprocess


def run_semgrep(repo_path: str):
    """
    Run Semgrep on a repository and return structured findings.
    """

    command = [
        "semgrep",
        "--config=auto",
        "--json",
        repo_path
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False
        )

        if not result.stdout:
            return []

        data = json.loads(result.stdout)

        findings = []

        for finding in data.get("results", []):

            findings.append({

                "rule_id": finding.get("check_id"),

                "severity": finding.get("extra", {}).get("severity", "UNKNOWN"),

                "message": finding.get("extra", {}).get("message", ""),

                "path": finding.get("path"),

                "start_line": finding.get("start", {}).get("line"),

                "end_line": finding.get("end", {}).get("line"),

                "metadata": finding.get("extra", {}).get("metadata", {})

            })

        return findings

    except Exception as e:

        print("Semgrep Error:", e)

        return []