def rbs(nums,target,s,e):
    if s>e:
        return -1
    m=s+(e-s)//2
    if e>m and nums[m]>nums[m+1]:
        return m
    if s<m and nums[m]<nums[m-1]:
        return m
    if nums[s]>nums[m]:
        return rbs(nums,target,s,m-1)
    if nums[s]<nums[m]:
        return rbs(nums,target,m+1,e)
    
def main():
    nums=[6,7,8,9,1,2,4]
    target=6
    print(rbs(nums,target,0,len(nums)-1))

main()