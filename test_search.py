from backend.repository.indexer import build_repository_index
from backend.repository.search import search_repository

index = build_repository_index("repos/bandit")

results = search_repository(index, "test")

print()

print(f"Found {len(results)} files")

print()

for file in results[:20]:

    print(file["path"])