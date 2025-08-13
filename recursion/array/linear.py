def linear(nums,target):
    return helper(nums,target,0)

def helper(nums,target,index):
    if index==len(nums)-1:
        return -1
    if nums[index]==target:
        return index
    return helper(nums,target,index+1)

def main():
    nums=[1,2,4,90,5,7,9]
    target=90
    print(linear(nums,target))

main()