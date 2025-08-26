class Queue():
    def __init__(self):
        self.list=[]
        self.size=0

    def __str__(self):
        ans=""
        for i in range(len(self.list)):
            ans=ans+" - "+(str(self.list[i]))
        return ans
    
    def push(self,val):
        self.list.append(val)
        self.size=self.size+1

    def pop(self):
        
        if self.size>0:
            ans=self.list[0]
            self.list.remove(self.list[0])
            self.size=self.size-1
            return ans
        else:
            print("Empty Queue")
            return
    
if __name__=="__main__":
    s=Queue()
    s.push(0)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s,s.size)
    print("Deleted" , s.pop())
    print("Deleted" , s.pop())
    print("Deleted" , s.pop())
    print(s)
    print("Deleted" , s.pop())
    print("Deleted" , s.pop())
    print("Deleted" , s.pop())
    print("Deleted" , s.pop())
    print("Deleted" , s.pop())
    print(s)