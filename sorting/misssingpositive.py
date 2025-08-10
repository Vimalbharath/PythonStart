from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i,n=0,len(nums)
        while i<n:
            actual=nums[i]-1
            if nums[i]<n and nums[i]>0 and  nums[i]!=nums[actual]:
                self.swap(nums,i,actual)
            else:
                i=i+1
        for i in range(n):
            if i!=nums[i]-1:
                return i
        return n+1

    def swap(self,nums,f,s):
        nums[f],nums[s]=nums[s],nums[f]

def main():
    instance=Solution()
    nums=[1]
    print(instance.firstMissingPositive(nums))
    print(nums)

main()