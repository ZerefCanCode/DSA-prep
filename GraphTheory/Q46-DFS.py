from collections import defaultdict
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)

    def insertEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFS_helper(self, u, visited):
        visited[u] = True
        print(u)

        for v in self.adj[u]:
            if not visited[v]:
                self.DFS_helper(v, visited)

    def DFS(self, u):
        visited = [False] * self.V
        self.DFS_helper(u, visited)

if __name__ == "__main__":
    g = Graph(7)

    g.insertEdge(0, 1)
    g.insertEdge(0, 3)
    g.insertEdge(1, 4)
    g.insertEdge(1, 2)
    g.insertEdge(2, 3)
    g.insertEdge(4, 5)
    g.insertEdge(4, 6)
    g.insertEdge(5, 6)

    g.DFS(0)