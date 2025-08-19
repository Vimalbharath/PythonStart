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

    def display(self):
        node=self.head
        while not node==None:
            print(node.val,"->",end="")
            node=node.next
        print("END")

def main():
    list=LinkedList()
    list.addFirst(0)
    list.addFirst(1)
    list.addFirst(2)
    list.display()

if __name__=="__main__":
    main()
        
