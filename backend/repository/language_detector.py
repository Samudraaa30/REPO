from collections import Counter


def detect_languages(index):
    """
    Detect languages from the indexed repository.
    """

    counter = Counter()

    for file in index:
        counter[file["language"]] += 1

    return {
        "primary_language": counter.most_common(1)[0][0] if counter else "Unknown",
        "languages": dict(counter)
    }