def average_followers(nums: list[int]) -> int:
    if nums:
        sum = 0
        for num in nums:
            sum += num
        return sum / len(nums)
