def howsum(arr,target,n):
    if target==0:
        return []
    if n==0 or target<0:
        return None
    ans=None
    if arr[n-1]<=target:
        include=howsum(arr,target-arr[n-1],n) 
        exclude=howsum(arr,target,n-1)
        if not include==None:
            include=include+[arr[n-1]]
        else:
            include=[arr[n-1]]
        if exclude:
            ans=include+exclude
        else:
            ans=include
    else:
        result=howsum(arr,target,n-1)
        if not result==None:
            ans=result
    return ans

if __name__=="__main__":
    arr=[2,5,6]
    print(howsum(arr,11,len(arr)))