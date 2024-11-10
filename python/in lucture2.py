def reverse(list):
    result = []

    for element in list:
        result.insert(0, element)

    return result

print (reverse([1, 2, 3, 4, 5, 6]))  # Output: