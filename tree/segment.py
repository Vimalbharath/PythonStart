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
        self.head=self.updatehelper(index,val,self.head)
        return self.head
    def updatehelper(self,index,val,node):
        if node.startInterval==index and node.endInterval==index:
            node.data=val
            return node
        if index<node.startInterval or index>node.endInterval:
            return node
        node.left=self.updatehelper(index,val,node.left)
        node.right=self.updatehelper(index,val,node.right)
        node.data=node.left.data+node.right.data
        return node
    
    def getsum(self,left,right):
            return self.getsumhelper(left,right,self.head)

    def getsumhelper(self,left,right,node):
        if node.startInterval>right or node.endInterval<left:
            return 0
        if left<=node.startInterval and node.endInterval<=right:
            return node.data
           
        l=self.getsumhelper(left,right,node.left)
        r=self.getsumhelper(left,right,node.right)
        return l+r

       

    def preorder(self,node):
        if not node:
            return
        self.preorder(node.left)
        print(node.data,node.startInterval,node.endInterval)
        self.preorder(node.right)


if __name__=="__main__":
    nums=[0,1,2,3,4,5,6,7]
    seg=Segment(nums)
    print(seg.getsum(3,7))
    seg.preorder(seg.head)
    seg.update(7,8)
    print(seg.getsum(3,7))
    seg.preorder(seg.head)
        
