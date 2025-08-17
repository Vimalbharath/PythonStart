def main():
    permutation("","Vimal")

def permutation(p,up):
    if len(up)==0:
        print(p)
        return
    for i in range(len(p)):
        ch=up[i]
        permutation(p[:i]+ch+p[i:],up[1:])
        

main()
    