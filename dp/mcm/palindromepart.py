import math

def partpalin(s):
    return partpalinh(s,0,len(s)-1,memo={})

def partpalinh(s,i,j,memo):
    if i>=j:
        return 0
    if (i,j) in memo:
        return memo[(i,j)]
    if palindrome(s,i,j):
        return 0
    ans=math.inf
    for k in range(i,j):
        # if (i,k) in memo:
        #     left=memo[(i,k)]
        # else:
        #     memo[(i,k)]=partpalinh(s,i,k,memo)
        #     left=memo[(i,k)]
        # if (k+1,j) in memo:
        #     right=memo[(k+1,j)]
        # else:
        #     memo[(k+1,j)]=partpalinh(s,k+1,j,memo)
        #     right=memo[(k+1,j)]
        # temp=1+left+right
        temp=1+partpalinh(s,i,k,memo)+partpalinh(s,k+1,j,memo)
        ans=min(temp,ans)
    memo[(i,j)]=ans
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
    s="malayalamhu"
    print(partpalin(s))