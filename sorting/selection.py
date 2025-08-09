def main():
    nums=[3,0,9,8,4,-1,-2,7,90,80,70,67,100,1]
    selection(nums)
    print(nums)

def selection(nums):
    n=len(nums)
    # print(n)
    # for i in range(n):
    #     print(i, "->", nums[i])
    for i in range(n):
        l=n-i-1
        maxpos=max(nums,0,l+1)#since using range in max, making code similar to java
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