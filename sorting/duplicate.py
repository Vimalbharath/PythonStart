#https://leetcode.com/problems/find-the-duplicate-number/

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i,n=0,len(nums)
        while i<n:
            if nums[i]!=i+1:
                actual=nums[i]-1
                if nums[i]!=nums[actual]:
                    self.swap(nums,i,actual)
                else:
                    return nums[i]
            else:
                i=i+1
        return -1
    
    def swap(self,nums,f,s):
        nums[f],nums[s]=nums[s],nums[f]
            
def main():
    instance=Solution()
    nums=[1,7,8,6,6,4,3,2,0,5,9,7]
    print(instance.findDuplicate(nums))
    print(nums)

main()