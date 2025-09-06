from graphlist import GraphList

class GraphListBFS(GraphList):
    def bfs(self):
        return "Hi Vimal"



if __name__=="__main__":
    graph=GraphListBFS(True,False)
    ch=graph.addVertex("Chennai")
    dl=graph.addVertex("Delhi")
    mb=graph.addVertex("Mumbai")
    graph.addEdge(ch,dl,800)
    graph.addEdge(ch,mb,400)
    print(graph)
    print(graph.bfs())