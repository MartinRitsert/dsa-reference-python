from __future__ import annotations

from typing import Any


# Index-based merge sort (standard textbook approach — O(n) auxiliary space):
def merge_sort(elements: list[Any]) -> None:
    """Sort by dividing and merging. O(n log n) time, O(n) space."""
    _merge_sort(elements, 0, len(elements))


def _merge_sort(elements: list[Any], start: int, end: int) -> None:
    """Recursively divide and merge a subarray. O(n log n) time, O(n) space."""
    if end - start <= 1:
        return

    mid = (start + end) // 2
    _merge_sort(elements, start, mid)
    _merge_sort(elements, mid, end)

    _merge(elements, start, mid, end)


def _merge(elements: list[Any], start: int, mid: int, end: int) -> None:
    """Merge two sorted subarrays using temp arrays. O(n) time, O(n) space."""
    left = elements[start:mid]
    right = elements[mid:end]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            elements[k] = left[i]
            i += 1
        else:
            elements[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        elements[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        elements[k] = right[j]
        j += 1
        k += 1


# # Slice-based merge sort (simpler to read but O(n log n) space due to slicing):
# # Version 1: Sorting elements list in place and not returning the sorted elements list
# def merge_sort(elements: list[Any]) -> None:
#     """Sort in-place by dividing and merging. O(n log n) time, O(n log n) space."""
#     if len(elements) <= 1:
#         return

#     mid = len(elements) // 2

#     left_list = elements[:mid]
#     right_list = elements[mid:]
#     merge_sort(left_list)
#     merge_sort(right_list)

#     merge(left_list, right_list, elements)

# def merge(a: list[Any], b: list[Any], elements: list[Any]) -> None:
#     """Merge two sorted lists into elements. O(n) time, O(1) space."""
#     len_a = len(a)
#     len_b = len(b)

#     i = j = k = 0

#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             elements[k] = a[i]
#             i += 1
#         else:
#             elements[k] = b[j]
#             j += 1
#         k += 1

#     while i < len_a:
#         elements[k] = a[i]
#         i += 1
#         k += 1

#     while j < len_b:
#         elements[k] = b[j]
#         j += 1
#         k += 1


# # Slice-based merge sort (simpler to read but O(n log n) space due to slicing):
# # Version 2: Not changing the original elements list, and returning a sorted copy of the elements list
# def merge_sort(elements: list[Any]) -> list[Any]:
#     """Sort by dividing and merging into a new list. O(n log n) time, O(n log n) space."""
#     if len(elements) <= 1:
#         return elements

#     mid = len(elements) // 2

#     left_list = merge_sort(elements[:mid])
#     right_list = merge_sort(elements[mid:])

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
