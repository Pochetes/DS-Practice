class Stack:
    def __init__(self):
        self.stack = []

    # pops most recently added out of the stack
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    
    # pushes most recent item into the stack
    def push(self, item):
        self.stack.append(item)
    
    # returns the size of the stack
    def size(self):
        return len(self.stack)
    
    def print(self):
        print("bottom")
        for item in self.stack:
            print(item)
        print("^top")
    
    # checks if stack is empty or not
    def isEmpty(self):
        if not self.stack:
            return True
        else:
            return False

def main():
    theStack = Stack()

    theStack.push(1)
    theStack.push(100)
    theStack.push(202)
    theStack.push(2)

    theStack.print()
    theStack.pop()
    print()
    theStack.print()



if __name__ == "__main__":
    main()