from backend.scanners.semgrep import run_semgrep
from backend.snippets.extractor import extract_snippet

findings = run_semgrep("repos/flask")

if findings:

    finding = findings[0]

    snippet = extract_snippet(
        finding["path"],
        finding["start_line"]
    )

    print(snippet["file"])
    print(snippet["start_line"])
    print(snippet["end_line"])
    print(snippet["code"])