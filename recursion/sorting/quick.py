def quick(nums,low,high):
    if high<=low:
        return
    s,e=low,high
    m=s+(e-s)//2
    pivot=nums[m]
    while s<=e:
        while nums[s]<pivot:
            s=s+1
        while nums[e]>pivot:
            e=e-1
        if s<=e:
            nums[s],nums[e]=nums[e],nums[s]
            s=s+1
            e=e-1
    quick(nums,low,e)
    quick(nums,s,high)

def main():
    nums=[4,3,2,1,9,5,7,6,0]
    quick(nums,0,len(nums)-1)
    print(nums)

main()