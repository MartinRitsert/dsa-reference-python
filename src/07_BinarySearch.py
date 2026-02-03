from __future__ import annotations

from typing import Any


# # Linear search (as reference)
# def linear_search(numbers_list, number_to_find):
#     """Search by checking each element sequentially. O(n) time, O(1) space."""
#     for index, element in enumerate(numbers_list):
#         if element == number_to_find:
#             return index
#     return -1


# # Recursive approach:
# def binary_search(numbers_list: list[Any], number_to_find: Any, left_index: int, right_index: int) -> int:
#     """Search a sorted list recursively. O(log n) time, O(log n) space."""
#     if right_index < left_index:
#         return -1
#
#     mid_index = left_index + (right_index - left_index) // 2
#     if mid_index >= len(numbers_list) or mid_index < 0:
#         return -1
#
#     mid_number = numbers_list[mid_index]
#
#     if mid_number == number_to_find:
#         return mid_index
#
#     elif mid_number < number_to_find:
#         left_index = mid_index + 1
#     else:
#         right_index = mid_index - 1
#
#     return binary_search(numbers_list, number_to_find, left_index, right_index)

# Iterative approach:
def binary_search(numbers_list: list[Any], number_to_find: Any) -> int:
    """Search a sorted list iteratively. O(log n) time, O(1) space."""
    left_index = 0
    right_index = len(numbers_list) - 1

    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        elif mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


if __name__ == '__main__':
    # Test cases: (array, target, expected_result)
    test_cases = [
        ([12, 15, 17, 19, 21, 24, 45, 67], 21, 4),   # Found in middle
        ([12, 15, 17, 19, 21, 24, 45, 67], 12, 0),   # Found at first
        ([12, 15, 17, 19, 21, 24, 45, 67], 67, 7),   # Found at last
        ([12, 15, 17, 19, 21, 24, 45, 67], 10, -1),  # Not found (before all)
        ([12, 15, 17, 19, 21, 24, 45, 67], 70, -1),  # Not found (after all)
        ([12, 15, 17, 19, 21, 24, 45, 67], 20, -1),  # Not found (between)
        ([], 5, -1),                                  # Empty array
        ([5], 5, 0),                                  # Single element (found)
        ([5], 3, -1),                                 # Single element (not found)
    ]

    # Test iterative binary search
    for arr, target, expected in test_cases:
        result = binary_search(arr, target)
        assert result == expected, f"Iterative: search {target} in {arr}, got {result}, expected {expected}"

    print("All tests passed!")