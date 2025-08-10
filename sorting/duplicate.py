#https://leetcode.com/problems/find-the-duplicate-number/

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i,n=0,len(nums)
        while i<n:
            actual=nums[i]-1
            if  nums[i]!=nums[actual]:
                self.swap(nums,i,actual)
            else:
                i=i+1
        missingnumbers=[]
        for i in range(n):
            if i!=nums[i]-1:
                missingnumbers.append(i+1)
        print("Missing",missingnumbers)

        duplicatenumbers=[]
        for i in range(n):
            if i!=nums[i]-1:
                duplicatenumbers.append(nums[i])
        print("Duplicate",duplicatenumbers)
        

    
    def swap(self,nums,f,s):
        nums[f],nums[s]=nums[s],nums[f]
            
def main():
    instance=Solution()
    nums=[4,3,2,7,8,2,3,1]
    print(instance.findDuplicate(nums))
    print(nums)

main()