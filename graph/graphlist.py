class Vertex:
    def __init__(self,name):
        self.name=name
        self.edges=[]

    def getEdges(self):
        return self.edges
    
    def addEdge(self,v2,w=0):
        self.edges.append(v2,w)
    
class Edge:
    def __init__(self,v1,v2,w=0):
        v1.addEdge(v2,w)

class GraphList:
    def __init__(self,directed,weighted):
        self.vertices=[]
        self.directed=directed
        self.weighted=weighted

    def __str__(self):
        return self.vertices
    
    def addVertex(self,name):
        newVertex=Vertex(name)
        self.vertices.append(newVertex)
        return newVertex
    
    def getVertices(self):
        return self.vertices
    
    def addEdge(self,v1,v2,w=0):
        Edge(v1,v2,w)
        if not self.directed:
            Edge(v2,v1,w)

if __name__=="__main__()":
    graph=GraphList(True,True)
    ch=graph.addVertex("Chennai")
    dl=graph.addVertex("Delhi")
    mb=graph.addVertex("Mumbai")
    graph.addEdge(ch,dl,800)
    graph.addEdge(ch,mb,400)
    print(graph)
