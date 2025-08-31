#https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    diameter=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global diameter
        diameter=0
        self.height(root)
        return diameter-1

    def height(self,node):
        if node==None:
            return 0
        global diameter
        left=self.height(node.left)
        right=self.height(node.right)
        dia=right+left+1
        diameter=max(dia,diameter)
        return max(right,left)+1