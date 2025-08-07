def main():
    nums=[1,2,3,4,5,6,7]
    element=7
    ans=binary(nums,element)
    print(ans)

def binary(nums,element):
    if len(nums)==0: return -1
    s,e=0,len(nums)-1
    while s<=e:
        m=s+(e-s)//2
        if nums[m]>element:
            e=m-1
        elif nums[m]<element:
            s=m+1
        else:
            return m
    return -1


main()