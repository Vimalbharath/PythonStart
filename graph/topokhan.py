from dfslist import GraphListBFS
from collections import deque

class GraphListBFS1(GraphListBFS):
    def khan(self):
      ans=[]
      vertices=self.vertices
      inDegree=[0]*len(vertices)
      for vertex in vertices:
         edges=vertex.getEdges2()
         for edge in edges:
            pos=vertices.index(edge.v2)
            inDegree[pos]+=1
      print(inDegree)
      for i in range(len(inDegree)):
         if not inDegree[i]:
            ans.append(vertices[i].name)
            edges=vertices[i].getEdges2()
            for edge in edges:
                pos=vertices.index(edge.v2)
                inDegree[pos]-=1
      print(inDegree)
      print(ans)

    def khan2(self):
        # A topological sort requires a directed graph.
        if not self.directed:
            print("Error: Khan's algorithm requires a directed graph.")
            return

        ans = []
        in_degree = {v.name: 0 for v in self.vertices}
        vertex_map = {v.name: v for v in self.vertices}

        # Step 1: Compute in-degrees for all vertices
        for vertex in self.vertices:
            for edge in vertex.getEdges2():
                in_degree[edge.v2.name] += 1

        # Step 2: Initialize queue with all vertices with an in-degree of 0
        queue = deque([v for v in self.vertices if in_degree[v.name] == 0])

        # Step 3: Process the queue
        while queue:
            u = queue.popleft()
            ans.append(u.name)

            for edge in u.getEdges2():
                v = edge.v2
                in_degree[v.name] -= 1
                if in_degree[v.name] == 0:
                    queue.append(v)

        # Step 4: Check for a cycle
        if len(ans) == len(self.vertices):
            print("No cycle present.")
            print("Topological Sort Order:", ans)
        else:
            print("Cycle present. Topological sort is not possible.")


if __name__=="__main__":
    graph=GraphListBFS1(True,True)
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
    graph.addEdge(kl,dl,6000)
    graph.addEdge(sl,sg,5000)
    graph.addEdge(bg,sg,6000)
    print(graph)
    graph.dfs()
    graph.dfs2()
    graph.khan()
    graph.khan2()

    