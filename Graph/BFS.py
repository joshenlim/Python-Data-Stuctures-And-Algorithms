import collections

class Graph:
    def __init__(self, adjList = None):
        if adjList == None:
            adjList = []
        self.adjList = adjList
        self.shortestPath = collections.deque()

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

    def findShortestPath(self, src, dest):
        toVisit = collections.deque()
        visited = collections.deque()
        self.shortestPath.clear()
        paths = []

        toVisit.append(src)
        while (len(toVisit) != 0):
            vertex = toVisit.popleft()
            visited.append(vertex)

            vertexNeighbours = self.getNeighbours(vertex)
            for neighbour in vertexNeighbours:
                paths.append([neighbour, vertex])
                if neighbour == dest:
                    return self.processPath(src, dest, paths)
                elif neighbour not in visited and neighbour not in toVisit:
                    toVisit.append(neighbour)

        return shortestPath

    def processPath(self, src, dest, paths):
        for path in paths:
            pathDest = path[0]
            pathSrc = path[1]
            if pathDest == dest:
                if pathSrc == src:
                    self.shortestPath.appendleft(pathSrc)
                    print("Given source:", src, " and destination:", dest)
                    print("Shortest Path:", self.stringifyShortestPath())
                    return
                else:
                    self.shortestPath.appendleft(pathDest)
                    self.shortestPath.appendleft(pathSrc)
                    self.processPath(src, pathSrc, paths)

    def stringifyShortestPath(self):
        path = ""
        for i in range(0, len(self.shortestPath)):
            vertext = self.shortestPath[i]
            if i == len(self.shortestPath) - 1:
                path += vertext
            else:
                path += vertext + " -> "
        return path

    def genBFSTree(self):
        toVisit = collections.deque()
        visited = collections.deque()
        root = list(self.adjList.keys())[0]
        spanningTree = {}

        toVisit.append(root)
        while (len(toVisit) != 0):
            vertex = toVisit.popleft()
            visited.append(vertex)

            vertexNeighbours = self.getNeighbours(vertex)
            for neighbour in vertexNeighbours:
                if neighbour not in visited and neighbour not in toVisit:
                    toVisit.append(neighbour)
                    if vertex not in spanningTree:
                        spanningTree[vertex] = [neighbour]
                    else:
                        spanningTree[vertex].append(neighbour)

        return spanningTree

    def printBFSTree(self):
        spanningTree = self.genBFSTree()
        print("================================")
        print("| Breadth First Spanning Tree: |")
        print("================================")
        for vertex in spanningTree:
            print(vertex, ' -> ', spanningTree[vertex])

################################################################################################

adjacencyList = {
    "a": ["b", "c", "f"],
    "b": ["c", "d"],
    "c": [],
    "d": ["a", "c"],
    "e": ["c", "g"],
    "f": ["a", "c"],
    "g": ["d", "e"]
}

graph = Graph(adjacencyList)
print()
graph.printGraph()
print()
graph.printBFSTree()
print()
traverseAtoD = graph.findShortestPath("a", "d")
print()
