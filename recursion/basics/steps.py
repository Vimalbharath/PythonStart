#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        return self.helper(num,0)
    
    def helper(self,num,ans):
        if num==0:
            return ans

        if num%2==0:
            return self.helper(num//2,ans+1)
        return self.helper(num-1,ans+1)