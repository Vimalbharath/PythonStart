from gmfull import GraphMatrix
from collections import deque
import math
import heapq

class GraphBFS(GraphMatrix):
    def dijstra(self,source_vertex_name):
        vertices=self.vertices
        n=len(vertices)
        index=self.vertex_to_index

        distance=[math.inf]*n
        #visited=[False]*n
        s=index[source_vertex_name]
        distance[s]=0
        minheap=[(distance[s],s)]
        while minheap:
            weight,u=heapq.heappop(minheap)
            for i in range(n):
                if self.matrix[u][i]!=math.inf and self.matrix[u][i]!=0:
                    l=self.matrix[u][i]
                    if l+weight<distance[i]:
                        distance[i]=min(distance[i],l+weight)
                        heapq.heappush(minheap,(distance[i],i))
        print(distance)

    
if __name__=="__main__":
    graph=GraphBFS(True,True)
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

    graph.print_matrix()   
    graph.dijstra("Mumbai")