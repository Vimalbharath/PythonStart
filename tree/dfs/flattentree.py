#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        node=root
        if node.left:
            left=node.left
            right=node.right

            node.left=None
            node.right=left
            while node.right:
                node=node.right
            node.right=right
        self.flatten(root.right)