import json

from backend.api.qwen_client import QwenClient

client = QwenClient()


def choose_best_snippet(rule, snippets):

    prompt = f"""
You are a cybersecurity expert.

The following snippets triggered the SAME Semgrep rule.

Rule:

{rule}

Choose ONLY ONE representative snippet.

Return JSON.

{{
"selected":0,
"reason":"",
"confidence":""
}}

"""

    for i, snippet in enumerate(snippets):

        prompt += f"""

Snippet {i}

File:

{snippet['file']}

Code:

{snippet['code']}

"""

    result = client.ask(prompt)
    print(result)

    if "error" in result:

        return {
            "selected": 0,
            "reason": "Fallback selection.",
            "confidence": "80%"
        }

    try:

        return json.loads(result["response"])

    except:

        return {
            "selected": 0,
            "reason": "Fallback selection.",
            "confidence": "80%"
        }