from typing import Any


def shell_sort(arr: list[Any]) -> None:
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

# def foo(arr: list[Any]) -> None:
#     size = len(arr)
#     gap = size // 2
#     gap = 3
#     for i in range(gap, size):
#         anchor = arr[i]
#         j = i
#         while j >= gap and arr[j - gap] > anchor:
#             arr[j] = arr[j - gap]
#             j -= gap
#         arr[j] = anchor


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