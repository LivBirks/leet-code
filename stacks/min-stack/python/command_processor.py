from solution import MinStack


def process_commands(commands, values):
    result = []
    stack = None
    
    for i, cmd in enumerate(commands):
        if cmd == "MinStack":
            stack = MinStack()
            result.append(None)
        elif cmd == "push":
            stack.push(values[i])
            result.append(None)
        elif cmd == "pop":
            stack.pop()
            result.append(None)
        elif cmd == "top":
            result.append(stack.top())
        elif cmd == "getMin":
            result.append(stack.getMin())
    
    return result