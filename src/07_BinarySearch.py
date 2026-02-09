from __future__ import annotations

from typing import Any


# # Recursive approach:
# def binary_search(elements: list[Any], target: Any, left_index: int, right_index: int) -> int:
#     """Search a sorted list recursively. O(log n) time, O(log n) space."""
#     if right_index < left_index:
#         return -1
#
#     mid_index = (left_index + right_index) // 2
#     if mid_index >= len(elements) or mid_index < 0:
#         return -1
#
#     mid_value = elements[mid_index]
#
#     if mid_value == target:
#         return mid_index
#
#     elif mid_value < target:
#         left_index = mid_index + 1
#     else:
#         right_index = mid_index - 1
#
#     return binary_search(elements, target, left_index, right_index)


# Iterative approach:
def binary_search(elements: list[Any], target: Any) -> int:
    """Search a sorted list iteratively. O(log n) time, O(1) space."""
    left_index = 0
    right_index = len(elements) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_value = elements[mid_index]

        if mid_value == target:
            return mid_index

        elif mid_value < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


if __name__ == "__main__":
    # Test cases: (array, target, expected_result)
    test_cases = [
        ([12, 15, 17, 19, 21, 24, 45, 67], 21, 4),  # Found in middle
        ([12, 15, 17, 19, 21, 24, 45, 67], 12, 0),  # Found at first
        ([12, 15, 17, 19, 21, 24, 45, 67], 67, 7),  # Found at last
        ([12, 15, 17, 19, 21, 24, 45, 67], 10, -1),  # Not found (before all)
        ([12, 15, 17, 19, 21, 24, 45, 67], 70, -1),  # Not found (after all)
        ([12, 15, 17, 19, 21, 24, 45, 67], 20, -1),  # Not found (between)
        ([], 5, -1),  # Empty array
        ([5], 5, 0),  # Single element (found)
        ([5], 3, -1),  # Single element (not found)
    ]

    # Test iterative binary search
    for arr, target, expected in test_cases:
        result = binary_search(arr, target)
        assert result == expected, (
            f"Iterative: search {target} in {arr}, got {result}, expected {expected}"
        )

    print("All tests passed!")
