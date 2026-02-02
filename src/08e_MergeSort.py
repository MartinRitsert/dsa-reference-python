from typing import Any


# Index-based merge sort (standard textbook approach — O(n) auxiliary space):
def merge_sort(nums: list[Any]) -> None:
    """Sort in-place by dividing and merging. O(n log n) time, O(n) space."""
    _merge_sort(nums, 0, len(nums))


def _merge_sort(nums: list[Any], start: int, end: int) -> None:
    """Recursively divide and merge a subarray. O(n log n) time, O(n) space."""
    if end - start <= 1:
        return

    mid = (start + end) // 2
    _merge_sort(nums, start, mid)
    _merge_sort(nums, mid, end)

    _merge(nums, start, mid, end)


def _merge(nums: list[Any], start: int, mid: int, end: int) -> None:
    """Merge two sorted subarrays in-place using a temp array. O(n) time, O(n) space."""
    left = nums[start:mid]
    right = nums[mid:end]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1


# # Slice-based merge sort (simpler to read but O(n log n) space due to slicing):
# # Version 1: Sorting nums list in place and not returning the sorted nums list
# def merge_sort(nums: list[Any]) -> None:
#     """Sort in-place by dividing and merging. O(n log n) time, O(n log n) space."""
#     if len(nums) <= 1:
#         return

#     mid = len(nums) // 2

#     left_list = nums[:mid]
#     right_list = nums[mid:]
#     merge_sort(left_list)
#     merge_sort(right_list)

#     merge(left_list, right_list, nums)

# def merge(a: list[Any], b: list[Any], nums: list[Any]) -> None:
#     """Merge two sorted lists into nums. O(n) time, O(1) space."""
#     len_a = len(a)
#     len_b = len(b)

#     i = j = k = 0

#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             nums[k] = a[i]
#             i += 1
#         else:
#             nums[k] = b[j]
#             j += 1
#         k += 1

#     while i < len_a:
#         nums[k] = a[i]
#         i += 1
#         k += 1

#     while j < len_b:
#         nums[k] = b[j]
#         j += 1
#         k += 1


# # Slice-based merge sort (simpler to read but O(n log n) space due to slicing):
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


if __name__ == "__main__":
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
