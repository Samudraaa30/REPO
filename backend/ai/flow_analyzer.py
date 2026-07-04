import json

from backend.api.qwen_client import QwenClient

client = QwenClient()


def analyze_flow(rule, function_name, snippet, call_graph):

    prompt = f"""
You are a Senior Cybersecurity Engineer.

Repository Finding

Rule:
{rule}

Function:
{function_name}

Representative Code:

{snippet}

Function Calls:

{call_graph}

Explain:

1. How execution reaches this code.
2. Why it is vulnerable.
3. What an attacker can do.
4. Which function is the root cause.

Return ONLY JSON.

{{
    "flow":"",
    "root_cause":"",
    "attack":"",
    "fix":""
}}
"""

    result = client.ask(prompt)
    print(result)
    try:
        return json.loads(result["response"])
    except:
        return {
            "flow": "",
            "root_cause": "",
            "attack": "",
            "fix": ""
        }