import math


def logging(a, b):
    print(f"Logarithm base {a} of {b} is: {math.log(b, a)}")


logchecks = [
    (2,      2),  # Logarithm base 2 of 2 is: 1.0
    (2,      4),  # Logarithm base 2 of 4 is: 2.0
    (2,      8),  # Logarithm base 2 of 8 is: 3.0
    (2,     16),  # Logarithm base 2 of 16 is: 4.0
    (10,    10),  # Logarithm base 10 of 10 is: 1.0
    (10,   100),  # Logarithm base 10 of 100 is: 2.0
    (10,  1000),  # Logarithm base 10 of 1000 is: 2.9999999999999996
    (10, 10000),  # Logarithm base 10 of 10000 is: 4.0
    (3,     9),
]

for check in logchecks:
    logging(a=check[0],
            b=check[1])


def get_influencer_score(num_followers, average_engagement_percentage):
    return (
        average_engagement_percentage * math.log(num_followers, 2)
    )
