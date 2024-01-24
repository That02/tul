def filter_strings(array):
    result = []
    for string in array:
        if len(string) <= 3:
            result.append(string)
    return result

array1 = ["Hello", "2", "world", ":-)"]
array2 = ["1234", "1567", "-2", "computer science"]
array3 = ["Russia", "Denmark", "Kazan"]