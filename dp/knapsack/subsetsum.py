def subsetsum(arr,sum):
    table=[[None]*(sum+1) for i in range(len(arr)+1)]
    for j in range(sum+1):
        table[0][j]=False
    for i in range(len(arr)+1):
        table[i][0]=True
    for i in range(1,len(arr)+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                table[i][j]=table[i-1][j-1] or table[i-1][j]
            else:
                table[i][j]=table[i-1][j]
    return table

if __name__=="__main__":
    sum=11
    arr=[5,6,11]
    print(subsetsum(arr,sum))