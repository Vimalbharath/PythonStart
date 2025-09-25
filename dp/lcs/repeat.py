def lcs(a,b):
    m,n=len(a),len(b)
    table=[[-1] * (n+1) for _ in range(m+1)] 
    for j in range(n+1):
        table[0][j]=0
    for i in range(m+1):
        table[i][0]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1] and not i==j:
                table[i][j]=1+table[i-1][j-1]
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])
    print(table)
    return table[m][n]

if __name__=="__main__":
    a="aabcbec"
    b=a
    print(lcs(a,b))

