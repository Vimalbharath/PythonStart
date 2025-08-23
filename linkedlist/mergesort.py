#https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergesort(head)

    def mergesort(self,node):
        if not node:
            return None
        if not node.next:
            return ListNode(node.val)
        mid=self.middle(node)
        temp=node
        while not temp.next==mid:
            temp=temp.next
        temp.next=None
        list1=node
        list2=mid
        ans=self.mergesorted(list1,list2)
        return ans
    def middle(self,head):
        f=head
        s=head
        while f and f.next:
            f=f.next.next
            s=s.next
        return s

    def mergesorted(self,list1,list2):
        node=ListNode()
        while list1 and list2:
            if list1.val<=list2.val:
                node.next=ListNode(list1.val)
                node=node.next
                list1=list1.next
            else:
                node.next=ListNode(list2.val)
                node=node.next
                list2=list2.next
        while list1:
            node.next=ListNode(list1.val)
            node=node.next
            list1=list1.next
        while list2:
                node.next=ListNode(list2.val)
                node=node.next
                list2=list2.next
        return node.next
    
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
    input_list = [4,2,1,3]
    head = create_linked_list(input_list)

    print("Input linked list:")
    print_linked_list(head)

    solution = Solution()
    result_head = solution.sortList(head)

    print("\nLinked list after removing duplicates:")
    print_linked_list(result_head)
