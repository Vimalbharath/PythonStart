def sorted(nums):
    return helper(nums,0)

def helper(nums,index):
    if index==len(nums)-1:
        return True
    if nums[index]<=nums[index+1]:
        return True and helper(nums,index+1)
    return False

def main():
    nums=[1,2,2,3,4,5,5,6,7,8]
    print(sorted(nums))

main()