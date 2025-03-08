# Subtractive approach

def subtractive_num_countries_in_days(
        max_days: int,
        factor: float
) -> int:

    time_left = max_days
    count = 0
    time_in_country = 1

    while time_left >= time_in_country:
        time_left -= time_in_country
        time_in_country *= factor
        count += 1

    return count

# Additive approach

def additive_num_countries_in_days(
        max_days: int, 
        factor: float
) -> int:

    if not max_days: return 0
        
    days: float = 1.0
    time_in_country = factor
    countries = 1
    
    while days + factor < max_days:
        days += time_in_country
        if days > max_days: break
        countries += 1
        time_in_country *= factor

    return countries

