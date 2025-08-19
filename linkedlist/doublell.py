class DoubleLL:
    class Node:
        def __init__(self,val):
            self.val=val
            self.prev=None
            self.next=None

    def __init__(self):
        self.head=None
        self.size=0

    def insertFirst(self,val):
        node=self.Node(val)
        node.next=self.head
        if not self.head==None:
            self.head.prev=node
        self.head=node
        self.size=self.size+1

    def display(self):
        node=self.head
        last=None
        while not node==None:
            print(node.val,"->",end="")
            last=node
            node=node.next   
        print("END")
        while not last==None:
            print(last.val,"->",end="")
            last=last.prev
        print("START")

def main():
    list=DoubleLL()
    list.insertFirst(1)
    list.insertFirst(2)
    list.insertFirst(3)
    list.display()

if __name__=="__main__":
    main()
