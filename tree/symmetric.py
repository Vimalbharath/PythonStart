#https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue=deque([root])
        node=queue.popleft()
        queue.append(node.left)
        queue.append(node.right)
        while queue:    
            l=queue.popleft()
            r=queue.popleft()
            if l==None and r==None:
                continue
            if l==None or r==None:
                return False
            if not l.val == r.val:
                return False
            queue.append(l.left)
            queue.append(r.right)
            queue.append(l.right)
            queue.append(r.left)
        return True
