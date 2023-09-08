#!/usr/bin/env python3
"""
Quick sort algorithm
Worst-case: O(n^2)
Best-case: O(n(log(n)))
Average-case: O(n(log(n)))
Worst-case space complexity: O(n) auxillary 
Best-case space complexity: O(log(n)) Hoare
** Recursive nature of the algo is responsible
** for the auxillary space
Unstable
"""


def quick_sort(partition_scheme: str, arr: list[int], start_idx: int, last_idx: int):
    """
    Quick sort
    """
    if start_idx >= last_idx:
        return
    match partition_scheme:
        case 'hoare':
            partition = hoare_partitioning(arr, start_idx, last_idx)
            left_arr_last_idx = partition - 1
        case 'lomuto':
            partition = lomuto_partitioning(arr, start_idx, last_idx)
            left_arr_last_idx = partition - 1
        case _:
            raise ValueError('Unsupported partition scheme')

    right_arr_start_idx = partition + 1

    quick_sort(partition_scheme, arr, start_idx, left_arr_last_idx)
    quick_sort(partition_scheme, arr, right_arr_start_idx, last_idx)


def hoare_partitioning(arr, start_idx, last_idx):
    """
    Partitioning using hoare's partitioning scheme
    Leads to O(n(log(n))) even in sorted arrays
    """
    pivot_index = start_idx + ((last_idx - start_idx) // 2)
    pivot = arr[pivot_index]

    i = start_idx - 1
    j = last_idx + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def lomuto_partitioning(arr, start_idx, last_idx):
    """
    Partitioning using lomuto's partitioning scheme
    Leads to O(n^2) in sorted array
    """
    pivot = arr[last_idx]

    i = start_idx - 1
    j = start_idx
    while (j < last_idx):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    i += 1
    arr[i], arr[j] = arr[j], arr[i]
    return i


def median_of_three_pivot(arr, start_idx, last_idx):
    """
    Median of three pivot choice that use the first, middle
    and last index. Median element moved to the start of the
    array or sub-array
    """
    start = start_idx
    end = last_idx
    mid = ((start + end) // 2)

    if arr[mid] < arr[start]:
        arr[mid], arr[start] = arr[start], arr[mid]
    if arr[end] < arr[start]:
        arr[end], arr[start] = arr[start], arr[end]
    if arr[mid] < arr[end]:
        arr[end], arr[mid] = arr[mid], arr[end]

    return arr[end]


if __name__ == '__main__':
    arr = [102, 101, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100]
    # Hoare's partitioning
    quick_sort('hoare', arr, 0, len(arr) - 1)
    print('Ascending quick sort using hoare partitioning:\n', arr)

    # Lomuto partitioning
    quick_sort('lomuto', arr, 0, len(arr) - 1)
    print('Descending quick sort using lomuto partitioning:\n', arr)

    # Median of three pivot selection
    print('Median of three pivot selection:\n',
          median_of_three_pivot([1, 10, 7], 0, 2))
