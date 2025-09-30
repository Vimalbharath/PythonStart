def twosum(arr,target):
    #arr.sort()
    print(arr)
    for i in range(len(arr)):
        sum=arr[i]
        for j in range(i+1,len(arr)):
            if sum+arr[j]==target:
                return True
    return False

def twosum2(arr,target):
    arr.sort()
    i=0
    j=len(arr)-1
    sum=0
    while i<j:
        sum=arr[i]+arr[j]
        if sum==target:
            return True
        if sum>target:
            j=j-1
        else:
            i=i+1
    
if __name__=="__main__":
    arr = [0, -1, 2, -3, 1]
    target = 4

    # Call the two_sum function and print the result
    if twosum(arr, target):
        print("true")
    else:
        print("false")

    if twosum2(arr, target):
        print("true")
    else:
        print("false")