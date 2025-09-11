
from graph.unionfind import DSU

from gmfull import GraphMatrix
from collections import deque
import math

class GraphBFS(GraphMatrix):
    def kruskal(self):
        mst_weight=0
        mstset=set()
        alledges=self.edges
        asec=sorted(alledges,key=lambda edge: edge.w)
        # for edge in asec:
        #     print(edge)
        dsu=DSU(len(self.vertices))
        vertex_to_index = {vertex.name: i for i, vertex in enumerate(self.vertices)}
        for edge in asec:
            #print(vertex_to_index[edge.u.name],vertex_to_index[edge.v.name])
            pu=dsu.find(vertex_to_index[edge.u.name])
            pv=dsu.find(vertex_to_index[edge.v.name])
            if pu!=pv:
                dsu.union(vertex_to_index[edge.u.name],vertex_to_index[edge.v.name])
                mst_weight+=edge.w
                mstset.add(edge)

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
    graph.kruskal()

    # dsu=DSU(6)
    # for i in range(6):
    #     dsu.make_set(i)
    # edges=[[0,1],[0,2],[1,3],[3,4],[4,5]]
    # for edge in edges:
    #     x=dsu.find(edge[0])
    #     y=dsu.find(edge[1])
    #     if x==y:
    #         print("Cycle Present")
    #         break
    #     else:
    #         dsu.union(edge[0],edge[1])
    # else:
    #     print("No Cycle")
    