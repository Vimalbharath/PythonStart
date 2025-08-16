def quick(nums,low,high):
    if high<=low:
        return
    s,e=low,high
    m=s+(e-s)//2
    pivot=nums[m]
    while s<=e:
        if nums[low]<pivot:
            s=s+1
        if nums[high]>pivot:
            e=e-1
        if s<=e:
            nums[s],nums[e]=nums[e],nums[s]
            s=s+1
            e=e-1
    quick(nums,low,e)
    quick(nums,s,high)

def main():
    nums=[5,4,3,2,1]
    quick(nums,0,len(nums)-1)
    print(nums)

main()