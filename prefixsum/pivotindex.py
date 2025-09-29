# https://leetcode.com/problems/find-pivot-index/?envType=problem-list-v2&envId=prefix-sum

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        print(nums)
        sumLeft=[0 for i in range(len(nums))]
        sumRight=[0 for i in range(len(nums))]
        sumLeft[0]=nums[0]
        sumRight[len(nums)-1]=nums[len(nums)-1]
        for i in range(1,len(nums)):
            sumLeft[i]=sumLeft[i-1]+nums[i]
            sumRight[len(nums)-1-i]=sumRight[len(nums)-i]+nums[len(nums)-1-i]
        print(sumLeft)
        print(sumRight)
        for i in range(len(nums)):
            if sumLeft[i]==sumRight[i]:
                return i
        return -1
    
if __name__=="__main__":
    sol=Solution()
    nums = [1,7,3,6,5,6]
    print(sol.pivotIndex(nums))