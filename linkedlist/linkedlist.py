class LinkedList:
    class Node:
        def __init__(self,val) :
            self.val=val
            self.next=None

        def __str__(self):
            return str(self.val)
    
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

    def addrec2(self,val,index):
        self.head=self.helper2(val,index,self.head)
        return self.head
    
    def helper2(self,val,index,node):
        if index==0:
            temp=self.Node(val)
            temp.next=node
            return temp
        node.next=self.helper2(val,index-1,node.next)
        return node
        

    def addrec(self,val,index):
        temp=self.head
        self.helper(val,index,self.head)

    def helper(self,val,index,temp):
        if index==0:
            node=self.Node(val)
            self.size=self.size+1
            node.next=self.head
            self.head=node
            return
        if index==1:
            node=self.Node(val)
            self.size=self.size+1
            node.next=temp.next
            temp.next=node
            return
        self.helper(val,index-1,temp.next)
        
    def nodeat(self,index):
        node=self.head
        while index>0:
            node=node.next
            index=index-1
        return node
        
    def deletefirst(self):
        if self.head==None:
            print("List is Empty")
            return
        self.head=self.head.next
        if self.head==None:
            self.tail=None
        self.size=self.size-1

    def deletelast(self):
        if self.size<=1:
            self.deletefirst()
            return
        prev=self.nodeat(self.size-2)
        self.tail=prev
        prev.next=None
        self.size=self.size-1

    def reverse1(self,node):
        if not node.next:
            self.tail=node
            self.head=node
            return
        
        self.reverse1(node.next)
        self.tail.next=node
        self.tail=node
        self.tail.next=None
        
        

    def reverse2(self,head):
        if head==None:
            return None
        p,f,s=None,head,head.next
        while s:
           f.next=p
           p=f
           f=s
           s=s.next 
        f.next=p
        self.head=f

    def find(self,x):
        node=self.head
        while not node.val==x:
            node=node.next
        return node
        
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
    list.addlast(3)
    list.addatindex(100,1)
    list.addatindex(200,0)
    list.addatindex(300,6)
    # list.addrec2(100,1)
    # list.addrec2(200,0)
    # list.addrec2(300,6)
    # list.deletefirst()
    # list.deletefirst()
    # list.deletelast()
    # list.deletelast()
    # list.deletelast()
    # list.deletelast()
    # list.deletelast()
    # list.deletelast()
    list.display()
    list.reverse2(list.head)
    print(list.find(1))
    list.display()

if __name__=="__main__":
    main()
        
