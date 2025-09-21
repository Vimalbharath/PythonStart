def subsetsum(arr,sum):
    table=[[0]*(sum+1) for i in range(len(arr)+1)]
    for j in range(sum+1):
        table[0][j]=0
    for i in range(len(arr)+1):
        table[i][0]=1
    for i in range(1,len(arr)+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                table[i][j]=table[i][j-arr[i-1]] + table[i-1][j]
            else:
                table[i][j]=table[i-1][j]
    return table

if __name__=="__main__":
    sum=11
    arr=[2,5,6]
    print(subsetsum(arr,sum))