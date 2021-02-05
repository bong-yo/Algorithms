class Stack:
    def __init__(self):
        self.elements = []

    def push(self, elem):
        '''Add element on top of the stack'''
        self.elements.append(elem)

    def pop(self):
        '''Pop element on top of the stack'''
        if self.elements:
            return self.elements.pop(-1)
        else:
            return False

    def peek(self):
        '''Peek element on top of the stack'''
        if self.elements:
            return self.elements[-1]
        else:
            return False

    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def __len__(self):
        return len(self.elements)

    def __str__(self):
        print(self.elements)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(3)
    print(stack.is_empty())
    print(stack.elements)
    stack.push(4)
    print(stack.is_empty())
    print(stack.elements)
    stack.pop()
    print(stack.is_empty())
    print(stack.elements)
    print(len(stack))
