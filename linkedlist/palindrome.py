#https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next==None: return True
        mid=self.middle(head)
        newmid=self.reversehalf(head,mid)
        #mid=self.middle(head)
        while newmid :
            if not head.val==newmid.val:
                return False
            head=head.next
            newmid=newmid.next
        return True
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
    result = solution.isPalindrome(head)
    print(result)
   
    
    print("\nLinked list after half reverse:")
    print_linked_list(head)