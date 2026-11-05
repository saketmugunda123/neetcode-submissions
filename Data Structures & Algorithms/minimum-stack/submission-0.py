class MinStack:

    def __init__(self):
        #Create a stack that tracks the minimum value at each value in the 
        #original stack
        self.getMinStack = []
        self.stack = []
        
    def push(self, val: int) -> None:

        if len(self.getMinStack) == 0:
            self.getMinStack.append(val)
        elif self.getMinStack[-1] < val:
            self.getMinStack.append(self.getMinStack[-1])
        else:
            self.getMinStack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.getMinStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.getMinStack[-1]
        
