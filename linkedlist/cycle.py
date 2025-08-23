#https://leetcode.com/problems/linked-list-cycle/description/?source=submission-ac

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f=head
        if not f: return False
        if not f.next: return False
        s=head.next  
        while f and s:
            if f ==s:
                return True
            f=f.next
            if s.next:
                s=s.next.next
            else:
                return False
