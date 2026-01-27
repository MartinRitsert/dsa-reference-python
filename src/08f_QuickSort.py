from typing import Any


# # In case that only one argument "elements" is passed to the function
# def qsort(elements: list[Any]) -> None:
#     n = len(elements)
#     quick_sort(elements, 0, n - 1)
    
def quick_sort(elements: list[Any], start: int, end: int) -> None:
    if start < end:
        pi = partition(elements, start, end)

        # left partition
        quick_sort(elements, start, pi - 1)

        # right partition
        quick_sort(elements, pi + 1, end)
        
# # Lomuto partition scheme
# def partition(elements: list[Any], start: int, end: int) -> int:
#     pivot = elements[end]
#     pivot_index = start

#     for i in range(start, end):
#         if elements[i] < pivot:
#             elements[i], elements[pivot_index] = elements[pivot_index], elements[i]
#             pivot_index += 1

#     elements[pivot_index], elements[end] = elements[end], elements[pivot_index]

#     return pivot_index

# Hoare partition scheme
# In practice, you try to choose a pivot that is close to 
# the median value to achieve O(n log(n))
def partition(elements: list[Any], initial_start: int, initial_end: int) -> int:
    pivot_index = initial_start
    pivot = elements[pivot_index]

    start = initial_start
    end = initial_end

    while start < end:
        while start < initial_end and elements[start] <= pivot:
            start += 1

        while end > initial_start and elements[end] > pivot:
            end -= 1

        if start < end:
            elements[start], elements[end] = elements[end], elements[start]

    elements[pivot_index], elements[end] = elements[end], elements[pivot_index]
    return end


if __name__ == '__main__':
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [],                         # Empty
        [5],                        # Single element
        [2, 1],                     # Two elements
        [5, 5, 5, 5, 5],           # All equal (critical for partition)
        [1, 2, 3, 4, 5],           # Already sorted
        [5, 4, 3, 2, 1],           # Reverse sorted
        [3, 1, 3, 2, 3],           # Duplicates throughout
    ]

    for elements in tests:
        expected = sorted(elements)
        quick_sort(elements, 0, len(elements) - 1)
        assert elements == expected, f"Expected {expected}, got {elements}"

    print("All tests passed!")