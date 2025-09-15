#https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/?envType=problem-list-v2&envId=graph

from typing import List
import math

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[math.inf] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    dist[i][i]=0
        for edge in edges:
            dist[edge[0]][edge[1]]=edge[2]
            dist[edge[1]][edge[0]]=edge[2]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # if dist[i][j]> dist[i][k]+dist[k][j]:
                        dist[i][j]=min((dist[i][k]+dist[k][j]),dist[i][j])
        print(dist)
        ans=[0]*n
        for i in range(n):
            for j in range(n):
                if dist[i][j]<= distanceThreshold and not dist[i][j]==0:
                    ans[i]+=1
        print(ans)
        temp=math.inf
        for i in range(len(ans)):
            temp=min(ans[i],temp)
        print(temp)
        temp2=0
        for i in range(len(ans)):
            if ans[i]==temp:
                temp2=max(temp2,i)
        print(temp2)



if __name__=="__main__":
    sol=Solution()
    n = 4
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    distanceThreshold = 4
    sol.findTheCity(n,edges,distanceThreshold)