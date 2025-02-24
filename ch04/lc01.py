def selection_sort(
    nums: list[int]
) -> list[int]:
    
    for i in range(0, len(nums)):
        smallest_idx = i
        for j in range(smallest_idx + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        print(f"{nums[i]} and {nums[smallest_idx]} swapping")
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]

    return nums
