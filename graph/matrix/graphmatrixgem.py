import math

class Vertex:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
        
    def __format__(self, format_spec):
        return f"{self.name:{format_spec}}"

class GraphMatrix:
    def __init__(self):
        self.vertices = []
        self.vertex_to_index = {}
        self.matrix = []

    def add_vertex(self, name):
        if name in self.vertex_to_index:
            return self.vertices[self.vertex_to_index[name]]
        
        new_vertex = Vertex(name)
        new_size = len(self.vertices) + 1
        
        self.vertices.append(new_vertex)
        self.vertex_to_index[name] = len(self.vertices) - 1
        
        new_matrix = [[math.inf] * new_size for _ in range(new_size)]
        
        old_size = new_size - 1
        for i in range(old_size):
            for j in range(old_size):
                new_matrix[i][j] = self.matrix[i][j]
        
        self.matrix = new_matrix
        self.matrix[new_size - 1][new_size - 1] = 0
        return new_vertex

    def add_edge(self, v1, v2, weight):
        if v1.name not in self.vertex_to_index or v2.name not in self.vertex_to_index:
            print("Error: One or both vertices not found.")
            return

        v1_index = self.vertex_to_index[v1.name]
        v2_index = self.vertex_to_index[v2.name]
        
        self.matrix[v1_index][v2_index] = weight
        self.matrix[v2_index][v1_index] = weight

    def print_matrix(self):
        print("Adjacency Matrix:")
        # Print column headers
        print("    ", end="")
        for vertex in self.vertices:
            print(f"{vertex:>4}", end="") # This now works
        print()
        
        # Print the matrix with row headers
        for i in range(len(self.vertices)):
            print(f"{self.vertices[i]:>4}", end="") # This now works
            for j in range(len(self.vertices)):
                value = self.matrix[i][j]
                if value == math.inf:
                    print(f"{'inf':>4}", end="")
                else:
                    print(f"{value:>4}", end="")
            print()

# Example usage
if __name__ == "__main__":
    graph = GraphMatrix()
    
    a = graph.add_vertex("a")
    b = graph.add_vertex("b")
    c = graph.add_vertex("c")
    d = graph.add_vertex("d")
    
    graph.add_edge(a, b, 5)
    graph.add_edge(b, c, 8)
    graph.add_edge(c, d, 2)
    graph.add_edge(a, d, 10)
    
    graph.print_matrix()