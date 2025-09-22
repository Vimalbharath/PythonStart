def countsum(arr,target,n):
    table=[[0]*(target+1) for i in range (len(arr)+1)]
    for j in range(target+1):
        table[0][j]=0
    for i in range(len(arr)+1):
        table[i][0]=1
    for i in range(1,len(arr)+1):
        for j in range(1,target+1):
            if arr[i-1]<=j:
                table[i][j]=table[i][j-arr[i-1]] + table[i-1][j]
            else:
                table[i][j]=table[i-1][j]
    print(table)
    
    
if __name__=="__main__":
    arr=[5,2,6]
    print(countsum(arr,11,len(arr)))