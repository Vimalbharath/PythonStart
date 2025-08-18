def main():
    print(path(3,3))

def path(r,c):
    if r==1 or c==1:
        return 1
    left=path(r-1,c)
    right=path(r,c-1)
    ans=left+right
    return ans

main()