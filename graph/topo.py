from graphlist import GraphList
from collections import deque

class GraphListBFS(GraphList):
    def topo(self):
        vertices=self.vertices
        outDegree=[0]*len(self.vertices)
        inDegree=[0]*len(self.vertices)
        for i in range(len(vertices)):
            current=vertices[i]
            outDegree[i]=len(current.getEdges2())
        for vertex in vertices:
            edges=vertex.getEdges2()
            for e in edges:
                nextVertex=e.v2
                inDegree[vertices.index(nextVertex)]=inDegree[vertices.index(nextVertex)]+1
        print(inDegree)
        print(outDegree)

    def inout(self):
        # Using dictionaries for O(1) lookups
        in_degrees = {}
        out_degrees = {}

        # Initialize degrees and calculate out-degrees in a single pass
        for vertex in self.getVertices():
            in_degrees[vertex.name] = 0
            # Use the correct getEdges() method
            out_degrees[vertex.name] = len(vertex.getEdges2())

        # Calculate in-degrees by iterating through all edges
        for vertex in self.getVertices():
            
            for edge in vertex.getEdges2():
                # Correctly access the destination vertex
                next_vertex = edge.v2
                in_degrees[next_vertex.name] += 1
        
        print("In-degrees:", in_degrees)
        print("Out-degrees:", out_degrees)

if __name__=="__main__":
    graph=GraphListBFS(True,True)
    ch=graph.addVertex("Chennai")
    dl=graph.addVertex("Delhi")
    sl=graph.addVertex("SriLanka")
    mb=graph.addVertex("Mumbai")
    bg=graph.addVertex("Bangalore")
    kl=graph.addVertex("Kolkata")
    sg=graph.addVertex("Singapore")
    graph.addEdge(ch,dl,800)
    graph.addEdge(ch,mb,800)
    graph.addEdge(mb,bg,300)
    graph.addEdge(bg,kl,400)
    graph.addEdge(ch,sl,900)
    graph.addEdge(sl,sg,5000)
    graph.addEdge(bg,sg,6000)
    print(graph)
    graph.topo()
    graph.inout()
    