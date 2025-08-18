#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return self.helper('',digits)

    def helper(self,p,digits):
      if len(digits)==0:
        return chr(p)
      ans=[]
      ch=ord(digits[0])+47
      for i in range(3):
          ans.append(self.helper(ch+i,digits[1:]))
      return ans

def main():
   sol=Solution()
   print(sol.letterCombinations('2'))

main()