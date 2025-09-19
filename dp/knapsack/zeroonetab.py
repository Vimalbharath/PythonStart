def zeroone(val,w,weight,n):
    table=[[0]*(weight+1) for i in range(n+1)]
    for i in range(1,len(table)):
        for j in range(1,len(table[0])):
            if w[i-1]<=j:
                table[i][j]=max((val[i-1]+table[i-1][j-w[i-1]]),table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    return table
   

if __name__=="__main__":
    weight=1
    val=[100,300,500,250,150]
    w=[5,4,6,2,1]
    print(zeroone(val,w,weight,len(val)))