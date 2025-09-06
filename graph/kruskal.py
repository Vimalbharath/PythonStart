from graphlist import GraphList

class GraphList1(GraphList):
    def a(self):
        edges=self.getAllEdges()
        print(edges)

if __name__=="__main__":
    graph=GraphList1(False,True)
    a=graph.addVertex("a")
    b=graph.addVertex("b")
    c=graph.addVertex("c")
    d=graph.addVertex("d")
    e=graph.addVertex("e")
    f=graph.addVertex("f")
    g=graph.addVertex("g")
    h=graph.addVertex("h")
    i=graph.addVertex("i")
    graph.addEdge(a,b,4)
    graph.addEdge(b,c,8)
    graph.addEdge(c,d,7)
    graph.addEdge(d,e,9)
    graph.addEdge(e,f,10)
    graph.addEdge(f,g,2)
    graph.addEdge(g,h,1)
    graph.addEdge(h,i,7)
    graph.addEdge(h,a,8)
    graph.addEdge(b,h,11)
    graph.addEdge(d,f,14)
    graph.addEdge(c,f,4)
    graph.addEdge(c,i,2)
    graph.addEdge(i,g,6)
    print(graph)
    graph.a()
