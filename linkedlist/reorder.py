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
                temp2=newmid.next
                newmid.next=temp1
                newmid=temp2
                node=node.next.next
            
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
# Helper function to create a linked list from a Python list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    nodes = []
    current = head
    while current:
        nodes.append(str(current.val))
        current = current.next
    print(" -> ".join(nodes))

# --- Main part to run the example ---

if __name__ == '__main__':
    # Example 1: Input: head = [1, 1, 2]
    input_list = [1,2,3,2,1]
    head = create_linked_list(input_list)

    print("Input linked list:")
    print_linked_list(head)

    solution = Solution()
    solution.reorderList(head)
    
   
    
    print("\nLinked list after reorder:")
    print_linked_list(head)      
