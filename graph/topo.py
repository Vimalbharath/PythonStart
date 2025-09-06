from graphlist import GraphList
from collections import deque

class GraphListBFS(GraphList):
    def topo(self):
        vertices=self.vertices
        outDegree=[0]*len(self.vertices)
        for i in range(len(vertices)):
            current=vertices[i]
            outDegree[i]=len(current.getEdges2())
        print(outDegree)

if __name__=="__main__":
    graph=GraphListBFS(True,True)
    ch=graph.addVertex("Chennai")
    dl=graph.addVertex("Delhi")
    sl=graph.addVertex("SriLanka")
    mb=graph.addVertex("Mumbai")
    bg=graph.addVertex("Bangalore")
    kl=graph.addVertex("Kolkata")
    sg=graph.addVertex("Singapore")
    graph.addEdge(ch,dl,800)
    graph.addEdge(ch,mb,800)
    graph.addEdge(mb,bg,300)
    graph.addEdge(bg,kl,400)
    graph.addEdge(ch,sl,900)
    graph.addEdge(sl,sg,5000)
    print(graph)
    graph.topo()
    