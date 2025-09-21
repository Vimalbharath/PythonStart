def howsum(price,n,memo={}):
    if n in memo:
        return memo[n]
    if n==0:
        return []
    if n<0:
        return None
    for i in price:
        newlength=n-i
        result=howsum(price,newlength,memo)
        if not result==None:
            result.append(i)
            memo[n]=result
            return result
    memo[n]=None
    return memo[n]
    

if __name__=="__main__":
    price=[7,14]
    print(howsum(price,300))