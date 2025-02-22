def factorial(x, result=1):
    if x == 1:
        return result
    return factorial(x-1, result * x)


def num_possible_orders(num_posts):
    return factorial(num_posts)


for test in range(1, 21):
    print(f"The factorial of {test} is: {factorial(test)}")
