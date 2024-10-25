def print_even_value_keys(input_dict):
    for key, value in input_dict.items():
        if value % 2 == 0:
            print(key)

# Example usage
example_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_value_keys(example_dict)  # Output will be 'a' and 'c'
