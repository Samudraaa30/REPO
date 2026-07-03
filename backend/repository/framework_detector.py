from pathlib import Path

FRAMEWORK_FILES = {
    "requirements.txt": "Python",
    "pyproject.toml": "Python",
    "Pipfile": "Python",

    "package.json": "Node.js",
    "package-lock.json": "Node.js",
    "yarn.lock": "Node.js",

    "pom.xml": "Spring Boot",
    "build.gradle": "Spring Boot",

    "composer.json": "Laravel",

    "Cargo.toml": "Rust",

    "go.mod": "Go"
}


def detect_frameworks(repo_path):

    repo = Path(repo_path)

    frameworks = []

    for file in repo.rglob("*"):

        if file.name in FRAMEWORK_FILES:
            frameworks.append(FRAMEWORK_FILES[file.name])

        if file.name == "manage.py":
            frameworks.append("Django")

        if file.name == "app.py":
            frameworks.append("Flask")

        if file.name == "main.py":
            frameworks.append("FastAPI")

        if file.name == "angular.json":
            frameworks.append("Angular")

        if file.name == "next.config.js":
            frameworks.append("Next.js")

        if file.name == "vite.config.js":
            frameworks.append("Vite")

    return sorted(set(frameworks))