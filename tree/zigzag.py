#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        queue=deque([root])
        reverse=False
        while queue:
            size=len(queue)
            level=[]
            if reverse:
                for _ in range(size):
                    currentnode=queue.pop()
                    level.append(currentnode.val)
                    if currentnode.right:
                        queue.appendleft(currentnode.right)
                    if currentnode.left:
                        queue.appendleft(currentnode.left)
                reverse=not reverse
            else:
                for _ in range(size):
                    currentnode=queue.popleft()
                    level.append(currentnode.val)
                    if currentnode.left:
                        queue.append(currentnode.left)
                    if currentnode.right:
                        queue.append(currentnode.right)
                reverse=not reverse
            ans.append(level)
        return ans