class Segment:
    class Node:
        def __init__(self,startInterval,endInterval):
            self.data=0
            self.startInterval=startInterval
            self.endInterval=endInterval
            self.left=None
            self.right=None

    def __init__(self,nums) :
        self.head=self.constructTree(nums,0,len(nums)-1)
        pass
    
    def constructTree(self,nums,start,end):
        pass

    def update(self,index,val):
        pass

    def getsum(self,left,right):
        pass

if __name__=="__main__":
    nums=[0,1,2,3,4,5,6]
    seg=Segment(nums)
    print(seg.getsum(1,4))
        
