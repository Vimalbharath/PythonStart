#https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[]
        queue=deque([root])
        while queue:
            size=len(queue)
            level=[]
            for _ in range(size):
                current=queue.popleft()
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            ans.append(level.pop())
        return ans
