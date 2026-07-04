import json

from backend.api.qwen_client import QwenClient

client = QwenClient()


def analyze_group(
    rule,
    snippets,
    languages,
    frameworks,
    repository_summary,
    call_graph
):

    snippets = snippets[:3]

    prompt = f"""
You are a Senior Cybersecurity Engineer.

Repository Languages:
{languages}

Frameworks:
{frameworks}

Repository Summary:
{repository_summary}

Semgrep Rule:
{rule}

Candidate Snippets:
"""

    for i, snippet in enumerate(snippets):

        prompt += f"""

========================
Snippet {i}

File:
{snippet["file"]}

Lines:
{snippet["start_line"]} - {snippet["end_line"]}

Code:

{snippet["code"][:1200]}
"""

    prompt += f"""

Call Graph

{call_graph}

Your task:

1. Choose the BEST representative snippet.
2. Explain the vulnerability.
3. Give OWASP mapping.
4. Give CWE mapping.
5. Explain business impact.
6. Explain execution flow.
7. Explain root cause.
8. Explain possible attack.
9. Recommend a fix.

Return ONLY valid JSON.

{{
"selected":0,
"reason":"",
"confidence":"",

"label":"",
"title":"",
"summary":"",
"severity":"",
"risk":"",
"owasp":"",
"cwe":"",
"impact":"",
"recommendation":"",

"flow":{{
"flow":"",
"root_cause":"",
"attack":"",
"fix":""
}}
}}
"""

    result = client.ask(prompt)

    if "error" in result:

        raise Exception(result["error"])

    text = result["response"]

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)