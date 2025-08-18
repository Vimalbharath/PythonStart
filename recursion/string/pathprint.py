def main():
    print(pathprint(3,3,''))

def pathprint(r,c,way):
    if r==1 and c==1:
        print(way)
        return 1
    left,right,side=0,0,0
    if r>1:
        left=pathprint(r-1,c,way+'D')
    if c>1:
        right=pathprint(r,c-1,way+'R')
    if r>1 and c>1:
        side=pathprint(r-1,c-1,way+'S')
    ans=left+right+side
    return ans

main()