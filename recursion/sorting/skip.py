def main():
    skip("","Vimal")
    print(skipret("hgagjigjaaklgalaaaa"))

def skip(p,up):
    if len(up)==0:
        print(p)
        return
    ch=up[0]
    if ch=='a':
        skip(p,up[1:])
    else :
        skip(p+ch,up[1:])

def skipret(up):
    if len(up)==0:
        return ""
    ans=""
    if up[0]=='a':
       ans=ans+(skipret(up[1:]))
       return ans
    else:
        ans=ans+(up[0])
        ans=ans+(skipret(up[1:]))
        return ans

main()