def sum(nums: list[int]) -> int:
    total = 0
    if nums:
        for num in nums:
            total += num
    return total
