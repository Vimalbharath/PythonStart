from gmfull import GraphMatrix
from collections import deque
import math

class GraphBFS(GraphMatrix):
    def topo(self):
        ans=[]
        recursion_stack = [False] * len(self.vertices)
        has_cycle = False
        visited=[0]*len(self.vertices)
        for n in range(len(self.vertices)):
            if not visited[n]:
                if self.topohelper(n, visited, recursion_stack, ans):
                    has_cycle = True
                    break

        if has_cycle:
            print("Error: The graph contains a cycle. Topological sort is not possible.")
        else:
            ans.reverse()
            print("Topological Sort Order:", ans)

    def topohelper(self,u,visited,recursion_stack,ans):
        
        visited[u]=1
        recursion_stack[u] = True 
        for i in range(len(self.vertices)):
            # Check for a valid edge (not infinity and not a self-loop)
            if self.matrix[u][i] != math.inf and self.matrix[u][i] != 0 :
                if not visited[i]:
                   if self.topohelper(i, visited, recursion_stack, ans):
                        return True
                elif recursion_stack[i]:
                    return True
        recursion_stack[u] = False 
        ans.append(self.vertices[u].name)
        return False
    
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