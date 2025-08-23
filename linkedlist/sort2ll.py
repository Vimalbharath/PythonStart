#https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode()
        head=ans
        while list1 and list2:
            if list1.val <=list2.val:
                ans.next=ListNode(list1.val)
                ans=ans.next
                list1=list1.next
            else:
                ans.next=ListNode(list2.val)
                ans=ans.next
                list2=list2.next
        while list1:
            ans.next=ListNode(list1.val)
            ans=ans.next
            list1=list1.next
        while list2:
            ans.next=ListNode(list2.val)
            ans=ans.next
            list2=list2.next
        return head.next