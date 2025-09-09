import sys
import os

# Add the project's root directory to the system path
# This moves up two levels from the current file's location
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Now, you can use a normal absolute import from the project root
# Now, you can use a normal absolute import from the project root
from graph import unionfind

if __name__=="__main__":
    dsu=unionfind.DSU(6)
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
    