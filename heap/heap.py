class Heap:
    def __init__(self):
        self.data=[]

    def __str__(self) -> str:
        ans=''
        for i in self.data:
            ans=ans+".."+str(i)
        return ans

    def insert(self,val):
        self.data.append(val)
        size=len(self.data)
        self.upheap(size-1)

    def upheap(self,index):
        if index==0:
            return
        parent=index-1//2
        if self.data[index]>self.data[parent]:
            self.data[index],self.data[parent]=self.data[parent],self.data[index]
            self.upheap(parent)

    def remove(self):
        ans=self.data[0]
        self.data[0]=self.data.pop()
        self.downheap(0)
        return ans
    
    def downheap(self,index):
        if index>(len(self.data)-2)//2:
            return
        leftchild=(index*2)-1
        rightchild=(index*2)
        if self.data[index]<self.data[leftchild]:
            self.data[index],self.data[leftchild]=self.data[leftchild],self.data[index]
            self.data(leftchild)
        if self.data[index]<self.data[rightchild]:
            self.data[index],self.data[rightchild]=self.data[rightchild],self.data[index]
            self.data(rightchild)

if __name__=="__main__":
    heap=Heap()
    heap.insert(0)
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    heap.insert(5)
    print(heap)
    print(heap.remove())
    print(heap.remove())
    print(heap.remove())
    print(heap.remove())
    print(heap.remove())