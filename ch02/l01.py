def get_estimated_spread(audiences_followers: list[int]) -> int:
    if not audiences_followers:
        return 0
    avg_fols = 0
    for fol in audiences_followers:
        avg_fols += fol
    avg_fols /= len(audiences_followers)
    return avg_fols * (len(audiences_followers) ** 1.2)
