def fib( n: int ) -> int:
    
    current, grandparent, parent = 0, 0, 1

    if n == 0:
        return grandparent
    elif n == 1:
        return 1

    for _ in range(1, n):
        current = grandparent + parent
        grandparent, parent = parent, current

    return current
