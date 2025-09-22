def bestsum(arr, target, n):
    if target == 0:
        return []
    if n == 0 or target < 0:
        return None

    # Option 1: Try including the last number (arr[n-1])
    include_result = bestsum(arr, target - arr[n-1], n)
    
    # Option 2: Try excluding the last number
    exclude_result = bestsum(arr, target, n - 1)
    
    best_result = None

    if include_result is not None:
        current_result = include_result + [arr[n-1]]
        if best_result is None or len(current_result) < len(best_result):
            best_result = current_result
            
    if exclude_result is not None:
        if best_result is None or len(exclude_result) < len(best_result):
            best_result = exclude_result
            
    return best_result

if __name__ == "__main__":
    arr = [2,11,6, 5]
    print(bestsum(arr, 11, len(arr)))