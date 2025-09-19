def zeroone(val,w,weight,n):
    table=[[0]*(weight+1) for i in range(n+1)]
    for i in range(len(table)):
        for j in range(len(table[0])):
            if weight<=w[n-1] :
                table[i][j]=max((val[i-1]+table[weight-w[i-1]][j-1]),table[i][j-1])
            else:
                table[i][j]=table[i][j-1]
    return table[n][weight]
   

if __name__=="__main__":
    weight=1
    val=[100,300,500,250,150]
    w=[5,4,6,2,1]
    print(zeroone(val,w,weight,len(val)))