def lcsubstring(a,b):
    m,n=len(a),len(b)
    table=[[-1] * (n+1) for _ in range(m+1)] 
    for j in range(n+1):
        table[0][j]=0
    for i in range(m+1):
        table[i][0]=0
    ans=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                table[i][j]=1+table[i-1][j-1]
                ans=max(ans,table[i][j])
            else:
                table[i][j]=0
    print(table)
    return ans

if __name__=="__main__":
    a="abcdef"
    b="abrfd"
    print(lcsubstring(a,b))

