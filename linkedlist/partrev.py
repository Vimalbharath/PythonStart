#https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        previous,current=None,head
        dummyleft=left
        while dummyleft>1 and current:
            previous=current
            current=current.next
            dummyleft=dummyleft-1

        last=previous
        newEnd=current

        bet=(right-left)+1
        next=current.next
        while bet>0 and current:
            current.next=previous
            previous=current
            current=next
            if current:
                next=next.next
            bet=bet-1
        if last:
            last.next=previous
        else:
            head=previous#self.head removed

        newEnd.next=current
        return head
