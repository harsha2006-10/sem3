class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after pushes:", stack.items)

# Peek at the top element
print("Top element (peek):", stack.peek())

# Pop elements
print("Popped element:", stack.pop())
print("Stack after pop:", stack.items)

# Peek again
print("Top element after pop:", stack.peek())

# Check if stack is empty
print("Is stack empty?", stack.is_empty())
