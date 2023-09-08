#!/usr/bin/env python3
"""
Cocktail shaker sort aka bi-directional bubble sort
Helps move turtles in bubble sort
Worst-case: O(n^2)
Best-case: O(n)
Average-case: O(n^2)
Space-complexity: O(1)
"""


def cocktail_shaker_sort(arr: list[int]) -> None:
    """
    Implementation of cocktail shaker sort
    - Params:
        - arr: array of integers
    - Return:
        - nothing
    """
    swapped = True
    last_index = len(arr)
    first_index = 0

    while swapped:
        swapped = False
        for i in range(first_index + 1, last_index):
            current_num = arr[i]
            prev_num = arr[i - 1]
            if prev_num > current_num:
                arr[i], arr[i - 1] = prev_num, current_num
                swapped = True
                last_index = i

        if not swapped:
            return

        for i in range(last_index - 1, first_index, -1):
            current_num = arr[i]
            next_num = arr[i - 1]
            if current_num < next_num:
                arr[i], arr[i - 1] = next_num, current_num
                swapped = True
                first_index = i - 1


if __name__ == '__main__':
    arr = [101, 102, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100]
    # arr = [i for i in range(51)]
    cocktail_shaker_sort(arr)
    print('Ascending cocktail shaker sort:\n', arr)
