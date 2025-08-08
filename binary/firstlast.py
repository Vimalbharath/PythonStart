#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        ans[0]=self.search(nums,target,True)
        ans[1]=self.search(nums,target,False)
        return ans
        
    def search(self,nums,target,first):
        s,e=0,len(nums)-1
        
        ans=-1
        while s<=e:
            m=s+(e-s)//2
            if nums[m]<target:
                s=m+1
            elif nums[m]>target:
                e=m-1
            else:
                if(first):
                    e=m-1
                else:
                    s=m+1
                   
                ans=m
        return ans