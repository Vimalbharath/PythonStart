def reverse(n):
    global ans=1
    helper(n)
    print(ans)
    
def helper(n):
    if n==0:
        return
    ans=(ans*10)+n%10
    return helper(n//10)

def main():
    print(reverse(54321))

main()