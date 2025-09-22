def bestsum(arr,target,n):
    table=[[None]*(target+1) for i in range (len(arr)+1)]
    for j in range(target+1):
        table[0][j]=None
    for i in range(len(arr)+1):
        table[i][0]=[]
    for i in range(1,len(arr)+1):
        for j in range(1,target+1):
            include_result= table[i][j-arr[i-1]]
            exclude_result=table[i-1][j]
            best_result = None

            if include_result is not None:
                current_result = include_result + [arr[i-1]]
                if best_result is None or len(current_result) < len(best_result):
                    best_result = current_result
                    
            if exclude_result is not None:
                if best_result is None or len(exclude_result) < len(best_result):
                    best_result = exclude_result
            
            table[i][j]= best_result
    print(table)
    
    
if __name__=="__main__":
    arr=[2,6,5]
    print(bestsum(arr,11,len(arr)))