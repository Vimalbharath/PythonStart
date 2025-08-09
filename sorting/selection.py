def main():
    nums=[3,0,9,8,4]
    selection(nums)
    print(nums)

def selection(nums):
    n=len(nums)
    # print(n)
    # for i in range(n):
    #     print(i, "->", nums[i])
    for i in range(n):
        l=n-i
        maxpos=max(nums,0,l)
        swap(nums,l,maxpos)

def max(nums,s,e):
    max=s
    for x in range(s,e):
        if nums[x]>nums[max]:
            max=x
    #print(max) 
    return max


def swap(nums,f,s):
   nums[f],nums[s]=nums[s],nums[f]

if __name__=="__main__":
    main()