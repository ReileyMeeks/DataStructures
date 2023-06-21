#Stack ds 

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Example usage:
my_stack = Stack()
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)

print(my_stack.pop())  # Output: 15
print(my_stack.peek())  # Output: 10
print(my_stack.is_empty())  # Output: False
print(my_stack.size())  # Output: 2
