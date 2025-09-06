#https://leetcode.com/problems/keys-and-rooms/description/?envType=problem-list-v2&envId=graph

from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False]*len(rooms)
        visited[0]=True
        ans=1
        queue=deque([[rooms[0]]])
        while queue:
            current=queue.popleft()
            for a in current:
                if not visited[a]:
                    visited[a]=True
                    queue.append(a)
                    ans+=1
        return ans==len(rooms)
