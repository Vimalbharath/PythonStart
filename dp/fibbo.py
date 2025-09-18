def fibo(n,table={}):
    if n in table:
        return table[n]
    if n<=2:
        table[n]=1
        return table[n]
    table[n]=fibo(n-1)+fibo(n-2)
    return table[n]

if __name__=="__main__":
    print(fibo(50))
