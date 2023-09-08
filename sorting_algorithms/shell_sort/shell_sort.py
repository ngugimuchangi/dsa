#!/usr/bin/env python3
"""
Shell sort algorithm
Worst-case: O(n^2)
Best-case: O(n log(n))
Average performance: depends on gap
    - Knuth sequence avg performance = O(n ^ 3/2)
Space complexity: O(1)
Not stable due to varying gap that lead to transport of equal elements
past each other
"""


def knuth_sequence_gap(arr_size: int) -> int:
    """
    Finds max gap using knuth sequence
    - 'n + 1 = (n * 3) + 1'
    - Params:
        - arr_size: array size
    - Returns
        - gap: maximum gap size
    """
    gap = 1
    while gap < arr_size:
        gap = (gap * 3) + 1

    return gap


def shell_sort(arr: list[int]) -> None:
    """
    Implementation of shell sort algorithm
    - Params:
        - arr: list of integers
    - Return
        - None
    """
    arr_size = len(arr)
    gap = knuth_sequence_gap(arr_size)

    while gap:
        for i in range(gap, arr_size):
            temp = arr[i]
            j = i
            # insertion sort over gap
            while (j >= gap and arr[j - gap] > temp):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = gap // 3


if __name__ == '__main__':
    arr = [101, 102, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100]
    shell_sort(arr)
    print('Ascending order shell sort:\n', arr)
