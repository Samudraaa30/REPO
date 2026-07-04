from backend.repository.clone import clone_repository
from backend.repository.function_indexer import build_function_index
from backend.repository.indexer import build_repository_index
from backend.repository.language_detector import detect_languages
from backend.repository.framework_detector import detect_frameworks
from backend.repository.function_mapper import map_snippet_to_function
from backend.repository.call_graph import build_call_graph

from backend.scanners.semgrep import run_semgrep

from backend.snippets.grouper import group_findings
from backend.snippets.extractor import extract_snippet

from backend.ai.analyze_group import analyze_group
from backend.ai.security_labels import generate_label
from backend.ai.risk_engine import calculate_risk
from backend.ai.file_importance import calculate_file_importance
from backend.ai.repository_summary import repository_summary

SEVERITY_ORDER = {
    "CRITICAL": 4,
    "HIGH": 3,
    "MEDIUM": 2,
    "LOW": 1,
    "INFO": 0,
    "UNKNOWN": 0
}


def analyze_repository(repo_url: str):

    print("=" * 70)
    print("AI Repository Explorer")
    print("=" * 70)

    # --------------------------------------------------
    # Clone Repository
    # --------------------------------------------------

    repo = clone_repository(repo_url)

    # --------------------------------------------------
    # Repository Intelligence
    # --------------------------------------------------

    index = build_repository_index(repo)

    functions = build_function_index(index)

    call_graph = {}

    for file in index:

        graph = build_call_graph(file["path"])

        if graph:
            call_graph[file["path"]] = graph

    languages = detect_languages(index)

    frameworks = detect_frameworks(repo)

    summary = repository_summary(
        languages,
        frameworks,
        len(index),
        functions
    )

    # --------------------------------------------------
    # Security Scan
    # --------------------------------------------------

    findings = run_semgrep(repo)

    if not findings:

        return {

            "repository": repo,

            "languages": languages,

            "frameworks": frameworks,

            "repository_summary": summary,

            "functions": functions,

            "repository_files": index,

            "call_graph": call_graph,

            "important_files": [],

            "risk_score": 0,

            "total_files": len(index),

            "total_findings": 0,

            "unique_vulnerabilities": 0,

            "results": []

        }

    grouped = group_findings(findings)

    results = []

    # --------------------------------------------------
    # Process Every Vulnerability Group
    # --------------------------------------------------

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

        graph = call_graph.get(
            snippets[0]["file"],
            {}
        )

        try:

            analysis = analyze_group(
                rule=rule,
                snippets=snippets,
                languages=languages,
                frameworks=frameworks,
                repository_summary=summary,
                call_graph=graph
            )

        except Exception as e:

            print("AI Error:", e)

            analysis = {

                "selected": 0,

                "reason": "Default representative snippet selected.",

                "confidence": "80%",

                "label": generate_label(
                    rule,
                    vulnerabilities[0]["message"]
                ),

                "title": rule,

                "summary": "AI explanation unavailable.",

                "severity": vulnerabilities[0]["severity"],

                "risk": vulnerabilities[0]["severity"],

                "owasp": "",

                "cwe": "",

                "impact": "",

                "recommendation": "Review manually.",

                "flow": {

                    "flow": "",

                    "root_cause": "",

                    "attack": "",

                    "fix": ""

                }

            }

        selected = analysis.get("selected", 0)

        if selected < 0:
            selected = 0

        if selected >= len(snippets):
            selected = 0

        best = snippets[selected]

        mapped_function = map_snippet_to_function(
            best,
            functions
        )
     
        results.append({

            "rule": rule,

            "label": analysis.get(
                "label",
                generate_label(
                    rule,
                    vulnerabilities[0]["message"]
                )
            ),

            "title": analysis.get(
                "title",
                rule
            ),

            "summary": analysis.get(
                "summary",
                ""
            ),

            "severity": analysis.get(
                "severity",
                vulnerabilities[0]["severity"]
            ),

            "risk": analysis.get(
                "risk",
                vulnerabilities[0]["severity"]
            ),

            "owasp": analysis.get(
                "owasp",
                ""
            ),

            "cwe": analysis.get(
                "cwe",
                ""
            ),

            "impact": analysis.get(
                "impact",
                ""
            ),

            "recommendation": analysis.get(
                "recommendation",
                ""
            ),

            "confidence": analysis.get(
                "confidence",
                "80%"
            ),

            "reason": analysis.get(
                "reason",
                ""
            ),

            "occurrences": len(vulnerabilities),

            "snippet": best,

            "function": mapped_function,

            "flow": analysis.get(
                "flow",
                {}
            )

        })

    # --------------------------------------------------
    # Sort Results
    # --------------------------------------------------

    results.sort(

        key=lambda x: SEVERITY_ORDER.get(
            str(x["severity"]).upper(),
            0
        ),

        reverse=True

    )

    # --------------------------------------------------
    # Repository Statistics
    # --------------------------------------------------

    important_files = calculate_file_importance(results)

    report = {

        "repository": repo,

        "languages": languages,

        "frameworks": frameworks,

        "repository_summary": summary,

        "functions": functions,

        "repository_files": index,

        "call_graph": call_graph,

        "important_files": important_files,

        "risk_score": calculate_risk(results),

        "total_files": len(index),

        "total_findings": len(findings),

        "unique_vulnerabilities": len(results),

        "results": results

    }

    return report