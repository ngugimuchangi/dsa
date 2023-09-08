#!/usr/bin/env python

def quick_sort(arr: list[int], l: int, r: int):
    """
    Quick sort
    Time complexity:
     - Best and average case: O(n(log(n)))
     - Worst case: O(n^2)
     Space complexity:
     - O(1)
    """
    if r <= l:
        return
    p = hoare_partition(arr, l, r)
    quick_sort(arr, l, p - 1)
    quick_sort(arr, p + 1, r)


def three_way_quick_sort(arr: list[int], l: int, r: int):
    """
    Quick sort
    Time complexity:
     - Best and average case: O(n(log(n)))
     - Worst case: O(n^2)
     Space complexity:
     - O(1)
    """
    if r <= l:
        return
    lt, gt = three_way_partition(arr, l, r)
    three_way_quick_sort(arr, l, lt - 1)
    three_way_quick_sort(arr, gt + 1, r)


def partition(arr: list, l: int, r: int) -> int:
    """
    Lomuto partition
    """
    i, j = l, r + 1
    pivot = arr[l]

    while True:
        # increase left pointer until it encounters
        # a value gt pivot
        i += 1
        while arr[i] < pivot:
            if i == r:
                break
            i += 1
        j -= 1
        # increment right pointer until it encounter
        # a value lt pivot
        while arr[j] > pivot:
            # this guard is redundant in this case but will be needed
            # if pivot is changes to the last element
            if j == l:
                break
            j -= 1
        if i >= j:
            break
        # swap the two values that are out of order
        arr[i], arr[j] = arr[j], arr[i]
    # Swap the pivot number and number at j
    # Note that j will be less or equal to pivot at this point
    arr[l], arr[j] = arr[j], arr[l]
    return j


def lomuto_partition(arr: list[int], l: int, r: int) -> int:
    """
    Lomuto partitioning
    """
    pivot = arr[r]
    i, j = l - 1, l

    while j < r:
        # move left pointer by one and swap the positions
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    i += 1
    arr[i], arr[j] = arr[j], arr[i]
    return i


def hoare_partition(arr: list, l: int, r: int) -> int:
    """
    Hoare's partition
    """
    pivot = arr[l + (r - l) // 2]
    i, j = l - 1,  r + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1

        if j <= i:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def three_way_partition(arr: list[int], l: int, r: int) -> int:
    """
    Three way partition
    - Returns two pointers gt and lt
    - values before gt are less than pivot
    - values after lt are greater than pivot
    """
    pivot = arr[l]
    lt, i, gt, = l, l + 1, r

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1
    return lt, gt


if __name__ == "__main__":
    arr = [102, 101, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100]
    # arr = list(range(100, 0, -1))
    print(arr)
    quick_sort(arr, 0, len(arr) - 1)
    # three_way_quick_sort(arr, 0, len(arr) - 1)
    print(arr)
