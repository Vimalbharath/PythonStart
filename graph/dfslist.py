from graphlist import GraphList
from collections import deque

class GraphListBFS(GraphList):
    def dfs(self):
       ans=[]
       vertices=self.getVertices()
       visited=[False]*len(vertices)
       for i in range(len(vertices)):
            if not visited[i]:
                stack=deque([vertices[i]])
                visited[i]=True
            while stack:
                    current=stack.pop()
                    ans.append(current.name)
                    edges=current.getEdges2()
                    for e in edges:
                        endVertex=e.v2
                        pos=vertices.index(endVertex)
                        if not visited[pos]:
                            visited[pos]=True
                            stack.append(endVertex)
                    #         break
                    # else:
                    #     ans.append(stack.pop().name)
       #ans.reverse()
       print(ans)

    def dfs2(self):
        vertices=self.getVertices()
        visited=set()
        ans=[]
        for vertex in vertices:
            if vertex.name not in visited:
                self.dfshelper(vertex,visited,ans)
        print(ans)

    def dfshelper(self,vertex,visited,ans):
        if vertex.name in visited:
            return
        visited.add(vertex.name)
        ans.append(vertex.name)
        edges=vertex.getEdges2()
        for e in edges:
            endVertex=e.v2
            if endVertex.name not in visited:
                self.dfshelper(endVertex,visited,ans)
       



if __name__=="__main__":
    graph=GraphListBFS(False,True)
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
    print(graph)
    graph.dfs()
    graph.dfs2()