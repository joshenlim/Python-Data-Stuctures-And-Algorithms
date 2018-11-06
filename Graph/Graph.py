# Display graph as an array of adjacency lists (i.e Python Dictionary)

class Graph:
    def __init__(self, adjList = None):
        if adjList == None:
            adjList = []
        self.adjList = adjList

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

    def printGraph(self):
        for vertex in self.adjList:
            print(vertex, ' -> ', self.adjList[vertex])

    def getNeighbours(self, vertex):
        return self.adjList[vertex]

adjacencyList = {
    "a": ["b", "c", "d", "e"],
    "b": ["a", "d"],
    "c": ["a", "e"],
    "d": ["a", "b", "e"],
    "e": ["a", "c", "d"]
}

graph = Graph(adjacencyList)
# graph.printGraph()

vertices = graph.getVertices()
# print("Vertices:", vertices)

edges = graph.getEdges()
# print("Edges:", edges)

graph.addEdge("a", "f")
graph.addEdge("f", "a")
graph.printGraph()
