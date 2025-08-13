def reverse(n):
    return helper(n,0)

def helper(n,ans):
    if n==0:
        return ans
    ans=(ans*10)+n%10
    return helper(n//10,ans)

def main():
    print(reverse(12345))

main()
    
