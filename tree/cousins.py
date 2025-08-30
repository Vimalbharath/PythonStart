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

    def siblings(self,node,x,y):
        return self.parent(node,x)==self.parent(node,y) 

    def parent(self,node,x):
        if not node:
            return node
        if node.left:
            if node.left.val==x :
                return node
            self.parent(node.left,x)
        if node.right:
            if node.right.val==x:
                return node
            self.parent(node.right,x)

        