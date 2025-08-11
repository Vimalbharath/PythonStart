def binary(nums,target,s,e):
    if s>e:
        return -1
    m=s+(e-s)//2
    if nums[m]==target:
        return m
    if nums[m]>target:
        return binary(nums,target,s,m-1)
    return binary(nums,target,m+1,e)

def main():
    nums=[1,4,8,23,45,67,80,89]
    target=89
    ans=binary(nums,target,0,len(nums))
    print(ans)

main()
