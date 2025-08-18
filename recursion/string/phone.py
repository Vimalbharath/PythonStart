#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return self.helper('',digits)

    def helper(self,p,digits):
      if len(digits)==0:
        return [p]
      ans=[]
      digit=ord(digits[0])-49
      for i in range((digit-1)*3,digit*3):
          ans.extend(self.helper(p+chr(97+i),digits[1:]))
      return ans

def main():
   sol=Solution()
   print(sol.letterCombinations('23'))

main()