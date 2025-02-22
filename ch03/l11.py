def find_last_name(
    names_dict: dict,
    first_name: str
):
    return names_dict[first_name] if first_name in names_dict.keys() else None
