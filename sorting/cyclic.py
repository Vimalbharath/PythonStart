def main():
    nums=[9,8,4,5,6,7,3,2,1,0]
    cyclic(nums)
    print(nums)

def cyclic(nums):
    i,n=0,len(nums)
    while i<n:
        actual=i
        if nums[i]!=actual:
            swap(nums,i,nums[i])
        else:
            i=i+1

def swap(nums,f,s):
    nums[f],nums[s]=nums[s],nums[f]

if __name__=="__main__":
    main()
