def countzeros(n,ans):
    if n==0:
        return ans
    if n%10==0:
        ans=ans+1
    return countzeros(n//10,ans)

def main():
    print(countzeros(10203004000,0))

main()