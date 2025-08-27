#https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution:
    def minInsertions(self, s: str) -> int:
        stack=[]
        insertions=0
        i=0
        while i<len(s):
            if s[i] =='(':
                stack.append(s[i])
            else:
                if i+1 <len(s) and s[i + 1] == ')':
                    if stack:
                        stack.pop()
                    else:
                        insertions+=1
                    i=i+1
                else:
                    insertions+=1
                    if stack:
                        stack.pop()
                    else:
                        insertions+=1
                    i=i+1
            i=i+1
        insertions += len(stack) * 2
        
        return insertions


        


if __name__=="__main__":
    sol=Solution()
    print(sol.minInsertions(")(((())))"))