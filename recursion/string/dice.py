def main():
    print(dice(4,[]))

def dice(target,ans):
    if target==0:
        print(ans)
        return 1
    count=0
    for i in range(1,6):
        if i <= target:
            ans.append(i)
            count=count+dice(target-i,ans)
    return count

main()
        