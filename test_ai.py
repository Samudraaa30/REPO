from backend.ai.reasoning import explain_vulnerability

response = explain_vulnerability(

    "SQL Injection",

    """
query = "SELECT * FROM users WHERE id=" + user_id
"""
)

print(response)