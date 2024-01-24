def filter_strings(array):
    result = []
    for string in array:
        if len(string) <= 3:
            result.append(string)
    return result