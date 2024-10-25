def list_to_dict(tuples_list):
    result = {}
    for key, value in tuples_list:
        result[key] = value
    return result

# Example usage
tuples_list = [("apple", 5), ("banana", 3), ("cherry", 7)]
print(list_to_dict(tuples_list))  # Output will be {'apple': 5, 'banana': 3, 'cherry': 7}
