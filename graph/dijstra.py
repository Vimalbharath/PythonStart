from graphlist import GraphList
from collections import deque
import math
import heapq

class GraphBFS(GraphList):
    def dijstra(self,source_vertex_name):
        vertices=self.vertices
        n=len(vertices)

        parent=[None]*n
        index= {vertex.name : i for i,vertex in enumerate(self.vertices)} # Add this
        distance=[math.inf]*n
        #visited=[False]*n
        s=index[source_vertex_name]
        distance[s]=0
        minheap=[(distance[s],vertices[s])]
        while minheap:
            weight,u=heapq.heappop(minheap)
            for edge in u.getEdges2():
                
                    l=edge.w
                    i=index[edge.v2.name]
                    if l+weight<distance[i]:
                        parent[i]=index[u.name]
                        distance[i]=min(distance[i],l+weight)
                        heapq.heappush(minheap,(distance[i],vertices[i]))
        print(distance)
        print(parent)
        for i in range(n):
            print(self.path(parent,i))
        print("\nShortest Paths:")
        for i in range(n):
            print(f"Path to {self.vertices[i].name}:")
            self.print_path(parent, i, index[source_vertex_name])


    def path(self,parent,target):
        if parent[target]==None:
            return
        index_to_vertex = {i: vertex.name for i, vertex in enumerate(self.vertices)}
        
        self.path(parent,parent[target])
        print(index_to_vertex[parent[target]],end=" ->")

    def print_path(self, parent, target, source_index):
        path = []
        index_to_vertex = {i: vertex.name for i, vertex in enumerate(self.vertices)}
        current = target
        while current is not None:
            path.append(index_to_vertex[current])
            if current == source_index:
                break
            current = parent[current]
        
        if path:
            print(path)
        #     path.reverse()
        #     vertex_names = [self.vertices[i].name for i in path]
        #     print(" -> ".join(vertex_names))
        # else:
        #     print(f"{self.vertices[target].name} is not reachable.")


    
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
    print(graph)
    # graph.print_matrix()   
    graph.dijstra("Mumbai")