def howsum(arr,target,n):
    table=[[None]*(target+1) for i in range (len(arr)+1)]
    for j in range(target+1):
        table[0][j]=None
    for i in range(len(arr)+1):
        table[i][0]=[]
    for i in range(1,len(arr)+1):
        for j in range(1,target+1):
            # if arr[i-1]<=j:
                if not table[i][j-arr[i-1]] == None:
                    table[i][j]= table[i][j-arr[i-1]]+[arr[i-1]]
            # else:
                if not table[i-1][j]==None:
                    table[i][j]=table[i-1][j]
    print(table)
    
    
if __name__=="__main__":
    arr=[6,5,2]
    print(howsum(arr,11,len(arr)))