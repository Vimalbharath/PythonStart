#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i,n=0,len(nums)
        while i<n:
            actual=i
            if nums[i]<n and nums[i]!=actual:
                self.swap(nums,i,nums[i])
            else:
                i=i+1
        for i in range(n):
            if i!=nums[i]:
                return i
        return n

    def swap(self,nums,f,s):
        nums[f],nums[s]=nums[s],nums[f]