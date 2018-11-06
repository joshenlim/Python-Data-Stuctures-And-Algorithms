import collections

class Graph:
    def __init__(self, adjList = None):
        if adjList == None:
            adjList = []
        self.adjList = adjList
        self.visited = collections.deque()
        self.spanningTree = {}

    def getVertices(self):
        return list(self.adjList.keys())

    def getEdges(self):
        edges = []
        for vertex in self.adjList:
            for nextVertex in self.adjList[vertex]:
                edge = {vertex, nextVertex}
                if edge not in edges:
                    edges.append(edge)
        return edges

    def addEdge(self, src, dest):
        if src not in self.adjList:
            self.adjList[src] = [dest]
        else:
            self.adjList[src].append(dest)

    def getNeighbours(self, vertex):
        return self.adjList[vertex]

    def printGraph(self):
        print("======================================================")
        print("| Representing graph as an array of adjacency lists: |")
        print("======================================================")
        for vertex in self.adjList:
            print(vertex, ' -> ', self.adjList[vertex])

    def genDFSTree(self, src):
        self.visited.append(src)
        vertexNeighbours = self.getNeighbours(src)
        for neighbour in vertexNeighbours:
            if neighbour not in self.visited:
                self.genDFSTree(neighbour)
                if src not in self.spanningTree:
                    self.spanningTree[src] = [neighbour]
                else:
                    self.spanningTree[src].append(neighbour)

        return self.spanningTree

    def printDFSTree(self, src):
        spanningTree = self.genDFSTree(src)
        print("================================")
        print("| Depth First Spanning Tree: |")
        print("================================")
        for vertex in spanningTree:
            print(vertex, ' -> ', spanningTree[vertex])

################################################################################################

adjacencyList = {
    "a": ["b", "f"],
    "b": ["c", "d"],
    "c": [],
    "d": ["a"],
    "f": ["a", "c"],
}

graph = Graph(adjacencyList)
print()
graph.printGraph()
print()
graph.printDFSTree("a")
print()
