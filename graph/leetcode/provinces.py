from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False]*n
        provinces=0
        queue=deque()
        for i in range(n):
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                provinces+=1
            while queue:
                current=queue.popleft()
                for j in range(n):
                    if isConnected[current][j] and not current==j and not visited[j]:
                        queue.append(j)
                        visited[j]=True
        return provinces

if __name__=="__main__":
    sol=Solution()
    print(sol.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))