#https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return max(self.height(root),self.height(root.left),self.height(root.right))-1

    def height(self,node):
        if node==None:
            return 0
        left=self.height(node.left)
        right=self.height(node.right)
        return max(right,left)+1