#https://leetcode.com/problems/partition-equal-subset-sum/?envType=problem-list-v2&envId=dynamic-programming

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum=0
        for i in nums:
            sum+=i
        if not sum%2==0: return False
        sum=sum//2
        table=[[None]*(sum+1) for i in range(len(nums)+1)]
        for j in range(sum+1):
            table[0][j]=False
        for i in range(len(nums)+1):
            table[i][0]=True
        for i in range(1,len(nums)+1):
            for j in range(1,sum+1):
                if nums[i-1]<=j:
                    table[i][j]=table[i-1][j-nums[i-1]] or table[i-1][j]
                else:
                    table[i][j]=table[i-1][j]
        return table[len(nums)][sum]       
    
if __name__=="__main__":
    sol=Solution()
    nums = [1,5,11,5]
    print(sol.canPartition(nums))