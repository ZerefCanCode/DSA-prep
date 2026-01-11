from collections import defaultdict, deque
class Graph:
    def __init__(self, numberOfVertices):
        self.numberOfVertices = numberOfVertices
        self.adjacencyList = defaultdict(list) #dictionary with list as key

    def addEdge(self, v, w):
        self.adjacencyList[v].append(w)
        self.adjacencyList[w].append(v)

    def bfsTraversal(self, vertex):
        visited = [False] * self.numberOfVertices
        queue = deque([vertex])

        visited[vertex] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbour in self.adjacencyList[vertex]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

if __name__ == "__main__":
    graph = Graph(7)
    graph.addEdge(0, 3)
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(2, 5)
    graph.addEdge(3, 6)

    graph.bfsTraversal(1)
    print()