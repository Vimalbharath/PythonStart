def main():
    nums=[9,8,4,5,6,7,3,2,1,0]
    cyclic(nums)
    print(nums)

def cyclic(nums):
    n=len(nums)
    for i in range(n):
        actual=i
        while nums[i]!=actual:
            swap(nums,i,nums[i])

def swap(nums,f,s):
    nums[f],nums[s]=nums[s],nums[f]

if __name__=="__main__":
    main()
