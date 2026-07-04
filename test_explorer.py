from backend.repository.explorer import explore_repository

files = explore_repository("repos/flask")

for f in files[:20]:
    print(f)