from pathlib import Path

IGNORE = {
    ".git",
    ".github",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build"
}


def explore_repository(repo_path):

    tree = []

    repo = Path(repo_path)

    for file in repo.rglob("*"):

        if not file.is_file():
            continue

        if any(folder in file.parts for folder in IGNORE):
            continue

        tree.append({
            "path": str(file.relative_to(repo)),
            "name": file.name,
            "extension": file.suffix
        })

    return sorted(tree, key=lambda x: x["path"])