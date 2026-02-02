from typing import Any


# Version 1: Sorting nums list in place and not returning the sorted nums list
def merge_sort(nums: list[Any]) -> None:
    """Sort in-place by dividing and merging. O(n log n) time, O(n log n) space."""
    if len(nums) <= 1:
        return

    mid = len(nums) // 2

    left_list = nums[:mid]
    right_list = nums[mid:]
    merge_sort(left_list)
    merge_sort(right_list)

    merge(left_list, right_list, nums)

def merge(a: list[Any], b: list[Any], nums: list[Any]) -> None:
    """Merge two sorted lists into nums. O(n) time, O(1) space."""
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            nums[k] = a[i]
            i += 1
        else:
            nums[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        nums[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        nums[k] = b[j]
        j += 1
        k += 1
        
        
# # Version 2: Not changing the original nums list, and returning a sorted copy of the nums list
# def merge_sort(nums: list[Any]) -> list[Any]:
#     """Sort by dividing and merging into a new list. O(n log n) time, O(n log n) space."""
#     if len(nums) <= 1:
#         return nums

#     mid = len(nums) // 2

#     left_list = merge_sort(nums[:mid])
#     right_list = merge_sort(nums[mid:])

#     return merge(left_list, right_list)

# def merge(a: list[Any], b: list[Any]) -> list[Any]:
#     """Merge two sorted lists into a new list. O(n) time, O(1) space."""
#     len_a = len(a)
#     len_b = len(b)

#     i = j = 0
#     result = []

#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             result.append(a[i])
#             i += 1
#         else:
#             result.append(b[j])
#             j += 1

#     while i < len_a:
#         result.append(a[i])
#         i += 1

#     while j < len_b:
#         result.append(b[j])
#         j += 1

#     return result


if __name__ == '__main__':
    tests = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5],
        [2, 1],
        [3, 3, 3],
        [5, 4, 3, 2, 1],  # Reverse sorted
    ]

    for elements in tests:
        expected = sorted(elements)
        merge_sort(elements)
        assert elements == expected, f"Expected {expected}, got {elements}"

    print("All tests passed!")