from typing import Any


def bubble_sort(elements: list[Any]) -> None:
    """Sort in-place by swapping adjacent elements. O(n^2) time, O(1) space."""
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    tests = [
        [5, 9, 2, 1, 67, 34, 88, 34],
        [1, 2, 3, 4, 2],
        ["mona", "dhaval", "aamir", "tina", "chang"],
        [],
        [5],
        [2, 1],
        [3, 3, 3],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
    ]

    for elements in tests:
        expected = sorted(elements)
        bubble_sort(elements)
        assert elements == expected, f"Expected {expected}, got {elements}"

    print("All tests passed!")