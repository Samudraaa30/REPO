import ast
from pathlib import Path


def build_call_graph(file_path):

    if not file_path.endswith(".py"):
        return {}

    try:
        source = Path(file_path).read_text(
            encoding="utf-8",
            errors="ignore"
        )

        tree = ast.parse(source)

    except Exception:
        return {}

    graph = {}

    class CallVisitor(ast.NodeVisitor):

        def __init__(self):
            self.current_function = None

        def visit_FunctionDef(self, node):

            self.current_function = node.name

            graph[node.name] = []

            self.generic_visit(node)

        def visit_Call(self, node):

            if self.current_function:

                if isinstance(node.func, ast.Name):

                    graph[self.current_function].append(
                        node.func.id
                    )

                elif isinstance(node.func, ast.Attribute):

                    graph[self.current_function].append(
                        node.func.attr
                    )

            self.generic_visit(node)

    CallVisitor().visit(tree)

    return graph