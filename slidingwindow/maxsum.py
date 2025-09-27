def maxsum(arr,k):
    ans=0
    for i in range(len(arr)):
        temp=0
        for j in range(i,i+k):
            if j<len(arr):
                temp=temp+arr[j]
                ans=max(temp,ans)
    return ans

def maxsumslide(arr,k):
    i,j=0,len(arr)-1
    while(not i==j):
        window=0
        temp=0
        ans=0
        if not window==k:
            i=i+1
            temp=temp+arr[i]
            window=window+1
        else:
            ans=max(temp,ans)
            temp=temp-



if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9]
    print(maxsum(arr,3))
    print(maxsumslide(arr,3))