LABEL_MAP = {
    "sql": "SQL Injection",
    "xss": "Cross Site Scripting",
    "command": "Command Injection",
    "exec": "Remote Code Execution",
    "secret": "Secrets Detection",
    "password": "Secrets Detection",
    "auth": "Authentication",
    "authorize": "Authorization",
    "csrf": "CSRF",
    "cookie": "Session Management",
    "path": "Path Traversal",
    "traversal": "Path Traversal",
    "deserialize": "Insecure Deserialization",
    "logging": "Logging & Monitoring",
    "dependency": "Dependency Security",
    "input": "Input Validation"
}


def generate_label(rule, message):

    text = f"{rule} {message}".lower()

    for keyword, label in LABEL_MAP.items():

        if keyword in text:
            return label

    return "General Security"