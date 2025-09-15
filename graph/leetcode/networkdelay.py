#https://leetcode.com/problems/network-delay-time/

import math
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[]*n for _ in range(n)]
        for edge in times:
            adj[edge[0]-1].append((edge[1],edge[2]))
        key=[math.inf]*n
        key[k-1]=0
        minheap=[(key[k-1],k)]
        print(adj)
        while minheap:
            currdist,u=heapq.heappop(minheap)
            for adjedge in adj[u-1] :
                v=adjedge[0]
                l=adjedge[1]
                if key[v-1]>currdist+l:
                    key[v-1]=min(currdist+l,key[v-1])
                    heapq.heappush(minheap,(key[v-1],v))
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
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 1
    sol.networkDelayTime(times,n,k)