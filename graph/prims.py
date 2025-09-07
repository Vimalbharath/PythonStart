class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def __str__(self):
        # Correct and useful string representation
        return f"Vertex({self.name})"
    
    def get_edges(self):
        # Correctly returns the list of edge objects
        return self.edges
    
    def add_edge(self, v2, w=0):
        self.edges.append(Edge(self, v2, w))
    
class Edge:
    def __init__(self, v1, v2, w=0):
        self.v1 = v1
        self.v2 = v2
        self.w = w

    def __str__(self):
        return f"Edge:{self.v1.name}-{self.v2.name}:{self.w}"
    
class GraphList:
    def __init__(self, directed, weighted):
        self.vertices = {}  # Using a dictionary for O(1) vertex lookup
        self.directed = directed
        self.weighted = weighted

    def __str__(self):
        ans = "Graph:\n"
        for name, vertex in self.vertices.items():
            ans += f"  {vertex.name} -> "
            ans += ", ".join(str(edge) for edge in vertex.get_edges())
            ans += '\n'
        return ans
    
    def add_vertex(self, name):
        if name in self.vertices:
            return self.vertices[name]
        
        new_vertex = Vertex(name)
        self.vertices[name] = new_vertex
        return new_vertex
    
    def get_vertices(self):
        return list(self.vertices.values())
    
    def add_edge(self, v1, v2, w=0):
        if not self.weighted:
            w = 0
            
        # Add the edge to v1's list
        v1.add_edge(v2, w)
        if not self.directed:
            # Add the reverse edge for undirected graphs
            v2.add_edge(v1, w)

    def get_all_edges(self):
        all_edges = []
        for vertex in self.vertices.values():
            all_edges.extend(vertex.get_edges())
        return all_edges
    
    def get_unique_edges(self):
        seen_edges = set()
        unique_edges_list = []

        all_edges = self.get_all_edges()
        
        for edge in all_edges:
            # Create a unique identifier for the edge by sorting the vertex names
            edge_id = tuple(sorted((edge.v1.name, edge.v2.name)))
            
            if edge_id not in seen_edges:
                seen_edges.add(edge_id)
                unique_edges_list.append(edge)
                
        return unique_edges_list

    def prims(self):
        pass

if __name__ == "__main__":
    graph = GraphList(False, True)
    a = graph.add_vertex("a")
    b = graph.add_vertex("b")
    c = graph.add_vertex("c")
    d = graph.add_vertex("d")
    e = graph.add_vertex("e")
    f = graph.add_vertex("f")
    g = graph.add_vertex("g")
    h = graph.add_vertex("h")
    i = graph.add_vertex("i")
    
    graph.add_edge(a, b, 4)
    graph.add_edge(b, c, 8)
    graph.add_edge(c, d, 7)
    graph.add_edge(d, e, 9)
    graph.add_edge(e, f, 10)
    graph.add_edge(f, g, 2)
    graph.add_edge(g, h, 1)
    graph.add_edge(h, i, 7)
    graph.add_edge(h, a, 8)
    graph.add_edge(b, h, 11)
    graph.add_edge(d, f, 14)
    graph.add_edge(c, f, 4)
    graph.add_edge(c, i, 2)
    graph.add_edge(i, g, 6)
    
    print(graph)
    graph.prims()
   