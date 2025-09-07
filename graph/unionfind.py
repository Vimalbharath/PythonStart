class DSU:
    def __init__(self,n):
        self.parent=[0]*n
        self.rank=[0]*n

    def make_set(self,x):
        self.parent[x]=x

    def find(self,x):
        if not self.parent[x]==x:
            self.parent[x] =self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        xx=self.find(x)
        yy=self.find(y)
        if xx==yy:
            return
        if self.rank[xx]>self.rank[yy]:
            self.parent[yy]=xx
        else:
            self.parent[xx]=yy
            if self.rank[xx]==self.rank[yy]:
                self.rank[yy]+=1

if __name__=="__main__":
    dsu=DSU(6)
    for i in range(6):
        dsu.make_set(i)
    edges=[[0,1],[0,2],[1,3],[3,4],[4,5]]
    for edge in edges:
        x=dsu.find(edge[0])
        y=dsu.find(edge[1])
        if x==y:
            print("Cycle Present")
            break
        else:
            dsu.union(edge[0],edge[1])
    else:
        print("No Cycle")
    