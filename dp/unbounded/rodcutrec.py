def rod(price,n):
    if n==0:
        return True
    if n<0:
        return False
    for i in price:
        newlength=n-i
        if rod(price,newlength)==True:
            return True
    return False

if __name__=="__main__":
    price=[3, 5]
    print(rod(price,9))