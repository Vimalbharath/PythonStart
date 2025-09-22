def cansum(arr,target,n):
    if target==0:
        return True
    if n==0 or target<0:
        return False
    if arr[n-1]<=target:
        result=cansum(arr,target-arr[n-1],n) or cansum(arr,target,n-1)
        return result
    else:
        result=cansum(arr,target,n-1)
        return result

if __name__=="__main__":
    arr=[5,4]
    print(cansum(arr,10,len(arr)))