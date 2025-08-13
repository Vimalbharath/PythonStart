def linear(nums,target): #list inside func
    return helper(nums,target,0)

def helper(nums,target,index):
    ans=[]
    if index==len(nums):
        return []
    if nums[index]==target:
        ans.append(index)
    return ans.append(helper(nums,target,index+1))

def main():
    nums=[1,2,4,90,5,4,7,9]
    target=4
    print(linear(nums,target))

main()