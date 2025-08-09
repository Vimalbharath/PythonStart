#https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot=self.pivot(nums)
        if pivot==-1:
            return self.binary(nums,target,0,len(nums)-1)
        first=self.binary(nums,target,0,pivot)
        if first==-1:
            return self.binary(nums,target,pivot+1,len(nums)-1)
        else:
            return first
    
    def binary(self,nums,target,s,e):
        while s<=e:
            m=s+(e-s)//2
            if nums[m]>target:
                e=m-1
            elif nums[m]<target:
                s=m+1
            else:
                return m
        return -1
    
    def pivot(self,nums):
        s,e=0,len(nums)-1
        while s<=e:
            m=s+(e-s)//2
            if m<e and nums[m]>nums[m+1]:
                return m
            if m>s and nums[m-1]>nums[m]:
                return m-1
            if nums[s]>nums[m]:
                e=m-1
            else:
                s=m+1
        return -1