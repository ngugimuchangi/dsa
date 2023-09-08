#!/usr/bin/env python
"""
Bitonic sort is a comparison-based sorting algorithm that can be run in parallel.
It focuses on converting a random sequence of numbers into a bitonic sequence,
one that monotonically increases, then decreases.
The algorithm consists of two parts:
    1. Creating a bitonic sequence
    2. Sorting it
The first part is done recursively, and the second part is done iteratively.
Length of the input array must be a power of 2.
The algorithm is O(log^2 n) in all cases.
Space complexity is O(n) due to the recursive nature of the algorithm.
"""


def bitonic_merge(arr: list[int], low_index, count, direction: int):
    """
    Merge subroutine for bitonic sort.
    """
    if count > 1:
        k = count // 2
        # log(n) comparisons
        for i in range(low_index, low_index + k):
            if (arr[i] < arr[i + k]) == direction:
                arr[i], arr[i + k] = arr[i + k], arr[i]  # swap
        bitonic_merge(arr, low_index, k, direction)
        bitonic_merge(arr, low_index + k, k, direction)


def bitonic_sort(arr: list[int], low_index: int, count: int, direction: int):
    """
    Implements the bitonic sort algorithm.
    Parameters:
        arr: list of integers to be sorted
        low_index: starting index of the subarray
        count: number of elements to be sorted
        direction: 1 for ascending order, 0 for descending order
    """
    if count > 1:
        k = count // 2
        bitonic_sort(arr, low_index, k, 1)
        bitonic_sort(arr, low_index + k, k, 0)
        bitonic_merge(arr, low_index, count, direction)


def sort(arr: list[int], reverse: bool = False) -> list[int]:
    bitonic_sort(arr, 0, len(arr), reverse)
    return arr


if __name__ == '__main__':
    # arr = [3, 7, 4, 8, 6, 2, 1, 5]
    arr = [5, 10, 11, 11, 7, 2, 1, 3]
    print('Unsorted array:', arr)
    print('Ascending bitonic sort:', sort(arr))
    print('Descending bitonic sort:', sort(arr, reverse=True))
