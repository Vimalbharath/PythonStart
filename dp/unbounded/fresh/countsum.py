def countsum(arr,target,n):
    if target==0:
        return 1
    if n==0 or target<0:
        return 0
    ans=0
    if arr[n-1]<=target:
        result=countsum(arr,target-arr[n-1],n) + countsum(arr,target,n-1)
        ans=ans+result
    else:
        result=countsum(arr,target,n-1)
        ans=ans+result
    return ans

if __name__=="__main__":
    arr=[2,5,6]
    print(countsum(arr,11,len(arr)))