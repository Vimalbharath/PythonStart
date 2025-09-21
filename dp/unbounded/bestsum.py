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
        result=bestsum(price,newlength,memo)
        if not result==None:
            current_result = result + [i]
            if not bestresult or len(current_result)<=len(bestresult):
                bestresult=current_result
    memo[n]=bestresult
    return bestresult
    

if __name__=="__main__":
    price=[5,4]
    print(bestsum(price,100))