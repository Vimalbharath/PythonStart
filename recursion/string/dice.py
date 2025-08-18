def main():
    print(dice(4,""))

def dice(target,ans):
    if target==0:
        return [ans]
    res=[]
    for i in range(1,6):
        if i <= target:
            
            res.extend(dice(target-i,ans+str(i)))
    return res

main()
        