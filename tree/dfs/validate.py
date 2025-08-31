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
        return self.helper(root,None,None)
    def helper(self,node,low,high):
        if not node:
            return True
        left=False
        if not low or low.val<node.val:
            left=self.helper(node.left,low,node)
        return  left
