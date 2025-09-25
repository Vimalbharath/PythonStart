import math

def mcm(arr):
    return mcmhelp(arr,1,len(arr)-1,memo={})

def mcmhelp(arr,i,j,memo):
    if i>=j:
        return 0
    if (i,j) in memo:
        return memo[(i,j)]
    ans=math.inf
    for k in range(i,j):
        temp=mcmhelp(arr,i,k,memo)+mcmhelp(arr,k+1,j,memo)+(arr[i-1]*arr[k]*arr[j])
        ans=min(temp,ans)
    memo[(i,j)] =ans
    return ans

if __name__=="__main__":
    arr=[2,1,3,4]
    print(mcm(arr))