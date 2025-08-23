#https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) :
        s,f=n,n
        while not f==1:
            s=self.square(s)
            f=self.square(f)
            f=self.square(f)
            if f==s and not f==1:
                return False
        return True
    def square(self,n):
        ans=0
        while not n==0:
            rem=n%10
            ans=ans+rem**2
            n=n//10
        return ans
            


def main():
    sol=Solution()
    print(sol.isHappy(10))

main()