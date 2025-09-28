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

if __name__=="__main__":
    arr=[1,2,3,2,1]
    print(minsubarr(arr,7))