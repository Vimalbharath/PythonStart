#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.head=None

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.binary(nums,0,len(nums)-1)
        return self.head

    def binary(self,nums,start,end):
        if(start>end):
            return
        mid=start+(end-start)//2
        self.head=self.insert(nums[mid],self.head)
        self.binary(nums,start,mid-1)
        self.binary(nums,mid+1,end)

    def insert(self,val,node):
        if not node:
            node=TreeNode(val)
            return  node
        if node.val>val:
            node.left=self.insert(val,node.left)
        else:
            node.right=self.insert(val,node.right)
        return node
