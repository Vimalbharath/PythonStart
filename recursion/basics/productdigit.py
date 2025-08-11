def productdigit(n):
    if n==0:
        return 1
    
    return n%10*productdigit(n//10)

def main():
    print(productdigit(54321))

main()