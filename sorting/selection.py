def main():
    nums=[3,0,9,8,4]
    max(nums,0,len(nums))
    print(nums)

def selection(nums):
    n=len(nums)
    # print(n)
    # for i in range(n):
    #     print(i, "->", nums[i])
    for i in range(n):
        pass

def max(nums,s,e):
    for x in range(s,e):
        max=nums[s]
        if nums[x]>max:
            max=nums[x]
            print(max) 
    print(max) 


def swap(nums,f,s):
   nums[f],nums[s]=nums[s],nums[f]

if __name__=="__main__":
    main()