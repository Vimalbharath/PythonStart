#https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max=0
        for x in accounts:
            sum=0
            for y in x:
                sum=sum+y
            if sum>max:
                max=sum
        return max