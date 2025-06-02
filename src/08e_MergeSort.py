from typing import Any


# Version 1: Sorting nums list in place and not returning the sorted nums list
def merge_sort(nums: list[Any]) -> None:
    if len(nums) <= 1:
        return

    mid = len(nums) // 2

    left_list = nums[:mid]
    right_list = nums[mid:]
    merge_sort(left_list)
    merge_sort(right_list)

    merge(left_list, right_list, nums)

def merge(a: list[Any], b: list[Any], nums: list[Any]) -> None:
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

    nums[k:] = a[i:] + b[j:]
        
        
# # Version 2: Not changing the original nums list, and returning a sorted copy of the nums list
# def merge_sort(nums: list[Any]) -> list[Any]:
#     if len(nums) <= 1:
#         return nums

#     mid = len(nums) // 2

#     left_list = merge_sort(nums[:mid])
#     right_list = merge_sort(nums[mid:])

#     return merge(left_list, right_list)

# def merge(a: list[Any], b: list[Any]) -> list[Any]:
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

#     result.extend(a[i:])
#     result.extend(b[j:])
    
#     return result


if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)