from typing import Any


def selection_sort(arr: list[Any]) -> None:
    """Sort in-place by selecting the minimum. O(n^2) time, O(1) space."""
    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5],
        [3, 3, 3],  # All equal
        [2, 1],     # Two elements
    ]

    for elements in tests:
        expected = sorted(elements)
        selection_sort(elements)
        assert elements == expected, f"Expected {expected}, got {elements}"

    print("All tests passed!")