def cansum(arr,target,n):
    table=[[False]*(target+1) for i in range (len(arr)+1)]
    for j in range(target+1):
        table[0][j]=False
    for i in range(len(arr)+1):
        table[i][0]=True
    for i in range(1,len(arr)+1):
        for j in range(1,target+1):
            if arr[i-1]<=j:
                table[i][j]=table[i][j-arr[i-1]] or table[i-1][j]
            else:
                table[i][j]=table[i-1][j]
    print(table)
    
    
if __name__=="__main__":
    arr=[5,4,1]
    print(cansum(arr,10,len(arr)))