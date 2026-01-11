class Stack:
    def __init__(self):
        self.size = 1000
        self.arr = [0] * self.size
        self.top = -1

    def push(self, x):
        if self.top < self.size - 1:
            self.top += 1
            self.arr[self.top] = x
        else:
            print("Stack overflow")

    def pop(self):
        if self.top >= 0:
            x = self.arr[self.top]
            self.top -= 1
            return x
        else:
            print("Stack underflow")
            return -1

    def Top(self):
        if self.top >= 0:
            return self.arr[self.top]
        else:
            print("Stack is empty")
            return -1

    def Size(self):
        return self.top + 1

# Example usage
s = Stack()
s.push(6)
s.push(3)
s.push(7)
print("Top of stack before deleting any element:", s.Top())
print("Size of stack before deleting any element:", s.Size())
print("The element deleted is:", s.pop())
print("Size of stack after deleting an element:", s.Size())
print("Top of stack after deleting an element:", s.Top())

