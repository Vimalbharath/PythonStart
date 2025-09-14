# https://leetcode.com/problems/course-schedule/description/?envType=problem-list-v2&envId=graph

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ans=[]
        indegree=[0]*numCourses
        for edge in prerequisites:
            indegree[edge[1]]+=1
        queue=deque()
        for i,deg in enumerate(indegree):
            if deg==0:
                queue.append(i)
        while queue:
            current=queue.popleft()
            ans.append(current)
            for edge in prerequisites:
                if edge[0]==current:
                    indegree[edge[1]]-=1
                    if indegree[edge[1]]:
                        queue.append(edge[1])
        return len(ans)==numCourses