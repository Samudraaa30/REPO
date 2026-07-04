def map_snippet_to_function(snippet, function_index):

    snippet_file = snippet["file"]
    snippet_start = snippet["start_line"]
    snippet_end = snippet["end_line"]

    for function in function_index:

        if function.get("file") != snippet_file:
            continue

        if (
            function.get("start_line") is None
            or function.get("end_line") is None
        ):
            continue

        if (
            function["start_line"] <= snippet_start
            and function["end_line"] >= snippet_end
        ):
            return function

    return {
        "name": "Global Scope",
        "start_line": snippet_start,
        "end_line": snippet_end,
        "file": snippet_file
    }