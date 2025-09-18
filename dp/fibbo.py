def fibo(n,table=[0]*701):
    if table[n]:
        return table[n]
    if n<=1:
        table[n]=1
        return table[n]
    table[n]=fibo(n-1)+fibo(n-2)
    return table[n]

if __name__=="__main__":
    print(fibo(700))
