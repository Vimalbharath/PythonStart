def zeroone(val,w,weight,n,memo={}):
    if not weight or not n:
        return 0
    if (weight,n) in memo:
        return  memo[(weight,n)]
    if w[n-1]<=weight:
        memo[(weight,n)]=max(val[n-1]+zeroone(val,w,weight-w[n-1],n-1),zeroone(val,w,weight,n-1))
        return memo[(weight,n)]
    else:
        memo[(weight,n)]=zeroone(val,w,weight,n-1)
        return memo[(weight,n)]

if __name__=="__main__":
    weight=14
    val=[100,300,500,250,150]
    w=[5,4,6,2,1]
    print(zeroone(val,w,weight,len(val)))