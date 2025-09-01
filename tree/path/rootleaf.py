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
        self.ans=0
        self.pathsum=0
        self.helper(root,self.pathsum,self.ans)
        return self.ans

    def helper(self,root,pathsum,ans):
        if not root:
            return

        if not root.left and not root.right:
            self.ans=self.ans+self.pathsum

        self.pathsum=(self.pathsum*10)+root.val
        self.helper(root.left,self.pathsum,self.ans)
        self.helper(root.right,self.pathsum,self.ans)