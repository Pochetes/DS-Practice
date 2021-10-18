class Graph(object):
    def __init__(self, graph=None):
        if graph == None:
            graph = {}
        self.graph = graph
    
    # returns a boolean whether vertex exists in graph
    def doesVertexExist(self, vertex):
        return vertex in self.graph

    # returns a list of all edges in a specific vertex
    def edgesForVertex(self, vertex):
        if self.doesVertexExist(vertex):
            return self.graph[vertex]
        else:
            print("Could not produce edges for Vertex " + str(vertex) + " because it does not exist!")
    
    # returns a list of all nodes/vertices in graph
    def allVertices(self):
        return set(self.graph.keys())
    
    def allEdges(self):
        return self.__generateEdges()
    
    # adds a vertex into graph as a key=vertex : value=adjacent_nodes pair
    def addVertex(self, vertex):
        if not self.doesVertexExist(vertex):
            self.graph[vertex] = {}

    # adds an adjancency node to a specifc node 
    def addEdge(self, edge):
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)

        for v1, v2 in [(vertex1, vertex2), (vertex2, vertex1)]:
            if v1 in self.graph:
                self.graph[v1].add(v2)
            else:
                self.graph[v1] = {v2}

    # returns a list of all the edges of the graph
    def __generateEdges(self):
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    # prints nodes traversed in a breadth-first fashion
    # runtime: O(V + E) where V : vertices and E : edges
    def breadthFirstSearch(self, vertex):
        visited = [vertex]
        queue = [vertex]

        while not self.isEmpty(queue):
            currNode = queue.pop(0)
            print(currNode, end=" ")

            for neighbor in self.graph[currNode]:

                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

    def depthFirstSearch(self, vertex):
        visited = []
        stack = [vertex]

        while not self.isEmpty(stack):
            currNode = stack.pop()
            print(currNode, end=" ")
            visited.append(currNode)
            
            for neighbor in self.edgesForVertex(currNode):
                if neighbor not in visited:
                    stack.append(neighbor)

        

    # returns whether iterable is empty or not
    def isEmpty(self, obj):
        return len(obj) == 0

    # creates an iterable object for graph
    def __iter__(self):
        self.iterObj = iter(self.graph)
        return self.iterObj
    
    # allows for iteration of graph
    def __next__(self):
        return next(self.iterObj)
    

    def __str__(self):
        res = "vertices: "
        for k in self.graph:
            res += str(k)
        res += "\nedges: "
        for edge in self.__generateEdges():
            res += str(edge) + " "
        return res