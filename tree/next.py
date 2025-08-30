#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
"""
from typing import List, Optional
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        return self.helper(root)
    def helper(self,node):
        if not node:
            return node
        leftmost=None
        while node:
            if node.left:
                if leftmost==None:
                    leftmost=node.left
                node.left.next=node.right
            if node.next:
                if node.right:
                    node.right.next=node.next.left
            else:
                if node.right:
                    node.right.next=None
            node=node.next
        self.helper(leftmost)
        return node
# --- Helper function to build a perfect binary tree for testing ---
def build_tree(nodes: List[Optional[int]]) -> Optional[Node]:
    if not nodes or nodes[0] is None:
        return None
    
    root = Node(nodes[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(nodes):
        current_parent = queue.popleft()
        
        # Build left child
        if i < len(nodes) and nodes[i] is not None:
            current_parent.left = Node(nodes[i])
            queue.append(current_parent.left)
        i += 1
        
        # Build right child
        if i < len(nodes) and nodes[i] is not None:
            current_parent.right = Node(nodes[i])
            queue.append(current_parent.right)
        i += 1
        
    return root

# --- Main execution block ---
if __name__ == "__main__":
    # Create a perfect binary tree
    #      1
    #     / \
    #    2   3
    #   / \ / \
    #  4  5 6  7
    
    perfect_tree_nodes = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(perfect_tree_nodes)
    
    print("Original tree constructed.")
    
    # Connect the next pointers
    solution = Solution()
    solution.connect(root)