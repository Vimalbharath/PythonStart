def main():
    print(permutation("","abc"))
    for i in range(1):
        print(i)

def permutation(p,up):
    if len(up)==0:
        print(p)
        return 1
    ch=up[0]
    count=0
    for i in range(0,len(p)+1):
        count= count+permutation(p[:i]+ch+p[i:],up[1:])

    return count
        

main()
    