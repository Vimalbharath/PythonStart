def main():
    skip("","Vimalapplevimalapple")

def skip(p,up):
    if len(up)==0:
        print(p)
        return
    ch=up[0]
    if up.startswith('apple'):
        skip(p,up[5:])
    else :
        skip(p+ch,up[1:])

main()