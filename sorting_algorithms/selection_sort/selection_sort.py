#!/usr/bin/env python3
"""
Selection sort algorithm
Upper bound: O(n^2), O(n) swaps
Lower bound: O(n^2), O(1) swaps
Average performance: O(n^2), O(n) swaps
Space complexity: O(1)
Unstable due to swapping
"""


def selection_sort(arr: list[int]):
    """
    Selection sort
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


def bingo_sort(arr: list[int]):
    """
    Bingo sort algorithm
    Variant of selection sort
    Worst case: O(M * N) - M number of distinct element
    Worst case: I(N + M^2)
    Space complexity O(1)
    Works best for case where there is repetitive elements
    """
    bingo = max(arr)
    smallest = min(arr)
    next_bingo = smallest
    swap_index = 0
    while bingo > next_bingo:
        for i in range(swap_index, len(arr)):
            if arr[i] == bingo:
                arr[i], arr[swap_index] = arr[swap_index], arr[i]
                swap_index += 1
            elif arr[i] > next_bingo:
                next_bingo = arr[i]

        bingo = next_bingo
        next_bingo = smallest


if __name__ == '__main__':
    arr = [19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100]
    # simulation of an array with a single repetitive element
    # arr = [19 for _ in range(100)]
    selection_sort(arr)
    print(arr)

    bingo_sort(arr)
    print(arr)
