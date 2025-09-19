#https://leetcode.com/problems/target-sum/

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums)<=1 and not abs(target) == abs(nums[0]): return 0
        total=sum(nums)
        diff=target
        s1sum=total+diff
        s1sum=s1sum//2
        return self.subsetsum(nums,s1sum)

    def subsetsum(self,arr,sum):
        table=[[None]*(sum+1) for i in range(len(arr)+1)]
        for j in range(sum+1):
            table[0][j]=0
        for i in range(len(arr)+1):
            table[i][0]=1
        for i in range(1,len(arr)+1):
            for j in range(1,sum+1):
                if arr[i-1]<=j:
                    table[i][j]=table[i-1][j-arr[i-1]] + table[i-1][j]
                else:
                    table[i][j]=table[i-1][j]
        return table[len(arr)][sum]
    