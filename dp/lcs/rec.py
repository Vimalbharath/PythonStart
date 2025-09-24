def lcs(a,b):
    return lcshelper(a,b,len(a),len(b))

def lcshelper(a,b,m,n):
    if m==0 or n==0:
        return 0
    if a[m-1]==b[n-1]:
        return 1+lcshelper(a,b,m-1,n-1)
    return max(lcshelper(a,b,m,n-1),lcshelper(a,b,m-1,n))

if __name__=="__main__":
    a="abcde"
    b="abrfd"
    print(lcs(a,b))