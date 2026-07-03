from backend.repository.clone import clone_repository
from backend.repository.indexer import build_repository_index
from backend.repository.language_detector import detect_languages
from backend.repository.framework_detector import detect_frameworks

from backend.scanners.semgrep import run_semgrep

from backend.snippets.grouper import group_findings
from backend.snippets.extractor import extract_snippet
from backend.snippets.ranker import choose_best_snippet

from backend.ai.reasoning import explain_vulnerability


def analyze_repository(repo_url):

    print("=" * 70)
    print("AI Repository Explorer")
    print("=" * 70)

    # Clone
    repo = clone_repository(repo_url)

    # Index
    index = build_repository_index(repo)

    # Repository Intelligence
    languages = detect_languages(index)
    frameworks = detect_frameworks(repo)

    # Scan
    findings = run_semgrep(repo)

    grouped = group_findings(findings)

    results = []

    for rule, vulnerabilities in grouped.items():

        snippets = []

        for finding in vulnerabilities:

            snippet = extract_snippet(
                finding["path"],
                finding["start_line"]
            )

            if snippet:
                snippets.append(snippet)

        if not snippets:
            continue

        ranking = choose_best_snippet(
            rule,
            snippets
        )

        selected = ranking["selected"]

        if selected >= len(snippets):
            selected = 0

        best = snippets[selected]

        explanation = explain_vulnerability(
            rule,
            best["code"]
        )

        results.append({

            "rule": rule,

            "label": explanation["label"],

            "title": explanation["title"],

            "summary": explanation["summary"],

            "severity": explanation["severity"],

            "risk": explanation["risk"],

            "owasp": explanation["owasp"],

            "cwe": explanation["cwe"],

            "impact": explanation["impact"],

            "recommendation": explanation["recommendation"],

            "confidence": ranking["confidence"],

            "reason": ranking["reason"],

            "snippet": best

        })

    return {

        "repository": repo,

        "languages": languages,

        "frameworks": frameworks,

        "total_files": len(index),

        "total_findings": len(findings),

        "results": results

    }