def rodcut(price,w,length,n):
    table=[[0]*(length+1) for i in range(n+1)]
    for i in range(1,len(table)):
        for j in range(1,len(table[0])):
            if w[i-1]<=j:
                table[i][j]=max((price[i-1]+table[i][j-w[i-1]]),table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    return table
   

if __name__=="__main__":
    length=8
    price=[1, 5, 8, 9, 10, 17, 17, 20]
    w=[1,2,3,4,5,6,7,8]
    print(rodcut(price,w,length,len(price)))