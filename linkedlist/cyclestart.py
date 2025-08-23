# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodefound=self.cycleat(head)
        length=self.cyclelength(head)
        if length ==-1: return None
        temp=head
        s=head
        while length > 0:
            temp=temp.next
            length=length-1
        f=temp
        while not f==s:
            f=f.next
            s=s.next
        return s
    
    def cyclelength(self,head):
        f=head
        s=head
        while f and f.next:
            f=f.next.next
            s=s.next
            if f==s:
                s=s.next
                count=1
                while not f == s:
                    count=count+1
                    s=s.next
                return count
        return -1

    def cycleat(self,head):
        f=head
        s=head
        while f and f.next:
            f=f.next.next
            s=s.next
            if f==s:
                s=s.next
                count=1
                while not f == s:
                    count=count+1
                    s=s.next
                return f
        return None

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
    input_list = [1, 1, 2]
    head = create_linked_list(input_list)

    print("Input linked list:")
    print_linked_list(head)

    solution = Solution()
    result_head = solution.deleteDuplicates(head)
