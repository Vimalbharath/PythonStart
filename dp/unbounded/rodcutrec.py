def rod(price,n):
    if n==0:
        return []
    if n<0:
        return None
    for i in price:
        newlength=n-i
        result=rod(price,newlength)
        if not result==None:
            return result.append(i)
    return None
    

if __name__=="__main__":
    price=[3,5,4,7]
    print(rod(price,7))