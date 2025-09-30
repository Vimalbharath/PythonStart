def remove(arr,ele):
    i=0
    j=len(arr)-1
    while i<=j:
        if arr[i]==ele:
            arr[i],arr[j]=arr[j],arr[i]
            j=j-1
        i=i+1
    return arr


if __name__=="__main__":
    arr = [0, 1, 3, 0, 2, 2, 4, 2]
    ele = 2
    print(remove(arr, ele))