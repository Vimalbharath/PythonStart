def main():
    substring("","abc")

def substring(p,up):
    if len(up)==0:
        print(p)
        return
    ch=up[0]
    ascii=str(ord(up[0]))
    substring(p+ch,up[1:])
    substring(p,up[1:])
    substring(p+ascii,up[1:])


main()