def pattern(r,c):
    if c==0:
        return 
    print("* ",end="")
    pattern(r,c-1)
    if c==0:
        print()
        #pattern(r-1,c)

def main():
    pattern(5,5)

main()