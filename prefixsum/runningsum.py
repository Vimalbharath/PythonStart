#https://leetcode.com/problems/running-sum-of-1d-array/description/?envType=problem-list-v2&envId=prefix-sum

from typing import List


class Solution:
    #N^2 complexity
    def runningSum1(self, nums: List[int]) -> List[int]:
        ans=[0 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i+1):
                ans[i]+=nums[j]
        return ans
    
    #N complexity
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[0 for i in range(len(nums))]
        ans[0]=nums[0]
        for i in range(1,len(nums)):
            ans[i]=ans[i-1]+nums[i]
        return ans