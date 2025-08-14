def pattern(r,c):
    if r==0:
        return 
    
    if c<5:
        print("* ",end="")
        pattern(r,c+1)
    else:
        print()
        pattern(r-1,0)
    

def main():
    pattern(5,0)

main()

# def pattern(r,c):
#     if r==0:
#         return 
    
#     if c>0:
#         print("* ",end="")
#         pattern(r,c-1)
#     else:
#         print()
#         pattern(r-1,5)
    

# def main():
#     pattern(5,5)

# main()