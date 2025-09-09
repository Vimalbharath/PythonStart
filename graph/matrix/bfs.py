from gmfull import GraphMatrix
from collections import deque
import math

class GraphBFS(GraphMatrix):
    def bfs(self):
        ans=[]
        visited=[0]*len(self.vertices)
        for n in range(len(self.vertices)):
            if visited[n]:
                continue
            queue=deque([n])
            visited[n]=1
            while queue:
                u=queue.popleft()
                ans.append(self.vertices[u].name)
                v=self.matrix[u]
                for i in range(len(v)):
                    if not v[i] == math.inf and not v[i]==0 and not visited[i]:
                        visited[i]=1
                        queue.append(i)
        print(ans) 
    
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
    graph.bfs()