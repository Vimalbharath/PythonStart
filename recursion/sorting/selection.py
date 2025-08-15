def selection(nums,r,c,max):
    if r==0:
        return
    if c<r:
        if nums[max]<=nums[c]:
            selection(nums,r,c+1,c)
        else:
            selection(nums,r,c+1,max)
    else:
        swap(nums,max,c)
        selection(nums,r-1,0,0)


def swap(nums,f,s):
    nums[f],nums[s]=nums[s],nums[f]

def main():
    nums=[4,3,2,1]
    selection(nums,len(nums)-1,0,0)
    print(nums)

main()