class AVL:
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
        if not node:
            newnode=self.Node(val)
            node=newnode
            return node
        if val<node.val:
            node.left=self.inserthelper(val,node.left)
        else:
            node.right=self.inserthelper(val,node.right)
        node.height=max(self.height(node.left),self.height(node.right))+1
        return self.rotate(node)
    
    def height(self,node):
        if node:
            return node.height
        else:
            return 0
    
    def rotate(self,node):
        # if self.bal(node):
        #     return node
        if self.height(node.left)-self.height(node.right)>1:
            #left heavy
            if self.height(node.left.left)-self.height(node.left.right)>0:
                #left left
                return self.rotateRight(node)
            else:
                #left right
                node.left=self.rotateLeft(node.left)
                return self.rotateRight(node)
        if self.height(node.left)-self.height(node.right)<-1:
            #right heavy
            if self.height(node.right.right)>self.height(node.right.left):
                #right right
                return self.rotateLeft(node)
            else:
                #right left
                node.right=self.rotateRight(node.right)
                return self.rotateLeft(node)
        return node
        
    def rotateRight(self,node):
        p=node
        c=p.left
        temp=c.right
        c.right=p
        p.left=temp

        p.height=max(self.height(p.left),self.height(p.right))+1
        c.height=max(self.height(c.left),self.height(c.right))+1
        return c
    
    def rotateLeft(self,node):
        c=node
        p=c.right
        temp=p.left
        p.left=c
        c.left=temp

        p.height=max(self.height(p.left),self.height(p.right))+1
        c.height=max(self.height(c.left),self.height(c.right))+1
        return p
    
    def balanced(self):
        return self.bal(self.head)
    def bal(self,node):
        if not node:
            return True
        return abs(self.height(node.left)-self.height(node.right))<=1 and self.bal(node.left) and self.bal(node.right)

    def preorder(self,node):
        if not node:
            return
        self.preorder(node.left)
        print(node.val,node.height)
        self.preorder(node.right)

if __name__=="__main__":
    tree=AVL()
    tree.insert(5)
    tree.insert(3)
    tree.insert(2)
    tree.insert(4)
    tree.insert(1)
    tree.insert(7)
    tree.insert(9)
    tree.insert(0)
    tree.preorder(tree.head)
    print(tree.balanced())
        
        



