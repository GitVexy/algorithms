def power_set(input_set):
    if len(input_set) == 1 and isinstance(input_set[0], list):
        input_set = input_set[0]

    if len(input_set) == 0:
        return [[]]

    first = input_set[0]
    
    rest_power_set = power_set(input_set[1:])
    
    final_list = []
    
    for subset in rest_power_set:
        final_list.append([first] + subset)
    
    for subset in rest_power_set:
        final_list.append(subset)
    
    return final_list
