def main():
    print("Even" if parity()==True else "Odd")

def parity():
    n=int(input("Enter a number:"))
    return n%2==0

main()