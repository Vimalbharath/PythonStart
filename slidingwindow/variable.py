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
    ans=0
    i,j=0,0
    wsum=0
    while j<len(arr) :  
        wsum+=arr[j]      
        while wsum>sum:
            wsum-=arr[i]
            i=i+1
        ans=max(ans,j-i+1)
        j=j+1      
    return ans

def longest_subarray_lessthan_k(arr, target_sum):
    n = len(arr)
    max_len = 0
    i = 0      # Start pointer
    wsum = 0   # Current window sum

    # j drives the expansion of the window
    for j in range(n):
        wsum += arr[j]  # 1. EXPANSION: Always add the new element

        # 2. CONTRACTION: Contract only when the condition is violated
        while wsum > target_sum:
            wsum -= arr[i]
            i += 1
        
        # 3. EVALUATION: The window is guaranteed to be valid (wsum <= target_sum)
        # Update max_len with the current valid length
        max_len = max(max_len, j - i + 1)
            
    return max_len

if __name__=="__main__":
    #arr=[1,2,3,1,1,1]
    arr = [1, 5, 2, 3, 1]
    target = 3
    #print(minsubarr(arr,5))
    print(minsubarrslide(arr,target))
    print(f"Longest Subarray (sum <= 7): {longest_subarray_lessthan_k(arr, target)}")