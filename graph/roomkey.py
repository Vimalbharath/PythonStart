#https://leetcode.com/problems/keys-and-rooms/description/?envType=problem-list-v2&envId=graph

from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False]*len(rooms)
        visited[0]=True
        ans=1
        queue=deque()
        for b in rooms[0]:
            queue.append(b)
            visited[b]=True
            ans+=1

        while queue:
            current=queue.popleft()
            for a in rooms[current]:
                if not visited[a]:
                    visited[a]=True
                    queue.append(a)
                    ans+=1
        return ans==len(rooms)
    
if __name__=="__main__":
    sol=Solution()
    print(sol.canVisitAllRooms([[1],[2],[3],[]]))
