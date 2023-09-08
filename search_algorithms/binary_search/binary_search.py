"""
Binary search algorithm
Worst-case: O(log(n))
Best-case: O(1) - item at the beginning of array
Average-case: O(log(n))
Space complexity: O(1)
"""


def binary_search(arr: list[int], num: int):
    """
    Binary search
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < num:
            left = mid + 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            return mid
    return None


def binary_search_right_most(arr: list[int], num: int):
    """
    Binary search for right most or last element
    """
    last_idx = len(arr) - 1
    left = 0
    right = last_idx

    while left <= right:
        mid = (left + right) // 2
        if (mid == last_idx or arr[mid + 1] > num) and arr[mid] == num:
            return mid
        if arr[mid] <= num:
            left = mid + 1
        else:
            right = mid - 1
    return None


def binary_search_left_most(arr: list[int], num: int):
    """
    Binary search for left most element
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or arr[mid - 1] < num) and arr[mid] == num:
            return mid
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return None


if __name__ == '__main__':
    arr = [i for i in range(100) if i % 2]
    arr = [7,  13, 13, 13, 13, 13, 19, 48, 52, 71,  73,
           86,  96, 96, 99, 99, 100, 101, 102]

    num = 13
    index = binary_search(arr, num)
    print('Normal binary search:', index, '=>', arr[index])
    index = binary_search_right_most(arr, num)
    print('Right most binary search:', index, '=>', arr[index])
    index = binary_search_left_most(arr, num)
    print('Left most binary search:', index, '=>', arr[index])
