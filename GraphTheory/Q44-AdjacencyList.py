class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, s, d):
        self.adj[s].append(d)
        self.adj[d].append(s)

    def printGraph(self):
        for d in range(self.V):
            print(f"\nVertex {d}:", end="")
            for x in self.adj[d]:
                print(f" -> {x}", end="")
            print()

if __name__ == "__main__":
    V = 5
    graph = Graph(V)

    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 2)
    graph.printGraph()