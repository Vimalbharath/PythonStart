def bubble(nums,r,c):
    if r<0:
        return
    if nums[c]<nums[c-1]:
        swap(nums,c,c-1)
    if(c<r):
        bubble(nums,r,c+1)
    else:
        bubble(nums,r-1,1)

def swap(nums,a,b):
    nums[a],nums[b]=nums[b],nums[a]

def main():
    nums=[4,3,2,1,9,8]
    bubble(nums,len(nums)-1,1)
    print(nums)

main()