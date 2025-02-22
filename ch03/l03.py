def does_name_exist(
    first_names: list[str],
    last_names: list[str],
    full_name: str
) -> bool:
    output = False

    for fname in first_names:
        for lname in last_names:
            if full_name == f"{fname} {lname}": output = True

    return output
