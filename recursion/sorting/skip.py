def main():
    skip("","Vimal")
    print(skipret("Vimal"))

def skip(p,up):
    if len(up)==0:
        print(p)
        return
    if up[0]=='a':
        skip(p,up[1:])
    else :
        skip(p+up[0],up[1:])

def skipret(up):
    if len(up)==0:
        return []
    ans=[]
    if up[0]=='a':
       ans.append(skipret(up[1:]))
       return ans
    else:
        ans.append(up[0])
        ans.append(skipret(up[1:]))
        return ans

main()