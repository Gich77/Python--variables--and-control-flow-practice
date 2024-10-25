def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
example_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(example_list))  # Output will be [1, 2, 3, 4, 5]
