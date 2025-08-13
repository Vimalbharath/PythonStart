def linear(nums,target): #list inside func,return and combine
    return helper(nums,target,0)

def helper(nums,target,index):
    ans=[]
    if index==len(nums):
        return []
    if nums[index]==target:
        ans.append(index)
    prev=helper(nums,target,index+1)
    ans.extend(prev)
    return ans

def main():
    nums=[1,2,4,90,5,4,7,9]
    target=4
    print(linear(nums,target))

main()