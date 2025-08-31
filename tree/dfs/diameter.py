#https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        # Initialize an instance variable to store the diameter
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.diameter-1

    def height(self,node):
        if node==None:
            return 0
        left=self.height(node.left)
        right=self.height(node.right)
        dia=right+left+1
        self.diameter=max(dia,self.diameter)
        return max(right,left)+1