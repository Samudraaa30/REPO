from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".go": "Go",
    ".php": "PHP",
    ".cs": "C#",
    ".cpp": "C++",
    ".c": "C",
    ".rb": "Ruby",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".rs": "Rust",
}

IGNORE_FOLDERS = {
    ".git",
    ".github",
    "node_modules",
    "venv",
    ".venv",
    "__pycache__",
    "dist",
    "build",
    "target",
    ".idea",
    ".vscode",
}


def build_repository_index(repo_path: str):
    """
    Scan the repository and return all supported source files.
    """

    repo = Path(repo_path)

    files = []

    for file in repo.rglob("*"):

        if not file.is_file():
            continue

        # Ignore unwanted folders
        if any(folder in file.parts for folder in IGNORE_FOLDERS):
            continue

        ext = file.suffix.lower()

        if ext not in SUPPORTED_EXTENSIONS:
            continue

        files.append({
            "path": str(file),
            "name": file.name,
            "extension": ext,
            "language": SUPPORTED_EXTENSIONS[ext],
            "size": file.stat().st_size
        })

    return files