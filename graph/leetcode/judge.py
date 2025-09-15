#https://leetcode.com/problems/find-the-town-judge/description/?envType=problem-list-v2&envId=graph

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n==1:
                return 1
            return -1
        outdegree=[0]*n
        indegree=[0]*n
        for edge in trust:
            outdegree[edge[0]-1]+=1
            indegree[edge[1]-1]+=1
        for i in range(n):
            if outdegree[i]==0 and indegree[i]==n-1:
                return i+1
        return -1