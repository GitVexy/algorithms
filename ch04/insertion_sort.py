def insertion_sort(
        nums: list[int]
) -> list[int]:
    
    for i in range(0, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            swap = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = swap
            j -= 1
    return nums
