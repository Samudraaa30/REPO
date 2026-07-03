import os
import shutil
from pathlib import Path
from git import Repo


REPOS_DIR = Path("repos")


def clone_repository(repo_url: str) -> str:
    """
    Clone a GitHub repository into the local repos directory.

    Returns:
        Absolute path of the cloned repository.
    """

    if not repo_url.startswith("https://github.com/"):
        raise ValueError("Please enter a valid GitHub repository URL.")

    REPOS_DIR.mkdir(exist_ok=True)

    repo_name = repo_url.rstrip("/").split("/")[-1]
    clone_path = REPOS_DIR / repo_name

    # Remove previous clone
    if clone_path.exists():
        shutil.rmtree(clone_path)

    print(f"Cloning {repo_url}...")

    Repo.clone_from(repo_url, clone_path)

    print("Repository cloned successfully.")

    return str(clone_path.resolve())