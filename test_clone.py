from backend.repository.clone import clone_repository

repo = clone_repository(
    "https://github.com/pallets/flask"
)

print(repo)