def fibo(n):
    if n<2:
        return n
    return fibo(n-2)+fibo(n-1)

def main():
    print(fibo(6))

main()