def is_balanced(
        input_str: str
) -> bool:
    opened = "("
    closed = ")"
    balance = 0
    stack = Stack() # Yes it is

    if len(input_str) % 2 == 1: return False

    for char in input_str:
        stack.push(char)

    for _ in range(stack.size()):
        if stack.peek() == closed:
            balance += 1
        elif stack.peek() == opened:
            balance -= 1
        
        stack.pop()

        if balance < 0:
            return False
    
    return balance == 0

