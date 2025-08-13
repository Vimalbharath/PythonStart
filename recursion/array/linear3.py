ans=[]
def linear(nums,target): #list as global
    global ans
    return helper(nums,target,0)

def helper(nums,target,index):
    global ans
    if index==len(nums):
        return ans
    if nums[index]==target:
        ans.append(index)
    return helper(nums,target,index+1)

def main():
    nums=[1,2,4,90,5,4,7,9,4]
    target=4
    print(linear(nums,target))

main()