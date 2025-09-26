def solve(s,i,j,isboolean):
    if i>=j:
        if s[i]=='T':
            return True
        else:
            return False
    ans=0
    for k in range(i+1,j,k+2):
        lT=solve(s,i,k-1,True)
        lF=solve(s,i,k-1,False)
        rT=solve(s,k+1,j,True)
        rF=solve(s,k+1,j,False)
        if s[k]=='|':
            if isboolean:
                ans=ans+lT*rF+lF*rT
            else:
                ans=ans+lF*rF+lT*rT
        if s[k]=='&':
            if isboolean:
                ans=ans+lT*rT
            else:
                ans=ans+lF*rF+lT*rF+lF*rT
        if s[k]=='^':
            if isboolean:
                ans=ans+lT*rF+lF*rT
            else:
                ans=ans+lF*rF+lT*rT

def countways(s):
    return solve(s,1,len(s)-1,True)

if __name__ == "__main__":
    s = "T|T&F^T"
    print(countways(s))