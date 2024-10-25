def find_largest_number(numbers):
    largest = numbers[0]  # Start with the first element as the largest
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Example usage
numbers = (10, 20, 30, 40, 50)
print(find_largest_number(numbers))  # Output will be 50
