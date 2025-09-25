import math

def mcm(arr):
    return mcmhelp(arr,1,len(arr)-1)

def mcmhelp(arr,i,j):
    if i>=j:
        return 0
    ans=math.inf
    for k in range(i,j):
        temp=mcmhelp(arr,i,k)+mcmhelp(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        ans=min(temp,ans)
    return ans

if __name__=="__main__":
    arr=[2,1,3,4]
    print(mcm(arr))