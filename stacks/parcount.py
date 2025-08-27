#https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s)==0: return 0
        open,close=0,0
        for char in s:
            if char=='(':
                open=open+1
            elif char==')':
                close=close+1
        return abs(open-close)
