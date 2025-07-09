def main():
    numbers=[1,2,3,4,5,6,7,8,9]
    target=8
    n=bsearch(numbers,target)
    print(n)

def bsearch(numbers,target):
    s,e=int(0),len(numbers)
   
    while s<e:
        m=int(s+(e-s)/2)
        if target>numbers[m]:
            s=m
        elif target<numbers[m]:
            e=m
        else:
            return m
    return -1

main()
