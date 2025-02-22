import math


def log_scale(
    data: list[int],
    base: int
) -> list[int]:

    output = []

    for datapoint in data:
        output.append(math.log(datapoint, base))

    return output
