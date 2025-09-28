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

def min_subarray_len_greater_than_or_equal_k(arr, target_sum):
    """
    Finds the minimum length of a contiguous subarray whose sum is >= target_sum.
    Time Complexity: O(N)
    """
    min_len = math.inf
    i = 0      # Start pointer
    wsum = 0   # Current window sum

    # j drives the expansion of the window
    for j in range(len(arr)):
        wsum += arr[j]  # 1. EXPANSION: Add the new element

        # 2. CONTRACTION & EVALUATION: Contract as long as the condition is met (wsum >= target_sum)
        while wsum >= target_sum:
            # A. EVALUATION: This is the time to record the length.
            current_len = j - i + 1
            min_len = min(min_len, current_len)

            # B. CONTRACTION: Remove the element at the start and slide 'i'
            wsum -= arr[i]
            i += 1
            
    # Return 0 if no subarray was found, otherwise return the minimum length.
    return min_len if min_len != math.inf else 0
if __name__=="__main__":
    arr = [1, 5, 2,  1,1,1,1]
    target = 3
    print(minsubarr(arr,target))
    print(min_subarray_len_greater_than_or_equal_k(arr,target))