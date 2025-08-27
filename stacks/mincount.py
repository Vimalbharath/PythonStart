#https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution:
    def minInsertions(self, s: str) -> int:
        stack=[]
        close=0
        open=0
        for char in s:
            if char =='(':
                stack.append(char)
            else:
                if char == ')':
                    if close==0:
                        close=close+1
                    elif close==1:
                        close=close-1
                        if len(stack)>0 :
                            stack.pop()
                        else:
                            open=open+1

        return len(stack)*2+open

if __name__=="__main__":
    sol=Solution()
    print(sol.minInsertions(")(((())))"))