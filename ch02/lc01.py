def decayed_followers(intl_followers: int, fraction_lost_daily: float, days: int) -> float:
    return intl_followers * ((1.0 - fraction_lost_daily) ** days)
