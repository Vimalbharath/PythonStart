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
        if start==end:
            node=self.Node(start,end)
            node.data=nums[start]
            return node
        node=self.Node(start,end)
        m=start+(end-start)//2
        node.left=self.constructTree(nums,start,m)
        node.right=self.constructTree(nums,m+1,end)
        node.data=node.left.data+node.right.data
        return node

    def update(self,index,val):
        pass

    def getsum(self,left,right):
        pass

    def preorder(self,node):
        if not node:
            return
        self.preorder(node.left)
        print(node.data,node.startInterval,node.endInterval)
        self.preorder(node.right)


if __name__=="__main__":
    nums=[0,1,2,3,4,5,6]
    seg=Segment(nums)
    print(seg.getsum(5,6))
    seg.preorder(seg.head)
        
