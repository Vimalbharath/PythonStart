class Binarytree:
    class Node:
        def __init__(self,val):
            self.val=val
            self.left=None
            self.right=None
            self.height=0
        
    def __init__(self):
        self.head=None

    def insert(self,val):
        self.head=self.inserthelper(val,self.head)

    def inserthelper(self,val,node):
        newnode=self.Node(val)
        if not node:
            node=newnode
            return node
        if val<node.val:
            node.left=self.inserthelper(val,node.left)
        else:
            node.right=self.inserthelper(val,node.right)
        return node
    
    def preorder(self,node):
        if not node:
            return
        self.preorder(node.left)
        print(node.val)
        self.preorder(node.right)

if __name__=="__main__":
    tree=Binarytree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(2)
    tree.insert(4)
    tree.insert(1)
    tree.insert(7)
    tree.insert(9)
    tree.preorder(tree.head)
        
        



