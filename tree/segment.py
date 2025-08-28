class Segment:
    class Node:
        def __init__(self,val=0):
            self.val=val
            self.left=None
            self.right=None

    def __init__(self) :
        self.head=None
    
    def insert(self,val):
        pass

    def delete(self,val):
        pass

    def getsum(self,left,right):
        pass

if __name__=="__main__":
    seg=Segment()
    nums=[0,1,2,3,4,5,6]
    for num in nums:
        seg.insert(num)
    print(seg.getsum(1,4))
        
