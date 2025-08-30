#https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        ans=[]
        queue=deque([root])
        while queue:
            size=len(queue)
            avg=0
            for i in range(size):
                currentnode=queue.popleft()
                if currentnode.left:
                    queue.append(currentnode.left)
                if currentnode.right:
                    queue.append(currentnode.right)
                avg=avg+currentnode.val
            avg=avg/size
            ans.append(avg)
        return ans