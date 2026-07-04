from pathlib import Path
from backend.repository.function_parser import extract_functions


def build_function_index(repository_index):

    function_index = []

    for file in repository_index:

        functions = extract_functions(
            file["path"]
        )

        for function in functions:

            function["file"] = file["path"]

            function_index.append(function)

    return function_index