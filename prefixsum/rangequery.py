#https://leetcode.com/problems/range-sum-query-immutable/description/?envType=problem-list-v2&envId=prefix-sum

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[0 for _ in range(len(nums))]
        self.prefix[0]=nums[0]
        for i in range(1,len(nums)):
            self.prefix[i]=self.prefix[i-1]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        ans=self.prefix[right]
        if not left==0:
            ans=self.prefix[right]-self.prefix[left-1]
        return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
    
if __name__=="__main__":
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    print(numArray.sumRange(0, 2)); # return (-2) + 0 + 3 = 1
    numArray.sumRange(2, 5); # return 3 + (-5) + 2 + (-1) = -1
    numArray.sumRange(0, 5); # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3