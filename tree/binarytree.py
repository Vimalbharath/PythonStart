class Binarytree:
    class Node:
        def __init__(self,val):
            self.val=val
            self.left=None
            self.right=None
            self.height=0
        
    def __init__(self):
        self.head=None
        
    def insert(self,val,node):
        newnode=self.Node(val)
        if not node:
            node=newnode
            return node
        if val<self.node.val:
            node.left=self.insert(val,node.left)
        else:
            node.right=self.insert(val,node.right)
        return node
    
    def preorder(self,node):
        if not node:
            return
        self.preorder(node.left)
        print(node.val)
        self.preorder(node.right)

if __name__=="__main__":
    tree=Binarytree()
    tree.insert(5,tree.head)
    tree.insert(4,tree.head)
    tree.insert(3,tree.head)
    tree.insert(7,tree.head)
    tree.insert(9,tree.head)
    tree.preorder(tree.head)
        
        



