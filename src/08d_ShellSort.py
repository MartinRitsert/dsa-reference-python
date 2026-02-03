from __future__ import annotations

from typing import Any


def shell_sort(elements: list[Any]) -> None:
    """Sort in-place using diminishing gap insertion sort. O(n^2) time, O(1) space."""
    size = len(elements)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = elements[i]
            j = i
            while j >= gap and elements[j - gap] > anchor:
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = anchor
        gap = gap // 2


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5],
        [2, 1],
        [3, 3, 3],
        [5, 4, 3, 2, 1],  # Reverse sorted
    ]

    for elements in tests:
        expected = sorted(elements)
        shell_sort(elements)
        assert elements == expected, f"Expected {expected}, got {elements}"

    print("All tests passed!")