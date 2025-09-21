def rod(price,n):
    if n==0:
        return []
    if n<0:
        return None
    for i in price:
        newlength=n-i
        result=rod(price,newlength)
        if not result==None:
            result.append(i)
            return result
    return None
    

if __name__=="__main__":
    price=[7,3,5,4]
    print(rod(price,7))