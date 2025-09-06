from graphlist import GraphList
from collections import deque

class GraphListBFS(GraphList):
    def bfs(self):
        ans=[]
        vertices= self.getVertices()
        visited=[0]*len(vertices)
        # for i in vertices:
        #     print(i.name)
        # print(visited)
        for i in range(len(vertices)):
            if not visited[i]:
                queue=deque([vertices[i]])
                visited[i]=1
            while queue:
                currentvertex=queue.popleft()
                ans.append(currentvertex.name)
                edges=currentvertex.getEdges2()
                for e in edges:
                    endvertex=e.v2
                    pos=vertices.index(endvertex)
                    if not visited[pos]:
                        visited[pos]=1
                        queue.append(endvertex)
        print(ans)
        #print(edges)
        ## for i in vertices:
        #     print(i.name)
        # print(visited)
        # print(queue)



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
    graph.bfs()