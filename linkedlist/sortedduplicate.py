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
        while not node == None  :
            while not node.next == None and node.next.val==node.val :
                node.next=node.next.next
            node=node.next
        return head

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

   
    
    print("\nLinked list after removing duplicates:")
    print_linked_list(result_head)