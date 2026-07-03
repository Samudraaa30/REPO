import json

from backend.api.qwen_client import QwenClient

AI_URL = "YOUR_NGROK_URL"


client = QwenClient(AI_URL)


def explain_vulnerability(rule, snippet):

    prompt = f"""
You are a Senior Cybersecurity Engineer.

Analyze this security finding.

Rule:
{rule}

Code:

{snippet}

Return ONLY valid JSON.

{{
"title":"",
"summary":"",
"label":"",
"severity":"",
"risk":"",
"owasp":"",
"cwe":"",
"impact":"",
"recommendation":""
}}

"""

    result = client.ask(prompt)

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