def rod(price,n):
    if n==0:
        return []
    if n<0:
        return None
    bestresult=None
    for i in price:
        newlength=n-i
        result=rod(price,newlength)
        if not result==None:
            result.append(i)
            if not bestresult or len(result)<=len(bestresult):
                bestresult=result
    return bestresult
    

if __name__=="__main__":
    price=[4,3,5]
    print(rod(price,7))