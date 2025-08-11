def product(n):
    if n==0:
        return 1
    
    return n*product(n-1)

def main():
    print(product(5))

main()