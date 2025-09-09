from gmfull import GraphMatrix
from collections import deque
import math

class GraphBFS(GraphMatrix):
    def dfs(self):
        ans=[]
        visited=[0]*len(self.vertices)
        for n in range(len(self.vertices)):
            if not visited[n]:
                self.dfshelper(n,visited,ans)
        print(ans) 

    def dfshelper(self,u,visited,ans):
        visited[u]=1
        ans.append(self.vertices[u].name)
        for i in range(len(self.vertices)):
            # Check for a valid edge (not infinity and not a self-loop)
            if self.matrix[u][i] != math.inf and self.matrix[u][i] != 0 and not visited[i]:
                self.dfshelper(i, visited, ans)
    
if __name__=="__main__":
    graph=GraphBFS(False,True)
    ch=graph.addVertex("Chennai")
    dl=graph.addVertex("Delhi")
   
    sl=graph.addVertex("SriLanka")
    mb=graph.addVertex("Mumbai")
    bg=graph.addVertex("Bangalore")
    kl=graph.addVertex("Kolkata")
    graph.addEdge(ch,dl,800)
    graph.addEdge(ch,mb,800)
    graph.addEdge(mb,bg,300)
    graph.addEdge(bg,kl,400)
    graph.print_matrix()   
    graph.dfs()