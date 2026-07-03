from pathlib import Path


CONTEXT = 15


def extract_snippet(file_path: str, line_number: int):
    """
    Extract a code snippet around a vulnerable line.
    """

    path = Path(file_path)

    if not path.exists():
        return None

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    total = len(lines)

    start = max(1, line_number - CONTEXT)
    end = min(total, line_number + CONTEXT)

    snippet = "".join(lines[start - 1:end])

    return {
        "file": str(path),
        "start_line": start,
        "end_line": end,
        "code": snippet
    }