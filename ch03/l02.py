def find_max(nums: list[int]) -> int:
    max_so_far = -9223372036854775806 # u whore

    for n in nums:
        if n > max_so_far: max_so_far = n

    return max_so_far
