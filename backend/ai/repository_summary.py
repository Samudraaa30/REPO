import json

from backend.api.qwen_client import QwenClient

client = QwenClient()


def repository_summary(

    languages,

    frameworks,

    files,

    functions

):

    prompt = f"""

You are a cybersecurity architect.

Repository

Languages

{languages}

Frameworks

{frameworks}

Files

{files}

Functions

{len(functions)}

Generate ONLY JSON.

{{
"repository_type":"",
"architecture":"",
"security_sensitive_files":[],
"security_sensitive_components":[],
"summary":""
}}

"""

    result = client.ask(prompt)

    try:

        return json.loads(

            result["response"]

        )

    except:

        return {}