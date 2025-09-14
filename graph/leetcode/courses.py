# https://leetcode.com/problems/course-schedule/description/?envType=problem-list-v2&envId=graph

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build the adjacency list and indegree array
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            # Correctly represent the dependency: prereq -> course
            adj[prereq].append(course)
            indegree[course] += 1
            
        # 2. Initialize the queue with all nodes having an indegree of 0
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        processed_count = 0
        
        # 3. Process the queue
        while queue:
            current = queue.popleft()
            processed_count += 1
            
            # For each neighbor (dependent course) of the current node
            for neighbor in adj[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. Check for a cycle
        return processed_count == numCourses