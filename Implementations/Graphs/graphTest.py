from graphObj import Graph


def main():
    g = {
        "a": {"d"},
        "b": {"c"},
        "c": {"b", "c", "d", "e"},
        "d": {"a", "c"},
        "e": {"c"},
        "f": {}
    }

    graph = Graph(g)

    print(graph)
    print("\n")
    print("BFS --> ", end="")
    print(graph.breadthFirstSearch("c"))
    print("\n")
    print("DFS --> ", end="")
    print(graph.depthFirstSearch("c"))

if __name__ == "__main__":
    main()