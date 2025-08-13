import math

def reverse(n):
    digits=math.log(n)+1
    return helper(n,digits)

def helper(n,digits):
    if n%10==n:
        return n
    return (n%10)* 10**(digits-1) + helper(n//10,digits-1)

def main():
    print(reverse(12345))

main()