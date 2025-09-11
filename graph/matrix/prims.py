from gmfull import GraphMatrix
from collections import deque
import math
import heapq
from graph.unionfind import DSU

class GraphBFS(GraphMatrix):
    def prims(self,start_vertex):
        n=len(self.vertices)
        mst_weight=0
        queue=heapq((a,b),key=b)
        mstset=set()
        weightarray=[math.inf]*n
        visitedarray=[0]*n
        parent=[0]*n
        vertex_to_index = {vertex.name: i for i, vertex in enumerate(self.vertices)}
        u=(vertex_to_index[start_vertex])
        for i in range(len(self.vertices)):
            v=self.matrix[u][i]
            if v!=math.inf and v!=0 and v<weightarray[i]:
                weightarray[i]=v
                queue.push((i,weightarray[i]))
        while queue:
            u=queue.pop().b
       

        print(mst_weight)
        for edge in mstset:
            print(edge)
            

if __name__=="__main__":
    graph=GraphBFS(False,True)
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
    graph.prims("a")
