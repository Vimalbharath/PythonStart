def main():
    numbers=[1,2,3,4,5,6,7,8,9]
    target=6
    n=bsearch(numbers,target)
    print(n)

def bsearch(numbers,target):
    s,e=0,len(numbers)
    m=s+(e-s)/2
    while s<e:
        if target>numbers[m]:
            s=m
        elif target<numbers[m]:
            e=m
        else:
            return m
    return -1

main()



main()