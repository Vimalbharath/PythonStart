import math

class Vertex:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
        
    def __format__(self, format_spec):
        return f"{self.name:{format_spec}}"

class GraphMatrix:
    def __init__(self, directed=False, weighted=False):
        self.vertices = []
        self.vertex_to_index = {}
        self.matrix = []
        self.directed = directed
        self.weighted = weighted

    def get_key_from_value( self,value):
        for key, val in self.vertex_to_index.items():
            if val == value:
                return key
        return None
    
    def addVertex(self, name):
        if name in self.vertex_to_index:
            return self.vertices[self.vertex_to_index[name]]
        
        new_vertex = Vertex(name)
        new_size = len(self.vertices) + 1
        
        self.vertices.append(new_vertex)
        self.vertex_to_index[name] = len(self.vertices) - 1
        
        # Initialize matrix with appropriate values for weighted/unweighted
        if self.weighted:
            new_matrix = [[math.inf] * new_size for _ in range(new_size)]
        else:
            new_matrix = [[0] * new_size for _ in range(new_size)]

        old_size = new_size - 1
        for i in range(old_size):
            for j in range(old_size):
                new_matrix[i][j] = self.matrix[i][j]
        
        # Self-loops are typically 0
        new_matrix[new_size - 1][new_size - 1] = 0
        self.matrix = new_matrix
        return new_vertex

    def addEdge(self, v1, v2, weight=1):
        if not self.weighted:
            weight = 1
            
        if v1.name not in self.vertex_to_index or v2.name not in self.vertex_to_index:
            print("Error: One or both vertices not found.")
            return

        v1_index = self.vertex_to_index[v1.name]
        v2_index = self.vertex_to_index[v2.name]
        
        self.matrix[v1_index][v2_index] = weight
        if not self.directed:
            self.matrix[v2_index][v1_index] = weight

    def print_matrix(self):
        print("Adjacency Matrix:")
        print("    ", end="")
        for vertex in self.vertices:
            print(f"{vertex:>4}", end="")
        print()
        
        for i in range(len(self.vertices)):
            print(f"{self.vertices[i]:>4}", end="")
            for j in range(len(self.vertices)):
                value = self.matrix[i][j]
                if value == math.inf:
                    print(f"{'inf':>4}", end="")
                else:
                    print(f"{value:>4}", end="")
            print()

    def getOutdegree(self):
        ans=[0]* len(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if not self.matrix[i][j]==0 and not self.matrix[i][j]==math.inf:
                    ans[i]+=1
        return ans

    def getIndegree(self):
        ans=[0]* len(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if not self.matrix[i][j]==0 and not self.matrix[i][j]==math.inf:
                    ans[j]+=1
        return ans

if __name__ == "__main__":
    # Example 1: Undirected, Weighted Graph (like a road network)
    print("--- Undirected, Weighted Graph ---")
    graph1 = GraphMatrix(directed=False, weighted=True)
    a, b, c = graph1.addVertex("a"), graph1.addVertex("b"), graph1.addVertex("c")
    graph1.addEdge(a, b, 10)
    graph1.addEdge(b, c, 5)
    graph1.print_matrix()
    
    print("\n" + "="*35 + "\n")
    
    # Example 2: Directed, Unweighted Graph (like a website's links)
    print("--- Directed, Unweighted Graph ---")
    graph2 = GraphMatrix(directed=True, weighted=False)
    a, b, c = graph2.addVertex("a"), graph2.addVertex("b"), graph2.addVertex("c")
    graph2.addEdge(a, b) # Default weight of 1 is used
    graph2.addEdge(b, c)
    graph2.print_matrix()

    graph = GraphMatrix(False, True)
    a = graph.addVertex("a")
    b = graph.addVertex("b")
    c = graph.addVertex("c")
    d = graph.addVertex("d")
    e = graph.addVertex("e")
    f = graph.addVertex("f")
    g = graph.addVertex("g")
    h = graph.addVertex("h")
    i = graph.addVertex("i")
    
    graph.addEdge(a, b, 4)
    graph.addEdge(b, c, 8)
    graph.addEdge(c, d, 7)
    graph.addEdge(d, e, 9)
    graph.addEdge(e, f, 10)
    graph.addEdge(f, g, 2)
    graph.addEdge(g, h, 1)
    graph.addEdge(h, i, 7)
    graph.addEdge(h, a, 8)
    graph.addEdge(b, h, 11)
    graph.addEdge(d, f, 14)
    graph.addEdge(c, f, 4)
    graph.addEdge(c, i, 2)
    graph.addEdge(i, g, 6)
    graph.print_matrix()
