"""
Multi Assignment over indexing

This script demonstrates two key ideas:
1. Using multi-variable assignment (also called tuple unpacking) to extract values from dictionary items.
2. Implementing a binary search algorithm with safe midpoint calculation.
"""

 # Define a dictionary mapping countries to their capitals
my_dict = {"United States": "Washington DC"}

# Use multi-assignment to unpack the first (key, value) pair from the dictionary
# list(my_dict.items()) converts the dict items to a list of tuples: [('United States', 'Washington DC')]
(country, capital) = list(my_dict.items())[0]

print(f"The capital of {country} is {capital}")

numbers = [1, 2, 3, 5, 6, 7, 8, 8, 9, 10, 10]

target = 9


def binary_search(nums, target):
    start_idx, end_idx = 0, len(nums) - 1
    while True:
        # Calculate midpoint using overflow-safe formula (Not neccesary for Python)
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if nums[mid_idx] == target:
            return f"Target: {target} Index: {mid_idx}"
        elif start_idx >= end_idx:
            return f"Not found"
        elif target < nums[mid_idx]:
            end_idx = mid_idx - 1
        elif target > nums[mid_idx]:
            start_idx = mid_idx + 1


# Perform the binary search and print the result
numbers = [1, 2, 3, 5, 6, 7, 8, 8, 9, 10, 10]
target = 9
search = binary_search(numbers, target)
print(search)

# Swapping Value
x = 10
y = 15

y, x = x, y

print(f"x:{x} y:{y}")