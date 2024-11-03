class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0 or len(self.stack) == 0:
            self.min_stack.append(val)
            self.stack.append(val)
        elif self.min_stack[-1] >= val:
            self.min_stack.append(val)
            self.stack.append(val)
        else:
            self.stack.append(val)
        
        

    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.stack.pop()
            self.min_stack.pop()
        else:
            self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:        
        return self.min_stack[-1]
    
