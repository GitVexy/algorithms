class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        return None if not self.items else self.items[-1]

    def pop(self):
        return None if not self.items else self.items.pop()

