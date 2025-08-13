ans=0    #way to use global variable
def reverse(n):
    global ans
    helper(n)
    print(ans)
    
def helper(n):
    global ans
    if n==0:
        return
    ans=(ans*10)+n%10
    return helper(n//10)

def main():
    print(reverse(54321))

main()