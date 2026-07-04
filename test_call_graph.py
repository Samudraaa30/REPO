from backend.repository.call_graph import build_call_graph

graph = build_call_graph(
    "repos/bandit/bandit/core/manager.py"
)

for function, calls in graph.items():

    print()

    print(function)

    print("Calls:")

    for call in calls:

        print("  ->", call)