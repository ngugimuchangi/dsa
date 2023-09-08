#!/usr/bin/env python3
"""
Merge sort algorithm
Worst-case: O(n(log(n)))
Best-case: O(n(log(n)))
Average-case: O(n(log(n)))
Worst-case-space-complexity:
    - O(n) auxillary space
    - O(1) with linked list
    - Stack size is O(log(n))
Characteristics:
    - Stable
    - Not adaptive
"""


def merge_sort(arr: list[int], size: int):
    """
    Merge sort
    """
    if size <= 1:
        return

    mid = size // 2
    right_arr = arr[0:mid]
    left_arr = arr[mid:]
    merge_sort(right_arr, mid)
    merge_sort(left_arr, size - mid)
    merge(arr, left_arr, right_arr)


def merge(arr: list[int], left_arr: list[int], right_arr: list[int]):
    """
    Merges right and left array by placing the items
    in the right slot
    """
    idx = 0
    left_idx = 0
    right_idx = 0
    left_arr_size = len(left_arr)
    right_arr_size = len(right_arr)

    while (left_idx < left_arr_size and right_idx < left_arr_size):
        if left_arr[left_idx] < right_arr[right_idx]:
            arr[idx] = left_arr[left_idx]
            idx += 1
            left_idx += 1
            continue
        arr[idx] = right_arr[right_idx]
        idx += 1
        right_idx += 1
    while (left_idx < left_arr_size):
        arr[idx] = left_arr[left_idx]
        left_idx += 1
        idx += 1
    while (right_idx < right_arr_size):
        arr[idx] = right_arr[right_idx]
        right_idx += 1
        idx += 1


if __name__ == '__main__':
    arr = [102, 101, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100]
    arr = [i for i in range(25, 0, -1)]
    print(arr)
    merge_sort(arr, len(arr))
    print('Ascending merge sort:\n', arr)
