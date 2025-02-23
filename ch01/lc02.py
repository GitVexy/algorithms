def median_followers(nums: list[int]):
    if nums:
        median = float
        new_nums = sorted(nums.copy())
        if len(new_nums) % 2 == 0:
            mid_low = new_nums[(len(new_nums) // 2) - 1]
            mid_high = new_nums[(len(new_nums) // 2)]
            median = (mid_low + mid_high) / 2
        else:
            median = new_nums[len(new_nums) // 2]

        if isinstance(median, float) and float(int(median)) != median:
            return median
        else:
            return int(median)
