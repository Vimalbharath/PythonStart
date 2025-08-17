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
    ch=up[0]
    if ch=='a':
       return skipret(up[1:])
    else:
        return ch+skipret(up[1:])

main()