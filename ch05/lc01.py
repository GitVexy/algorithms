def exponential_growth(
    followers: int,
    factor: int,
    days: int
) -> list[int]:

    result = []
    
    for _ in range(days + 1):
        result.append(followers)
        followers *= factor
    
    return result
