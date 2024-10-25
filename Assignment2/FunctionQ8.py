def keys_with_values_greater_than_n(input_dict, n):
    result = []
    for key, value in input_dict.items():
        if value > n:
            result.append(key)
    return result

# Example usage
example_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print(keys_with_values_greater_than_n(example_dict, n))  # Output will be ['a', 'b']
