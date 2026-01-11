class Graph:
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.adjMatrix = [[False for _ in range(numVertices)] for _ in range(numVertices)]

    def addEdge(self, i, j):
        self.adjMatrix[i][j] = True
        self.adjMatrix[j][i] = True

    def removeEdge(self, i, j):
        self.adjMatrix[i][j] = False
        self.adjMatrix[j][i] = False

    def toString(self):
        for i in range(self.numVertices):
            print(f"{i} : ", end="")
            for j in range(self.numVertices):
                print(1 if self.adjMatrix[i][j] else 0, end=" ")
            print()

if __name__ == "__main__":
    g = Graph(4)

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)

    g.toString()