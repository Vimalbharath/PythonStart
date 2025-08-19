class LinkedList:
    class Node:
        def __init__(self,val) :
            self.val=val
            self.next=None
    
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def addFirst(self,val):
        node=self.Node(val)
        node.next=self.head
        self.head=node
        if self.head.next==None:
            self.tail=self.head
        self.size=self.size+1

    def addlast(self,val):
        if self.head==None:
            self.addFirst(val)
            return
        node=self.Node(val)
        self.tail.next=node
        self.tail=node
        self.size=self.size+1

    def addatindex(self,val,index):
        if index==0:
            self.addFirst(val)
            return 
        if index==self.size:
            self.addlast(val)
            return
        node=self.Node(val)
        prevnode=self.nodeat(index-1)
        node.next=prevnode.next
        prevnode.next=node
        self.size=self.size+1

    def nodeat(self,index):
        node=self.head
        while index>0:
            node=node.next
        return node
        
    def deletefirst(self):
        if self.head==None:
            print("List is Empty")
            return
        self.head=self.head.next
        if self.head==None:
            self.tail=None
        self.size=self.size-1
        
    def display(self):
        node=self.head
        while not node==None:
            print(node.val,"->",end="")
            node=node.next
        print("END")

def main():
    list=LinkedList()
    list.addFirst(0)
    # list.addFirst(1)
    # list.addFirst(2)
    # list.addlast(3)
    # list.addatindex(100,1)
    # list.addatindex(200,0)
    # list.addatindex(300,6)
    list.deletefirst()
    list.deletefirst()
    list.display()

if __name__=="__main__":
    main()
        
