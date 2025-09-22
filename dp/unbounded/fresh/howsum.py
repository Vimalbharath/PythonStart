def howsum(arr,target,n):
    if target==0:
        return []
    if n==0 or target<0:
        return None
    include=howsum(arr,target-arr[n-1],n) 
    if not include ==None:
        return include+[arr[n-1]]
    exclude=howsum(arr,target,n-1)
    if not exclude ==None:
        return exclude
    return None

if __name__=="__main__":
    arr=[2,5]
    print(howsum(arr,11,len(arr)))