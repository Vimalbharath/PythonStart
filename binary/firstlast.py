#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s,e=0,len(nums)-1
        
        while s<=e:
            m=s+(e-s)//2
            if nums[m]<target:
                s=m+1
            elif nums[m]>target:
                e=m-1
            else:
                if nums[m+1]==target:
                    return [m,m+1]
                if nums[m-1]==target:
                    return [m-1,m]
        return [-1,-1]
