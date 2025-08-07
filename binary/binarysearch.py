def main():
    nums=[1,2,3,4,5,6,7]
    element=9
    ans=binary(nums,element)
    print(ans)

def binary(nums,element):
    if len(nums)==0: return -1
    s,e=0,len(nums)
    while e>s:
        m=s+(e-s)//2
        if nums[m]>element:
            e=m
        elif nums[m]<element:
            s=m
        else:
            return m
    return -1


main()