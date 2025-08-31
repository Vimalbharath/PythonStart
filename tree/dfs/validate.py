#https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left,right=True,True
        if root.left:
            if root.left.val<root.val:
                left=self.isValidBST(root.left)
            else:
                left=False
        if root.right:
            if root.right.val>root.val:
                right=self.isValidBST(root.right)
            else:
                right=False
        return left and right
