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
    i,j=0,0
    temp=0
    ans=0
    while(j<len(arr)):
        window=j-i+1
        temp=temp+arr[j]
        if window<k:
            j=j+1
        elif window==k:
            ans=max(temp,ans)
            j=j+1
            temp=temp-arr[i]
            i=i+1   
    return ans



if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9]
    print(maxsum(arr,2))
    print(maxsumslide(arr,2))