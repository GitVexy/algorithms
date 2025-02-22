def count_names(
    list_of_lists: list[list[str]],
    target_name: str
) -> int:
    
    count = 0
    for lst in list_of_lists:
        for val in lst:
            if val == target_name:
                count += 1

    return count
