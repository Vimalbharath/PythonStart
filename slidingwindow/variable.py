import math

def minsubarr(arr,sum):  
    ans=math.inf
    for i in range(len(arr)):
        wsum=0
        for j in range(i,len(arr)):
            wsum+=arr[j]
            if wsum==sum:
                ans=min(ans,j-i+1)
    return ans

def minsubarrslide(arr,sum):
    ans=math.inf
    i,j=0,0
    wsum=0
    while j<len(arr) :
        wsum+=arr[j]
        if wsum<sum:
            j=j+1
        if wsum==sum:
            ans=min(ans,j-i+1)
        if wsum>sum:
            if i<len(arr):
                wsum-=arr[i]
                i=i+1
                j=j+1
    return ans

if __name__=="__main__":
    arr=[1,2,3,2,1]
    print(minsubarr(arr,7))
    print(minsubarrslide(arr,7))