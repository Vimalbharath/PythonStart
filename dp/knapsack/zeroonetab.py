def zeroone(val,w,weight,n):
    table=[[0]*(weight+1) for i in range(n+1)]
    for i in range(len(table)):
        for j in range(len(table[0])):
            if weight<=w[n-1] :
                table[weight][n]=max((val[n-1]+table[weight-w[n-1]][n-1]),table[weight][n-1])
            else:
                table[weight][n]=table[weight][n-1]
    return table
   

if __name__=="__main__":
    weight=1
    val=[100,300,500,250,150]
    w=[5,4,6,2,1]
    print(zeroone(val,w,weight,len(val)))