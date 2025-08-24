#https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        leftnode=self.find(left)
        rightnode=self.find(right)

    def rev(self,prev,pres,next):
        pass

    def find(self,x):
        node=self.head
        while not node.val==x:
            node=node.next
        return node