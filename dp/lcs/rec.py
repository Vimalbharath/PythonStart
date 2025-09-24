def lcs(a,b):
    return lcshelper(a,b,len(a),len(b),memo={})

def lcshelper(a,b,m,n,memo):
    if m==0 or n==0:
        return 0
    if (m,n) in memo:
        return memo[(m,n)]
    if a[m-1]==b[n-1]:
        memo[(m,n)]=1+lcshelper(a,b,m-1,n-1,memo)
        return memo[(m,n)]

    memo[(m,n)]=max(lcshelper(a,b,m,n-1,memo),lcshelper(a,b,m-1,n,memo))
    return memo[(m,n)]

if __name__=="__main__":
    a="abcde"
    b="abrfd"
    print(lcs(a,b))