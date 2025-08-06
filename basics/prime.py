num=int(input("Enter a number: "))

def prime1(num):
    temp=0
    for i in range(num):
        if(num %(i+1)==0):
            temp=temp+14
            

    if(temp <=2):
        return True
    else:
        return False
    
def main():
    if(prime1(num)):
        print("Prime Number")
    else:
        print("Not a prime")

main()