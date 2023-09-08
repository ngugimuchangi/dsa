#!/usr/bin/env python3
"""
Bubble sort algorithm
Upper-bound - O(n^2) comparisons and swaps
Lower-bound - O(n) comparisons, O(1) swaps
Average performance - O(n^2) comparisons and swaps
Space-complexity - O(1)
"""


def bubble_sort(arr: list[int]):
    """
    Bubble sort
    Adaptive approach that takes advantage of existing order
    of inputs
    """
    arr_size = len(arr)
    last_idx = 1

    while last_idx:
        last_idx = 0
        for i in range(1, arr_size):
            prev_num, curr_num = arr[i - 1], arr[i]
            if prev_num > curr_num:
                arr[i - 1], arr[i] = curr_num, prev_num
                last_idx = i + 1
        arr_size = last_idx


if __name__ == '__main__':
    arr = [19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100]
    bubble_sort(arr)
    print(arr)
