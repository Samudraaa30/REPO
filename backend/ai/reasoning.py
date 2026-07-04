import json

from backend.api.qwen_client import QwenClient


client = QwenClient()


def explain_vulnerability(
    rule,
    snippet,
    languages,
    frameworks,
    repository_summary
):
    prompt = f"""
You are a Senior Cybersecurity Engineer.

Repository Information

Languages:
{languages}

Frameworks:
{frameworks}

Repository Summary:
{repository_summary}

Semgrep Rule:
{rule}

Representative Code:

{snippet}

Explain this finding for a CYBERSECURITY ANALYST.

Return ONLY JSON.

{{
"title":"",
"label":"",
"summary":"",
"severity":"",
"risk":"",
"owasp":"",
"cwe":"",
"impact":"",
"recommendation":""
}}
"""

    result = client.ask(prompt)
    print("========== AI RESPONSE ==========")
    print(result)
    print("=================================")
    if "error" in result:

        return {
            "title": rule,
            "summary": "AI unavailable.",
            "label": "Unknown",
            "severity": "Unknown",
            "risk": "Unknown",
            "owasp": "",
            "cwe": "",
            "impact": "",
            "recommendation": ""
        }

    try:

        return json.loads(result["response"])

    except:

        return {
            "title": rule,
            "summary": result.get("response", ""),
            "label": "Unknown",
            "severity": "Unknown",
            "risk": "Unknown",
            "owasp": "",
            "cwe": "",
            "impact": "",
            "recommendation": ""
        }