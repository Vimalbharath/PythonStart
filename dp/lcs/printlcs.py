def lcs(a,b):
    m,n=len(a),len(b)
    table=[[-1] * (n+1) for _ in range(m+1)] 
    for j in range(n+1):
        table[0][j]=0
    for i in range(m+1):
        table[i][0]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                table[i][j]=1+table[i-1][j-1]
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])
    print(table)
    ans=''
    m,n=i,j
    while i>0 and j>0:
        if a[i-1]==b[j-1]:
            ans=ans+a[i-1]
            i=i-1
            j=j-1
        else:
            if table[i-1][j]>table[i][j-1]:
                i=i-1
            else:
                j=j-1
    return ans[::-1]

if __name__=="__main__":
    a="abcdef"
    b="abrfd"
    print(lcs(a,b))

