def bestsum(price,n,memo={}):
    if n in memo:
        return memo[n]
    if n==0:
        return []
    if n<0:
        return None
    bestresult=None
    for i in price:
        newlength=n-i
        result=bestsum(price,newlength)
        if not result==None:
            result.append(i)
            if not bestresult or len(result)<=len(bestresult):
                bestresult=result
    memo[n]=bestresult
    return bestresult
    

if __name__=="__main__":
    price=[4,3,5]
    print(bestsum(price,50))