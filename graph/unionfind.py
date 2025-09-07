class DSU:
    def __init__(self):
        self.parent=[]

    def make_set(self,x):
        self.parent[x]=x

    def find(self,x):
        return self.parent[x]
    
    def union(self,x,y):
        xx=self.find(x)
        yy=self.find(y)
        if xx==yy:
            return
        self.parent[x]=y