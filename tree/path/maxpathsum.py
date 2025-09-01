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
        self.ans=-2**1000
        self.helper(root)
        return self.ans
    def helper(self,root):
        if not root:
            return 0
        left=self.helper(root.left)
        right=self.helper(root.right)
        nodesum=root.val+left+right
        leftpath=root.val+left
        rightpath=root.val+right
        if self.ans<leftpath:
            self.ans=leftpath
        if self.ans<rightpath:
            self.ans=rightpath
        if self.ans<root.val:
            self.ans=root.val
        if self.ans<nodesum:
            self.ans=nodesum
        return nodesum
