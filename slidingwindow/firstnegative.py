from collections import deque

def firstneg(arr,k):
    ans=[]
    for i in range(len(arr)):
        if i+k<=len(arr):
            for j in range(i,i+k):
                    if arr[j]<0:
                        ans.append(arr[j])
                        break
            else:
                ans.append(0)
    return ans

def firstnegslide(arr,k):
    i,j=0,0
    queue=deque()
    ans=[]
    while(j<len(arr)):
        window=j-i+1
        if arr[j]<0:
            queue.append(arr[j])
        if window<k:
            j=j+1
        elif window==k:
            if queue:
                ans.append(queue[0])
            else:
                ans.append(0)
            j=j+1
            if queue and queue[0]==arr[i]:
                queue.popleft()    
            i=i+1   
    return ans



if __name__=="__main__":
    arr=[1,2,3,4,-5,6,-7,8,9]
    print(firstneg(arr,2))
    print(firstnegslide(arr,2))