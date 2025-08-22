#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
from typing import Optional



        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        node=head
        while not node == None and not node.next == None :
            if node.next.val==node.val:
                node.next=node.next.next
            node=node.next
        return head
