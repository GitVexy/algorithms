def get_avg_brand_followers(
        all_handles: list[list[str]],
        brand_name: str
) -> float:
    count = 0
    
    for lst in all_handles:
        for s in lst:
            if brand_name in s:
                count += 1

    if count:
        return count / len(all_handles)
    else: return 0.0
