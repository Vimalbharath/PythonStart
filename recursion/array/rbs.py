def rbs(nums,target,s,e):
    if s>e:
        return -1
    m=s+(e-s)//2
    if nums[m]==target:
        return m
    if nums[s]<=nums[m]:
        if nums[s]<=target<nums[m]:
            return rbs(nums,target,s,m-1)
        else:
            return rbs(nums,target,m+1,e)
    else:
        if nums[m]<target<=nums[e]:
            return rbs(nums,target,m+1,e)
        else:
            return rbs(nums,target,s,m-1)
    
def main():
    nums=[6,7,8,9,1,2,4]
    target=6
    print(rbs(nums,target,0,len(nums)-1))

main()