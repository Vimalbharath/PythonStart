def countsum(price,n):

    if n==0:
        return 1
    if n<0:
        return 0
    total=0
    for i in price:
        newlength=n-i
        res=countsum(price,newlength)
        total=total+res
    return total
    

if __name__=="__main__":
    price=[5,1,2]
    print(countsum(price,6))