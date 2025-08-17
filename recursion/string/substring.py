def main():
    substring("","abc")
    print(substringret("abc"))

def substring(p,up):
    if len(up)==0:
        print(p)
        return
    ch=up[0]
    substring(p+ch,up[1:])
    substring(p,up[1:])

def substringret(up):
    if len(up)==0:
        return []
    ch=up[0]
    left=[ch]
    temp=(substringret(up[1:]))
    left.append(temp)
    right=substringret(up[1:])
    left.extend(right)
    return left

main()