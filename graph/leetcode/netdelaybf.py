#https://leetcode.com/problems/network-delay-time/

import math
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[math.inf]*n for _ in range(n)]
        for edge in times:
            adj[edge[0]-1][edge[1]-1]=edge[2]
            #adj[edge[0]-1][edge[1]-1]=edge[2]
        key=[math.inf]*(n)
        key[k-1]=0
        
        # for i in range(n):
        #     for j in range(n):
        #         if i==j:
        #             adj[i][i]=0
        print(adj)
        for _ in range(n-1):
            for i in range(n):
                for j in range(n):
                    weight=adj[i][j]
                    if weight != math.inf :
                         if key[i] != math.inf and key[i] + weight < key[j]:
                             key[j]=key[i]+weight

        print(key)
        ans=-1
        for k in key:
            if k==math.inf:
                print(-1)
                return
            else:
                ans=max(ans,k)
        print(ans)



if __name__=="__main__":
    sol=Solution()
    times = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
    n = 5
    k = 5
    sol.networkDelayTime(times,n,k)