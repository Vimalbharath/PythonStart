def main():
    nums=[3,9,8,4,7]
    bubble(nums)
    print(nums)

def bubble(nums):
    l=len(nums)-1
    for i in range(0,l):
        swapped=False
        for j in range(1,l-i):
            if nums[j]<nums[j-1]:
                swapped=True
                swap(nums,j,j-1)
        if swapped==False:
            break


def swap(nums,f,s):
    temp=nums[f]
    nums[f]=nums[s]
    nums[s]=temp

if __name__=="__main__":
    main()