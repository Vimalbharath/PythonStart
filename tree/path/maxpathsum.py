#https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        self.helper(root)
        return self.ans
    def helper(self,root):
        if not root:
            return 0
        left=self.helper(root.left)
        right=self.helper(root.right)
        nodesum=root.val+left+right
        if self.ans<nodesum:
            self.ans=nodesum
        return nodesum
