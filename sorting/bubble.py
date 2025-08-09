def main():
    nums=[3,0,9,8,4,-1,-2,7,90,80,70,67,100,1]
    bubble(nums)
    print(nums)

def bubble(nums):
    l=len(nums)
    for i in range(0,l):
        swapped=False
        for j in range(1,l-i):
            if nums[j]<nums[j-1]:
                swapped=True
                swap(nums,j,j-1)
        if swapped==False:
            break


def swap(nums,f,s):
   nums[f],nums[s]=nums[s],nums[f]

if __name__=="__main__":
    main()