def main():
    pattern8(5)
    #pattern5(5)
    
def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("* ",end="")
        print()

def pattern2(n):
    for i in range(n+1):
        for j in range(i):
            print("* ",end="")
        print()

def pattern3(n):
    for i in range(n):
        for j in range(n-i):
            print("* ",end="")
        print()

def pattern4(n):
    for i in range(n):
        #print(i) range(0,0) is empty
        for j in range(i+1):
            print(j,end=" ")
        print()

def pattern5(n):
    for i in range(n):
        #print(n-i)
        for j in range(n-i):
            print(j,end=" ")
        print()

def pattern6(n):
    for i in range(2*n):
        col=2*n-i if i>n else i
        for j in range(col):
            print(j+1,end=" ")
        print()

def pattern7(n):
    for i in range(2*n):
        col=i if i<=n else 2*n-i
        spaces=n-col
        for k in range(spaces):
            print(end=" ")
        for j in range(col):
            print(j+1,end=" ")
        print()

def pattern8(n):
    for i in range(n):
        for k in range(n-i+1):
            print(end=" ")
        for m in range(i):
            print("*",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()

if __name__=="__main__":
    main()