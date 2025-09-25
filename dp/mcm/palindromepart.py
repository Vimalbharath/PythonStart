import math

def partpalin(s):
    return partpalinh(s,0,len(s)-1)

def partpalinh(s,i,j):
    if i>=j:
        return 0
    if palindrome(s,i,j):
        return 0
    ans=math.inf
    for k in range(i,j+1):
        temp=1+partpalinh(s,i,k)+partpalinh(s,k+1,j)
        ans=min(temp,ans)
    return ans

def palindrome(s,i,j):
    if i==j:
        return True
    while i<=j:
        if not s[i]==s[j]:
            return False
        i=i+1
        j=j-1
    return True

if __name__=="__main__":
    s="malayalamh"
    print(partpalin(s))