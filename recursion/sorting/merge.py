def mergesort(nums,s,e):
    if s==e:
        return [nums[s]]
    
    
    m=s+(e-s)//2
    left=mergesort(nums,s,m)
    right=mergesort(nums,m+1,e)
    ans=merge(left,right)
    return ans

def merge(left,right):
    ans=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            ans.append(left[i])
            i=i+1
        else:
            ans.append(right[j])
            j=j+1
    while i<len(left):
        ans.append(left[i])
        i=i+1
    while j<len(right):
        ans.append(right[j])
        j=j+1

    return ans

def main():
    nums=[4,3,2,1,9,5,7,6,0]
    print(mergesort(nums,0,len(nums)-1))

main()
    