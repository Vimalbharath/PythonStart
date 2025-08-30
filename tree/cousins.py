#https://leetcode.com/problems/cousins-in-binary-tree/description/

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        return self.level(x,root)==self.level(y,root) and not self.siblings(root,x,y)

    def level(self,x,root):
        queue=deque([root])
        level=0
        while queue:
            size=len(queue)
            for _ in range(size):
                current=queue.popleft()
                if current.val==x:
                    return level+1
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level=level+1

        return level

    def siblings(self, node, x, y):
        if not node or (not node.left and not node.right):
            return False
        
        # Check if the current node's children are the sibling pair
        if node.left and node.right:
            if (node.left.val == x and node.right.val == y) or \
            (node.left.val == y and node.right.val == x):
                return True
                
        # Recursively search the left and right subtrees
        return self.siblings(node.left, x, y) or self.siblings(node.right, x, y)       