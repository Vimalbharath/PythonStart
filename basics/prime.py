# num=int(input("Enter a number: "))

def prime1(num):
    temp=0
    for i in range(num):
        if(num %(i+1)==0):
            temp=temp+1
            

    if(temp <=2):
        return True
    else:
        return False

def prime2(num):
    c=2
    while(c*c<=num):
        if(num%c==0):
            return False
        c=c+1
    return True
    
def main():
    for num in range(1,100):
        if(prime1(num)):print(num)
        if(prime2(num)):print(num)

main()