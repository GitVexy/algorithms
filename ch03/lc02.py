def remove_duplicates(
        nums: list[int]
) -> list[int]:
    unique = []
    for n in nums:
        if n not in unique:
            unique.append(n)
    return unique
