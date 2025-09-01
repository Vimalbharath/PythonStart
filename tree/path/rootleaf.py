#https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        return self.helper(root,0)

    def helper(self,root,pathsum):
        if not root:
            return 0

        pathsum=(pathsum*10)+root.val

        if not root.left and not root.right:
            return pathsum

        
        return self.helper(root.left,pathsum)+self.helper(root.right,pathsum)