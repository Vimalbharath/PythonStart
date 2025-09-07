import heapq
import math

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def get_edges(self):
        return self.edges
    
    def add_edge(self, v2, w=0):
        self.edges.append(Edge(self, v2, w))
    
    def __str__(self):
        return self.name

class Edge:
    def __init__(self, v1, v2, w=0):
        self.v1 = v1
        self.v2 = v2
        self.w = w

    def __str__(self):
        return f"Edge:{self.v1.name}-{self.v2.name}:{self.w}"

class GraphList:
    def __init__(self, directed, weighted):
        self.vertices = {}
        self.directed = directed
        self.weighted = weighted

    def add_vertex(self, name):
        if name in self.vertices:
            return self.vertices[name]
        
        new_vertex = Vertex(name)
        self.vertices[name] = new_vertex
        return new_vertex

    def get_vertices(self):
        return list(self.vertices.values())
    
    def add_edge(self, v1, v2, w=0):
        v1.add_edge(v2, w)
        if not self.directed:
            v2.add_edge(v1, w)

    def prims(self, start_vertex_name):
        num_vertices = len(self.vertices)
        
        if start_vertex_name not in self.vertices:
            print("Start vertex not found in graph.")
            return

        key = {vertex.name: math.inf for vertex in self.vertices.values()}
        parent = {vertex.name: None for vertex in self.vertices.values()}
        in_mst = {vertex.name: False for vertex in self.vertices.values()}
        
        start_vertex = self.vertices[start_vertex_name]
        key[start_vertex_name] = 0
        
        min_heap = [(0, start_vertex_name)]
        mst_edges = []
        mst_weight = 0

        while min_heap:
            # Extract the vertex with the minimum key value
            current_weight, u_name = heapq.heappop(min_heap)
            
            # If the vertex is already in the MST, skip it
            if in_mst[u_name]:
                continue
            
            in_mst[u_name] = True
            mst_weight += current_weight

            # Add the edge to the MST if it's not the start vertex
            if parent[u_name] is not None:
                mst_edges.append(f"Edge:{parent[u_name]}-{u_name}:{current_weight}")
            
            u = self.vertices[u_name]

            # Update keys of adjacent vertices
            for edge in u.get_edges():
                v = edge.v2
                weight = edge.w
                
                if not in_mst[v.name] and weight < key[v.name]:
                    key[v.name] = weight
                    parent[v.name] = u_name
                    heapq.heappush(min_heap, (weight, v.name))
        
        # Check if the graph is connected
        if len(mst_edges) < num_vertices - 1:
            print("The graph is not connected.")
        
        print("Minimum Spanning Tree (MST) Edges:")
        for edge in mst_edges:
            print(edge)
            
        print(f"\nTotal MST Weight: {mst_weight}")

    def primsvertex(self, start_vertex_name):
        vertices = self.get_vertices()
        vertex_to_index = {vertex.name: i for i, vertex in enumerate(vertices)}
        num_vertices = len(vertices)

        key = [math.inf] * num_vertices
        parent = [None] * num_vertices
        in_mst = [False] * num_vertices
        
        start_index = vertex_to_index[start_vertex_name]
        key[start_index] = 0
        min_heap = [(0, start_index)]
        
        mst_weight = 0
        mst_edges = []
        
        while min_heap:
            weight, u_index = heapq.heappop(min_heap)
            
            if in_mst[u_index]:
                continue
            
            in_mst[u_index] = True
            mst_weight += weight
            
            if parent[u_index] is not None:
                # You would need a way to get the vertex name from the index for printing
                mst_edges.append((parent[u_index], u_index, weight))
                
            u_vertex = vertices[u_index]
            
            for edge in u_vertex.get_edges():
                v_vertex = edge.v2
                v_index = vertex_to_index[v_vertex.name]
                edge_weight = edge.w
                
                if not in_mst[v_index] and edge_weight < key[v_index]:
                    key[v_index] = edge_weight
                    parent[v_index] = u_index
                    heapq.heappush(min_heap, (key[v_index], v_index))

        if len(mst_edges) < num_vertices - 1:
            print("The graph is not connected.")
        
        print("Minimum Spanning Tree (MST) Edges:")
        for edge in mst_edges:
            print(f"{edge[0]} - {edge[1]} : {edge[2]}")
        
        print(f"\nTotal MST Weight: {mst_weight}")
            
        

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

    graph.prims("a")
    graph.primsvertex("a")

    # Create a new graph for the test case
    fiber_graph = GraphList(directed=False, weighted=True)

    # Add the vertices (houses)
    a = fiber_graph.add_vertex("House A")
    b = fiber_graph.add_vertex("House B")
    c = fiber_graph.add_vertex("House C")
    d = fiber_graph.add_vertex("House D")
    e = fiber_graph.add_vertex("House E")

    # Add the edges with their weights (cable costs)
    fiber_graph.add_edge(a, b, 50)
    fiber_graph.add_edge(a, d, 60)
    fiber_graph.add_edge(b, c, 70)
    fiber_graph.add_edge(b, d, 30)
    fiber_graph.add_edge(c, e, 100)
    fiber_graph.add_edge(d, e, 20)

    print("--- Testing the Fiber Optic Network ---")
    fiber_graph.prims("House A")