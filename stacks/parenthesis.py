#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char=='[' or char =='{' or char =='(':
                stack.append(char)
            else:
                if char==']':
                    if len(stack)==0 or not stack.pop()=='[':
                        return False
                elif char=='}':
                    if len(stack)==0 or not stack.pop()=='{':
                        return False
                elif char==')':
                    if len(stack)==0 or not stack.pop()=='(':
                        return False
        return len(stack)==0

