from backend.repository.indexer import build_repository_index

files = build_repository_index("repos/flask")

print(f"Found {len(files)} source files.\n")

for file in files[:20]:
    print(file)