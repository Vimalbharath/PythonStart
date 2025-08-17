def main():
    skip("","Vimalapplevimalapple")
    print(skipret("Vimalappvimalapple"))

def skip(p,up):
    if len(up)==0:
        print(p)
        return
    ch=up[0]
    if up.startswith('apple'):
        skip(p,up[5:])
    else :
        skip(p+ch,up[1:])

def skipret(up):
    if len(up)==0:
        #print(p)
        return ''
    ch=up[0]
    if up.startswith('app') and not up.startswith('apple'):
        return skipret(up[3:])
    else :
        return ch+skipret(up[1:])
    
main()