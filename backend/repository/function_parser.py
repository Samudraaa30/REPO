import ast
from pathlib import Path


def extract_functions(file_path):

    if not file_path.endswith(".py"):
        return []

    try:

        source = Path(file_path).read_text(
            encoding="utf-8",
            errors="ignore"
        )

        tree = ast.parse(source)

    except Exception:
        return []

    functions = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            functions.append({

                "name": node.name,

                "start_line": node.lineno,

                "end_line": getattr(
                    node,
                    "end_lineno",
                    node.lineno
                )

            })

    return functions