class Stack():
    def __init__(self):
        self.list=[]
        self.size=0

    def __str__(self):
        ans=""
        for i in range(len(self.list)):
            ans=ans+(str(list[i]))
        return ans
    
    def push(self,val):
        self.list.append(val)
        self.size=self.size+1

    def pop(self):
        ans=self.list.pop
        self.size=self.size-1
        return ans
    
if __name__=="__main__":
    s=Stack()
    s.push(0)
    s.push(1)
    print(s)
    print(s.pop)
    print(s)