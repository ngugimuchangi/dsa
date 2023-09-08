#!/usr/bin/env python3
"""
Radix sort algorithm
- LSD implementation is stable
- MSD implementation is unstable
Time complexity:
- Worst case:
    * O(w.n) where:
        1. n is the number of keys
        2. w is the key length
    * Also O(d.(n + b)) where:
        - d is the number of keys
        - n is the number of elements
        - b is the base of the number system being used
Space complexity:
- Worst case:
    * O(w.n)
"""


def count_sort(arr: list[int], arr_len: int, tense: int):
    """
    Count sort of array based
    on current digit
    """
    temp_arr = [0] * arr_len
    count = [0] * 10

    # get frequency of significant digits
    for i in arr:
        significant_digit = (i // tense) % 10
        count[significant_digit] += 1

    # get prefix sum
    for i in range(1, 10):
        count[i] += count[i - 1]

    # place element in temp_arr
    for i in range(arr_len - 1, -1, -1):
        significant_digit = (arr[i] // tense) % 10
        count[significant_digit] -= 1
        index = count[significant_digit]
        temp_arr[index] = arr[i]

    # place elements in main array
    for i in range(arr_len):
        arr[i] = temp_arr[i]


def lsd_radix_sort(arr: list[int]):
    """
    Radix sort implementation using
    least significant digit approach
    - Params:
        - arr: array of integers
    """
    arr_len = len(arr)
    max_element = max(arr)
    tense = 1

    while max_element / tense > 0:
        count_sort(arr, arr_len, tense)
        tense *= 10


if __name__ == '__main__':
    arr = [102, 101, 19, 48, 13, 99, 71, 13,
           52, 96, 96, 73, 86, 7, 99, 100]
    lsd_radix_sort(arr)
    print(arr)
