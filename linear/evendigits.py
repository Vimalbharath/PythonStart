#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n=0
        for x in nums:
            if evendigit(x):
                n=n+1
        return n

    def evendigit(x):
        n=0
        while x>0:
            x=x/10
            n=n+1
        return n%2==0