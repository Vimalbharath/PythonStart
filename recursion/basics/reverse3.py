import math

def reverse(n):
    digits=int(math.log10(n))+1
    return helper(n,digits)

def helper(n,digits):
    if n%10==n:
        return n
    return (n%10)* 10**(digits-1) + helper(n//10,digits-1)

def main():
    n=123454321
    rev=reverse(n)
    print(rev)
    print(True if n==rev else  False)
main()