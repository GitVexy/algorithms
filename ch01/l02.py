def find_minimum(nums: list[int]) -> int:
    if nums:
        minimum = float("inf")
        for num in nums:
            if num < minimum:
                minimum = num

        return minimum
