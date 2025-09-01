# https://leetcode.com/problems/kth-smallest-element-in-a-bst/ 
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        self.helper(root,k,ans)
        return ans[k-1]

    def helper(self,root,k,queue):
        if not root:
            return None
        self.helper(root.left,k,queue)
        queue.append(root.val)
        self.helper(root.right,k,queue)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count=0
        return self.helper(root,k).val
        #return ans[k-1]

    def helper(self,root,k):
        if not root:
            return None
        left=self.helper(root.left,k)
        if left:
            return left
        self.count=self.count+1
        if self.count==k:
            return root
        return self.helper(root.right,k)
        