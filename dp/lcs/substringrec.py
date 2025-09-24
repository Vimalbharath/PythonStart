def lcsubstring(a,b):
    return lcsubstringhelper(a,b,len(a),len(b),0,memo={})
    
#failing
def lcsubstringhelper(a,b,m,n,ans,memo):
    
    if (m,n) in memo:
        return memo[(m,n)]
    if m==0 or n==0:
        return 0
    if a[m-1]==b[n-1]:
        memo[(m,n)]=1+lcsubstringhelper(a,b,m-1,n-1,ans,memo)
        ans=max(ans,memo[(m,n)])
        return memo[(m,n)]
    lcsubstringhelper(a,b,m,n-1,ans,memo)
    lcsubstringhelper(a,b,m-1,n,ans,memo)
    memo[(m,n)]=0
    return memo[(m,n)]

if __name__=="__main__":
    a="abcde"
    b="abrfd"
    print(lcsubstring(a,b))