#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return self.helper('',digits)

    def helper(self,p,digits):
      if len(digits)==0:
        return [p]
      ans=[]
      ch=97+(ord(digits[0])-50)
      for i in range(3):
          ans.extend(self.helper(chr(ch+i)+p,digits[1:]))
      return ans

def main():
   sol=Solution()
   print(sol.letterCombinations('23'))

main()