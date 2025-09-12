from gmfull import GraphMatrix
from collections import deque
import math
import heapq

class GraphBFS(GraphMatrix):
    def bellmanford(self,source_vertex_name):
        vertices=self.vertices
        index=self.vertex_to_index
        n=len(vertices)
        distance=[math.inf]*n
        parent = [None] * n
        s_index = index[source_vertex_name]
        distance[s_index] = 0

        # Phase 1: Relaxation (V-1 passes)
        # We iterate n-1 times over all edges to find the shortest paths.
        for _ in range(n - 1):
            for u in range(n):
                for v in range(n):
                    weight = self.matrix[u][v]
                    if weight != math.inf and weight != 0:
                        if distance[u] != math.inf and distance[u] + weight < distance[v]:
                            distance[v] = distance[u] + weight
                            parent[v] = u

        # Phase 2: Negative Cycle Detection
        # A final pass to check for any further distance updates.
        for u in range(n):
            for v in range(n):
                weight = self.matrix[u][v]
                if weight != math.inf and weight != 0:
                    if distance[u] != math.inf and distance[u] + weight < distance[v]:
                        print("Graph contains a negative cycle!")
                        return

        print("Shortest Distances:", [round(d) for d in distance])
        print("Parent Array:", parent)
        
        print("\nShortest Paths:")
        for i in range(n):
            print(f"Path to {vertices[i].name}:", self.get_path(parent, i, s_index))

    def get_path(self, parent, target_index, source_index):
        path = []
        current_index = target_index
        while current_index is not None:
            path.append(self.vertices[current_index].name)
            if current_index == source_index:
                break
            current_index = parent[current_index]

        if path and path[-1] == self.vertices[source_index].name:
            path.reverse()
            return " -> ".join(path)
        else:
            return "Not reachable."


    
if __name__=="__main__":
    graph2=GraphBFS(True,True)    
    a=graph2.addVertex("a")
    b=graph2.addVertex("b")
    c=graph2.addVertex("c")
    graph2.addEdge(a,b,1)
    graph2.addEdge(a,c,3)
    graph2.addEdge(c,b,-3)
    # graph2.print_matrix()
    # graph2.bellmanford("a")
    print("--- Example: Currency Arbitrage Detection ---")
    graph = GraphBFS(True, True) 
    a = graph.addVertex("A")
    b = graph.addVertex("B")
    c = graph.addVertex("C")
    d = graph.addVertex("D")
    graph.addEdge(a, b, -0.05)
    graph.addEdge(b, c, -0.20)
    graph.addEdge(c, a, 0.15)
    graph.addEdge(a, d, 0.30)
    graph.addEdge(d, b, -0.10)
    graph.print_matrix()
    graph.bellmanford("A")