from graphlist import GraphList
from collections import deque

class GraphListBFS(GraphList):
    def topo(self):
       ans=[]
       vertices=self.vertices
       visited=set()
       for vertex in vertices:
            if vertex not in visited:
                self.topohelper(vertex,visited,ans)
       print(ans)
       print ("No cycle present") if len(ans)==len(vertices) else print("Cycle present")

    
    def topohelper(self,vertex,visited,ans):
        if vertex in visited:
            return 
        visited.add(vertex.name)
        for edge in vertex.getEdges2():
            if edge.v2 not in visited:
                self.topohelper(edge.v2,visited,ans)
        ans.append(vertex.name)


        
       

if __name__=="__main__":
    graph=GraphListBFS(True,True)
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
    graph.addEdge(sl,sg,5000)
    graph.addEdge(bg,sg,6000)
    print(graph)
    graph.topo()

    