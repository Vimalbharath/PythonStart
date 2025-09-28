def anagramcount(a,b):
    anagram={}
    count=0
    for i in b:
        if i in anagram:
            anagram[i]+=1
        anagram[i]=1
    count=len(anagram)
    i,j=0,0
    k=len(b)
    ans=0
    while j<len(a):
        if j-i+1<k:
            if a[j] in anagram:
                anagram[a[j]]-=1
                if anagram[a[j]]==0:
                    count=count-1
            j=j+1
        else:
            if count==0:
                ans=ans+1
            if a[i] in anagram:
                anagram[a[i]]+=1
                if not anagram[a[i]]==0:
                    count=count+1
            i=i+1
            j=j+1
    return ans


if __name__=="__main__":
    a="forabrfofjcofr"
    b="for"
    print(anagramcount(a,b))