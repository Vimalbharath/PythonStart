from gmfull import GraphMatrix
from collections import deque
import math

class GraphBFS(GraphMatrix):
    def topokhan(self):
        ans=[]
        has_cycle = False
        visited=[0]*len(self.vertices)

        print(self.getOutdegree())
        print(self.getIndegree())
       
        if has_cycle:
            print("Error: The graph contains a cycle. Topological sort is not possible.")
        else:
            ans.reverse()
            print("Topological Sort Order:", ans)
    
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
    graph.topokhan()