from unionfind import DSU
import math

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

class GraphList1(GraphList):
    def a(self):
        edges = self.get_all_edges()
        print([str(e) for e in edges])

    def kruskal(self):
        # 1. Map vertices to integer indices
        vertices = self.get_vertices()
        vertex_to_index = {vertex.name: i for i, vertex in enumerate(vertices)}
        num_vertices = len(vertices)
        
        # 2. Initialize DSU with the correct number of elements
        dsu = DSU(num_vertices)
        
        # 3. Get all unique edges and sort them by weight
        edges = sorted(self.get_unique_edges(), key=lambda edge: edge.w)
        
        mst = []
        mst_weight = 0
        
        # 4. Iterate through sorted edges and build the MST
        for edge in edges:
            u_name, v_name = edge.v1.name, edge.v2.name
            u_index = vertex_to_index[u_name]
            v_index = vertex_to_index[v_name]
            
            # Check if adding the edge creates a cycle using the integer indices
            if dsu.find(u_index) != dsu.find(v_index):
                # If not, add the edge to the MST and union the sets
                dsu.union(u_index, v_index)
                mst.append(edge)
                mst_weight += edge.w
        
        # Check if the MST is a spanning tree for the entire graph
        if len(mst) < num_vertices - 1:
            print("The graph is not connected.")
        
        print("Minimum Spanning Tree (MST) Edges:")
        for edge in mst:
            print(edge)
            
        print(f"\nTotal MST Weight: {mst_weight}")

    def to_adjacency_matrix(self):
        # 1. Get a sorted list of vertex names to create a consistent mapping
        vertex_names = sorted(self.vertices.keys())
        vertex_to_index = {name: i for i, name in enumerate(vertex_names)}
        num_vertices = len(vertex_names)
        
        # 2. Initialize the adjacency matrix with a default value
        # Use infinity for weighted graphs to represent no edge, as 0 could be a valid weight.
        if self.weighted:
            # Initialize with inf and 0 on the diagonal for self-loops (if applicable)
            matrix = [[math.inf] * num_vertices for _ in range(num_vertices)]
            for i in range(num_vertices):
                matrix[i][i] = 0
        else:
            # Use 0 for unweighted graphs
            matrix = [[0] * num_vertices for _ in range(num_vertices)]
        
        # 3. Populate the matrix from the adjacency list
        for vertex_name, vertex_obj in self.vertices.items():
            u_index = vertex_to_index[vertex_name]
            for edge in vertex_obj.get_edges():
                v_name = edge.v2.name
                v_index = vertex_to_index[v_name]
                weight = edge.w if self.weighted else 1
                
                # Update the matrix with the edge's weight (or 1 for unweighted)
                matrix[u_index][v_index] = weight
        
        # Print the mapping for clarity
        print("Vertex Name to Index Mapping:", vertex_to_index)
        
        # Print the resulting adjacency matrix
        print("Adjacency Matrix:")
        for row in matrix:
            print(row)
        
        return matrix

    def increase_matrix_size(self,matrix):
        """
        Copies a matrix and increases its dimensions by one row and one column.
        
        Args:
            matrix (list of list): The original 2D list (matrix).

        Returns:
            list of list: A new matrix with one more row and one more column.
        """
        if not matrix or not matrix[0]:
            print("Error: The input matrix is empty.")
            return [[]]
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Create the new, larger matrix filled with a default value (e.g., 0)
        # The new dimensions are (rows + 1) x (cols + 1)
        new_matrix = [[math.inf] * (cols + 1) for _ in range(rows + 1)]
        
        # Copy the elements from the original matrix into the new one
        for i in range(rows):
            for j in range(cols):
                new_matrix[i][j] = matrix[i][j]
                
        return new_matrix

if __name__ == "__main__":
    graph = GraphList1(False, True)
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
    # graph.a()
    # print("All edges (including duplicates):")
    # print([str(e) for e in graph.get_all_edges()])

    print("\nUnique edges:")
    print([str(e) for e in graph.get_unique_edges()])
    graph.kruskal()
    mat=graph.to_adjacency_matrix()
    m2=graph.increase_matrix_size([[1]])
    print("\nEnlarged Matrix:")
    for row in m2:
        print(row)