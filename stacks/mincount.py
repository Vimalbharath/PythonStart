#https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution:
    def minInsertions(self, s: str) -> int:
        stack=[]
        pair=False
        close=0
        ans=0
        for char in s:
            if char =='(':
                pair=False
                stack.append(char)
            else:
                if not pair:
                    pair=True
                else:
                    if len(stack)>0 and stack[len(stack)-1]=='(':
                        stack.pop()
                    else:
                        ans=ans+1
        return len(stack)*2


        


if __name__=="__main__":
    sol=Solution()
    print(sol.minInsertions(")(((())))"))