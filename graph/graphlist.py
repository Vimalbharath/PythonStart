class Vertex:
    def __init__(self,name):
        self.name=name
        self.edges=[]

    def __str__(self):
        ans=''
        ans=ans+ "a"+self.name
        return ans
    
    def getEdges(self):
        ans=''
        for i in self.edges:
            ans=ans+str(i)
        return ans
    
    def getEdges2(self):
        return self.edges
    
    def addEdge(self,v2,w=0):
        self.edges.append(Edge(self,v2,w))
    
class Edge:
    def __init__(self,v1,v2,w=0):
        self.v1=v1
        self.v2=v2
        self.w=w

    def __str__(self):
        ans=''
        ans=ans+ "Edge :"+ str(self.v1.name)+"-"+str(self.v2.name)+":"+str(self.w)+". "
        return ans
    
class GraphList:
    def __init__(self,directed,weighted):
        self.vertices=[]
        self.directed=directed
        self.weighted=weighted

    def __str__(self):
        ans=''
        for i in self.vertices:
            ans=ans+ "---"+i.name+"-->"+i.getEdges()
            ans=ans+'\n'
        return ans
    
    def addVertex(self,name):
        newVertex=Vertex(name)
        self.vertices.append(newVertex)
        return newVertex
    
    def getVertices(self):
        return self.vertices
    
    def addEdge(self,v1,v2,w=0):
        if not self.weighted:
            w=0
        v1.addEdge(v2,w)
        if not self.directed:
            v2.addEdge(v1,w)

if __name__=="__main__":
    graph=GraphList(True,False)
    ch=graph.addVertex("Chennai")
    dl=graph.addVertex("Delhi")
    mb=graph.addVertex("Mumbai")
    graph.addEdge(ch,dl,800)
    graph.addEdge(ch,mb,400)
    print(graph)
    #print(ch.getEdges())
