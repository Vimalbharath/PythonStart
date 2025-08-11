def sumdigit(n):
    if n==0:
        return 0
    
    return n%10+sumdigit(n//10)

def main():
    print(sumdigit(54321))

main()