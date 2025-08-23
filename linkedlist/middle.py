#https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        return s