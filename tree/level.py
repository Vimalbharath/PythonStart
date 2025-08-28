#https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        node=root
        queue.append(node)
        ans=[]
        while len(queue)>0:
            a=len(queue)
            levelans=[]
            for i in range(1,a+1):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                levelans.append(queue.popleft().val)
            ans.append(levelans)
        return ans