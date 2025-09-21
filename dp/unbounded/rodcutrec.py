def rod(price,n,ans):
    if n==0:
        return ans
    if n<0:
        return -1
    for i in price:
        newlength=n-i
        if newlength<=n:
            ans.append(i)
            if not rod(price,newlength,ans)==-1:
                return ans
    return -1

if __name__=="__main__":
    price=[3, 5]
    print(rod(price,9,[]))