#https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s)==0: return 0
        stack=[]
        for char in s:
            if char=='(':
                stack.append(char)
            elif char==')':
                if len(stack)>0 and stack[len(stack)-1]=='(':
                    stack.pop()
                else: 
                    stack.append(char)
        return len(stack)
