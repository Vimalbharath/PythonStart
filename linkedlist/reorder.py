#https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next==None: return
        mid=self.middle(head)
        newmid=self.reversehalf(head,mid)
        node=head
        
        temp1=None
        while newmid and node:
           
                temp1=node.next
                node.next=newmid
                newmid=newmid.next
                node=node.next
                node.next=temp1
            
    def middle(self,head):
        f,s=head,head
        while f and f.next:
            f=f.next.next
            #if f and f.next:
            s=s.next
        return s

    def reversehalf(self,node,mid):
        prev,present,next=None,mid,mid.next
        # while not present==mid:
        #     prev=present
        #     present=next
        #     next=next.next

        # last=prev
        # newEnd=present

        while present:
            present.next=prev
            prev=present
            present=next
            if next:
                next=next.next
        return prev
        # if last:
        #     last.next=prev
        # else:
        #     self.head=prev
        # newEnd.next=present
        
