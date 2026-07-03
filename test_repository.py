from backend.repository.indexer import build_repository_index
from backend.repository.language_detector import detect_languages
from backend.repository.framework_detector import detect_frameworks

repo = "repos/flask"

index = build_repository_index(repo)

print("\n===== LANGUAGES =====")
print(detect_languages(index))

print("\n===== FRAMEWORKS =====")
print(detect_frameworks(repo))