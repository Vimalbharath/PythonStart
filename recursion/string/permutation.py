def main():
    permutation("","abc")
    for i in range(1):
        print(i)

def permutation(p,up):
    if len(up)==0:
        print(p)
        return
    ch=up[0]
    for i in range(0,len(p)+1):
        permutation(p[:i]+ch+p[i:],up[1:])
        

main()
    