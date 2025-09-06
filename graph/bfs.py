from graphlist import GraphList
from collections import deque

class GraphListBFS(GraphList):
    def bfs(self):
        ans=[]
        vertices= self.getVertices()
        visited=[0]*len(vertices)
        for i in vertices:
            print(i.name)
        print(visited)
        queue=deque([vertices[0]])
        visited[0]=1
        #while queue:
        currentvertex=queue.popleft()
        ans.append(currentvertex)
        edges=currentvertex.getEdges()
        print(edges)
        # for i in vertices:
        #     print(i.name)
        # print(visited)
        # print(queue)



if __name__=="__main__":
    graph=GraphListBFS(True,True)
    ch=graph.addVertex("Chennai")
    dl=graph.addVertex("Delhi")
    mb=graph.addVertex("Mumbai")
    bg=graph.addVertex("Bangalore")
    kl=graph.addVertex("Kolkata")
    graph.addEdge(ch,dl,800)
    graph.addEdge(ch,mb,400)
    graph.addEdge(mb,bg,300)
    graph.addEdge(bg,kl,400)
    print(graph)
    graph.bfs()