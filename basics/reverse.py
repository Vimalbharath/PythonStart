num=int(input("Enter a number: "))

ans=0

while num>0:
    temp=num%10
    num=int(num/10)
    ans=(ans*10)+temp
    print(temp,end='')
print()
print(ans)