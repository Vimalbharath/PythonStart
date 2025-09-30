def twosum(arr,target):
    arr.sort()
    print(arr)
    for i in range(len(arr)):
        sum=arr[i]
        for j in range(i+1,len(arr)):
            if sum+arr[j]==target:
                return True
    return False
    
if __name__=="__main__":
    arr = [0, -1, 2, -3, 1]
    target = -5

    # Call the two_sum function and print the result
    if twosum(arr, target):
        print("true")
    else:
        print("false")