def howsum(arr, target, index, memo={}):
    # Use a tuple as the key for memoization
    if (target, index) in memo:
        return memo[(target, index)]
    
    # Base cases for recursion
    if target == 0:
        return []
    if target < 0 or index == 0:
        return None
    
    # Option 1: Try to include the current number (arr[index - 1])
    # The current number is arr[index - 1] because we start from len(arr)
    current_num = arr[index - 1]
    
    result = howsum(arr, target - current_num, index, memo)
    
    if result is not None:
        memo[(target, index)] = result + [current_num]
        return memo[(target, index)]
    
    # Option 2: Exclude the current number and move to the previous one
    result = howsum(arr, target, index - 1, memo)
    
    if result is not None:
        memo[(target, index)] = result
        return memo[(target, index)]
    
    # If neither option works, memoize and return None
    memo[(target, index)] = None
    return None

if __name__ == "__main__":
    arr = [2, 5, 6]
    print(howsum(arr, 11, len(arr)))