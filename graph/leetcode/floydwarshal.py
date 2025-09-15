#https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/?envType=problem-list-v2&envId=graph

from typing import List
import math

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[math.inf]*n]*n
        for i in range(n):
            for j in range(n):
                if i==j:
                    dist[i][i]=0
        print(dist)


if __name__=="__main__":
    sol=Solution()
    n = 4
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    distanceThreshold = 4
    sol.findTheCity(n,edges,distanceThreshold)