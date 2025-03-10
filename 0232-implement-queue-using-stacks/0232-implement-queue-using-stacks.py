from collections import deque 
class MyQueue:

    def __init__(self):
        self.stack = deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        

    def pop(self) -> int:
        if self.stack:
            return self.stack.popleft()
        return -1
        

    def peek(self) -> int:
        if self.stack:
            return self.stack[0]
        return -1

        

    def empty(self) -> bool:
        if not self.stack:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()