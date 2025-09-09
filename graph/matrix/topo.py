from gmfull import GraphMatrix
from collections import deque
import math

class GraphBFS(GraphMatrix):
    def topo(self):
        ans=[]
        
        visited=[0]*len(self.vertices)
        for n in range(len(self.vertices)):
            if not visited[n]:
                self.topohelper(n,visited,ans)
        ans.reverse()
        print(ans) 

    def topohelper(self,u,visited,ans):
        visited[u]=1
        for i in range(len(self.vertices)):
            # Check for a valid edge (not infinity and not a self-loop)
            if self.matrix[u][i] != math.inf and self.matrix[u][i] != 0 and not visited[i]:
                self.topohelper(i, visited, ans)
        ans.append(self.vertices[u].name)
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

    graph.print_matrix()   
    graph.topo()