# https://leetcode.com/problems/find-the-highest-altitude/?envType=problem-list-v2&envId=prefix-sum


from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix=[0 for _ in range(len(gain)+1)]
        prefix[0]=0
        for i in range(1,len(gain)+1):
            prefix[i]=prefix[i-1]+gain[i-1]
        print(prefix)
        return max(prefix)
    
if __name__=="__main__":
    sol=Solution()
    gain = [-5,1,5,0,-7]
    sol.largestAltitude(gain)