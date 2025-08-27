#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char=='[' or char =='{' or char =='(':
                stack.append(char)
            else:
                if char==']':
                    if len(stack)==0 or not stack.remove(stack[len(stack)-1])=='[':
                        return False
                if char=='}':
                    if len(stack)==0 or not stack.remove(stack[len(stack)-1])=='{':
                        return False
                if char==')':
                    if len(stack)==0 or not stack.remove(stack[len(stack)-1])=='(':
                        return False
        return len(stack)==0
