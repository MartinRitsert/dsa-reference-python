from typing import Any


def insertion_sort(elements: list[Any]) -> None:
    """Sort in-place by inserting each element into its correct position. O(n^2) time, O(1) space."""
    for i in range(1, len(elements)):
        anchor = elements[i]

        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        
        elements[j + 1] = anchor


if __name__ == '__main__':
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6],
        [2, 1],
        [3, 3, 3],
        [5, 4, 3, 2, 1],  # Reverse sorted
    ]

    for elements in tests:
        expected = sorted(elements)
        insertion_sort(elements)
        assert elements == expected, f"Expected {expected}, got {elements}"

    print("All tests passed!")