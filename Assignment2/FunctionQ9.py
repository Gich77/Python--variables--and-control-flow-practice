def has_pair_with_sum(numbers, target_sum):
    seen_numbers = set()
    for num in numbers:
        complement = target_sum - num
        if complement in seen_numbers:
            return True
        seen_numbers.add(num)
    return False

# Example usage
numbers = [1, 2, 3, 4, 5]
target_sum = 8
print(has_pair_with_sum(numbers, target_sum))  # Output will be True (since 3 + 5 = 8)
