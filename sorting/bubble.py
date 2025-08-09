def main():
    nums=[3,0,9,8,4]
    bubble(nums)
    print(nums)

def bubble(nums):
    l=len(nums)
    for i in range(0,l):
        swapped=False
        for j in range(1,l-i):
            print(j,end=" ")
            if nums[j]<nums[j-1]:
                swapped=True
                swap(nums,j,j-1)
        print()
        if swapped==False:
            break


def swap(nums,f,s):
   nums[f],nums[s]=nums[s],nums[f]

if __name__=="__main__":
    main()