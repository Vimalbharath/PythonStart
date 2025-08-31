#https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root)
        return root
    def helper(self,node):
        if not node:
            return node
        temp=node.left
        node.left=self.helper(node.right)
        node.right=self.helper(temp)
        return node