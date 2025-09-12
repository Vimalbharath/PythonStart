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
        sindex=index[source_vertex_name]
        distance[sindex]=0
        for i in range(n-1):
            distance[i]


    
if __name__=="__main__":
    graph2=GraphBFS(True,True)    
    a=graph2.addVertex("a")
    b=graph2.addVertex("b")
    c=graph2.addVertex("c")
    graph2.addEdge(a,b,1)
    graph2.addEdge(a,c,3)
    graph2.addEdge(c,b,-3)
    graph2.print_matrix()
    graph2.bellmanford("a")