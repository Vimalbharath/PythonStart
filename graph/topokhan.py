from dfslist import GraphListBFS
from collections import deque

class GraphListBFS1(GraphListBFS):
    def khan(self):
      ans=[]
      vertices=self.vertices
      inDegree=[0]*len(vertices)
      for vertex in vertices:
         edges=vertex.getEdges2()
         for edge in edges:
            pos=vertices.index(edge.v2)
            inDegree[pos]+=1
      print(inDegree)
      for i in range(len(inDegree)):
         if not inDegree[i]:
            ans.append(vertices[i].name)
            edges=vertices[i].getEdges2()
            for edge in edges:
                pos=vertices.index(edge.v2)
                inDegree[pos]-=1
      print(inDegree)
      print(ans)

if __name__=="__main__":
    graph=GraphListBFS1(True,True)
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
    #graph.addEdge(kl,dl,6000)
    graph.addEdge(sl,sg,5000)
    graph.addEdge(bg,sg,6000)
    print(graph)
    graph.dfs()
    graph.dfs2()
    graph.khan()

    