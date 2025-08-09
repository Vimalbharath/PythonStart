def main():
    nums=[3,0,9,8,4,-1,-2,7,90,80,70,67,100,1]
    insertion(nums)
    print(nums)

def insertion(nums):
    n=len(nums)
    for i in range(1,n):
        j=i
        while j>0:
            if nums[j-1]>nums[j]:
                swap(nums,j,j-1)
            j=j-1

def swap(nums,f,s):
    nums[f],nums[s]=nums[s],nums[f]

if __name__=="__main__":
    main()