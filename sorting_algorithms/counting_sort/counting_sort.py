#!/usr/bin/env python3
"""
Counting sort algorithm
Time complexity O(n + k), where k is the range
of non-negative key values
Space complexity O(n + k)
"""


def counting_sort(arr: list[int]) -> tuple[list[int], list[int]]:
    """
    Counting sort
    """
    array_size = len(arr)
    last_idx = array_size - 1
    asc_arr = [0 for _ in range(array_size)]
    desc_arr = asc_arr.copy()
    count = [0 for _ in range(max(arr) + 1)]

    # count occurrences
    for num in arr:
        count[num] += 1

    # prefix count
    for i in range(len(count)):
        if i:
            count[i] += count[i - 1]

    # sorting the array
    # array_size - 1 because negative indices
    # start from -1 and not 0. -array_size is
    # a valid index in this case
    for i in range(-1, -array_size - 1, -1):
        key = arr[i]
        count[key] -= 1
        asc_idx = count[key]
        desc_idx = last_idx - count[key]
        asc_arr[asc_idx] = arr[i]
        desc_arr[desc_idx] = arr[i]

    return asc_arr, desc_arr


if __name__ == '__main__':
    array = [19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7]
    asc_arr, desc_arr = counting_sort(array)
    print(f'Ascending sort:\n{asc_arr}')
    print(f'Descending sort:\n{desc_arr}')
