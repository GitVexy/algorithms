# an = a1 * r ^ (n - 1)

def get_follower_prediction(follower_count: int, influencer_type: str, num_months: int) -> int:

    match influencer_type:
        case "fitness":
            return follower_count * (4 ** num_months)
        case "cosmetic":
            return follower_count * (3 ** num_months)
        case _:
            return follower_count * (2 ** num_months)
