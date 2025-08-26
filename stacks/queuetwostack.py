#https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue:

    def __init__(self):
        self.list1=[]
        self.list2=[]

    def push(self, x: int) -> None:
        self.list1.append(x)

    def pop(self) -> int:
        for i in range(len(self.list1)):
            self.list2.append(self.list1.pop())
        size=len(self.list2)
        ans=self.list2.pop()
        for i in range(len(self.list2)):
            self.list1.append(self.list2.pop())
        return ans

    def peek(self) -> int:
        return self.list1[0]

    def empty(self) -> bool:
        return len(self.list1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()