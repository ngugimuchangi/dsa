#!/usr/bin/env python3
"""
Bucket sort algorithm
Place elements in buckets and sort each bucket
Worst-case: O(n^2) - when most element are in the same bucket
Best-case: O(n + k) - when elements are uniformly distributed
Average-case: O(n + k + (n^2)/k) - when elements are uniformly distributed
Best-case space complexity: O(n) auxillary
Worst-case space complexity: O(n + k) auxillary
"""


def bucket_hash(num: int, max: int, bucket_size: int) -> int:
    """
    Hash function to determine which bucket to place a number in
    """
    max = max + 1
    return (bucket_size * num) // max


def insertion_sort(arr: list[int]) -> list[int]:
    """
    Insertion sort sub-routine for bucket sort
    """
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


def bucket_sort(arr: list[int], bucket_size: int = 5) -> list[int]:
    """
    Implementation of bucket sort algorithm
    """
    max_val = max(arr)
    buckets = [[] for _ in range(bucket_size)]
    for i in range(len(arr)):
        buckets[bucket_hash(arr[i], max_val, bucket_size)].append(arr[i])

    for i in range(bucket_size):
        insertion_sort(buckets[i])
    return [val for bucket in buckets for val in bucket]


def sort(arr: list[int]) -> list[int]:
    """
    Driver function for bucket sort
    """
    return bucket_sort(arr)


if __name__ == '__main__':
    arr = [102, 101, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100]
    print('Unsorted array:', arr)
    arr = sort(arr)
    print('Ascending bucket sort:', arr)
