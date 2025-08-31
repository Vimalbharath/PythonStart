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
        if low and node.val <= low.val:
            return False
        if high and node.val >= high.val:
            return False
        left=self.helper(node.left,low,node)
        right=self.helper(node.right,node,high)
        
        return  left and right
