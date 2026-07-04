def calculate_file_importance(results):

    importance = {}

    for finding in results:

        file = finding["snippet"]["file"]

        importance[file] = importance.get(file, 0) + 1

    ranked = sorted(
        importance.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked