def rod(price,n):
    table=[[0]*(n+1) for i in range(n+1)]
    for i in range(n+1):
        table[0][i]=0
    for i in range(n+1):
        table[i][0]=0
    for i in range(1,(n+1)):
        for j in range(1,(n+1)):
            if price[i-1]<=j:
                table[i][j]=max((price[i-1]+table[i][j-price[i-1]]),table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    print(table)

if __name__=="__main__":
    price=[2, 5]
    print(rod(price,len(price)))