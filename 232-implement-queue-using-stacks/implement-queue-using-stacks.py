class MyQueue:

    def __init__(self):
        self.ns = []
        

    def push(self, x: int) -> None:
        return self.ns.append(x)
        

    def pop(self) -> int:
        return self.ns.pop(0)

    def peek(self) -> int:
        return self.ns[0]

    def empty(self) -> bool:
        if not self.ns:
            return True
        return False
           


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()