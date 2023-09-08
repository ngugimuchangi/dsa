#!/usr/bin/env python3
"""
Insertion sort algorithm
Time complexity: O(n^2) comparisons and swaps
Base-case: O(n) comparisons, O(1)swaps
Average performance: O(n^2) comparisons and swaps
Space complexity: O(n^2)
"""


def insertion_sort(arr: list[int]):
    """
    Insertion sort
    """
    for i in range(1, len(arr)):
        j = i
        while j and arr[j - 1] > arr[j]:
            prev_num = arr[j - 1]
            current_num = arr[j]
            arr[j - 1], arr[j] = current_num, prev_num
            j -= 1


def insertion_sort_with_single_swap(arr: list[int]):
    """
    Insertion sort that uses a single swap for the element
    O(n) swaps like selection sort
    """
    for i in range(1, len(arr)):
        current_num = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < current_num:
            prev_num = arr[j]
            arr[j + 1] = prev_num
            j -= 1
        arr[j + 1] = current_num


def recursive_insertion_sort(arr: list[int], last_idx: int):
    """
    Recursive implementation of insertion sort
    """
    if last_idx:
        recursive_insertion_sort(arr, last_idx - 1)
        current_num = arr[last_idx]
        j = last_idx - 1
        while j >= 0 and arr[j] > current_num:
            prev_num = arr[j]
            arr[j + 1] = prev_num
            j -= 1
        arr[j + 1] = current_num


if __name__ == '__main__':
    arr = [102, 101, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100]
    # normal insertion sort
    insertion_sort(arr)
    print(arr)

    # swap optimized insertion sort
    insertion_sort_with_single_swap(arr)
    print(arr)

    # recursive insertion sort
    recursive_insertion_sort(arr, len(arr) - 1)
    print(arr)
