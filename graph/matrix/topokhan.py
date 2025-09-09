from gmfull import GraphMatrix
from collections import deque
import math

class GraphBFS(GraphMatrix):
   def topokhan(self):
        # A topological sort requires a directed graph
        if not self.directed:
            print("Error: Khan's algorithm requires a directed graph.")
            return

        ans = []
        indegrees = self.getIndegree()
        queue = deque()

        # 1. Initialize queue with all vertices with an in-degree of 0
        for i, in_degree_val in enumerate(indegrees):
            if in_degree_val == 0:
                queue.append(i) # Add vertex index to the queue

        # 2. Process the queue
        while queue:
            u_index = queue.popleft()
            ans.append(self.vertices[u_index].name)

            # Get neighbors of the current vertex from the matrix
            for v_index in range(len(self.vertices)):
                # Check for a valid edge from u to v
                if self.matrix[u_index][v_index] != math.inf and self.matrix[u_index][v_index] != 0:
                    indegrees[v_index] -= 1
                    # If neighbor's in-degree becomes 0, add it to the queue
                    if indegrees[v_index] == 0:
                        queue.append(v_index)

        # 3. Check for a cycle
        if len(ans) == len(self.vertices):
            print("No cycle present.")
            print("Topological Sort Order:", ans)
        else:
            print("Cycle present. Topological sort is not possible.")
if __name__=="__main__":
    graph=GraphBFS(True,False)
    ch=graph.addVertex("Chennai")
    dl=graph.addVertex("Delhi")
   
    sl=graph.addVertex("SriLanka")
    mb=graph.addVertex("Mumbai")
    bg=graph.addVertex("Bangalore")
    kl=graph.addVertex("Kolkata")
    sg=graph.addVertex("Singapore")
    graph.addEdge(dl,ch,800)
    graph.addEdge(mb,dl,800)
    graph.addEdge(mb,bg,300)
    graph.addEdge(bg,kl,400)
    graph.addEdge(ch,sl,900)
    graph.addEdge(sl,sg,9000)  
    graph.addEdge(bg,sg,9000) 
    graph.addEdge(sg,ch,1000)   

    graph.print_matrix()   
    graph.topokhan()