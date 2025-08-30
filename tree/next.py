#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
"""
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        return self.helper(root)
    def helper(self,node):
        if not node:
            return node
        leftmost=node.left
        while node:
            node.left.next=node.right
            if node.next:
                node.right.next=node.next.left
            else:
                node.right.next=None
            node=node.next
        return self.helper(leftmost)