#!/usr/bin/env python3
"""
Radix sort algorithm
for words
"""


def count_sort(arr: list[str], arr_size: int, letter_index: int):
    """
    Count sort subroutine for ascii letters
    """
    temp_arr = [0] * arr_size
    count = [0] * 128

    # get frequency of current letters
    for word in arr:
        try:
            letter_code = ord(word[letter_index])
        except IndexError:
            letter_code = 0
        count[letter_code] += 1

    # get prefix sum
    for i in range(1, 128):
        count[i] += count[i - 1]

    # place words in temp_arr
    for i in range(arr_size - 1, -1, -1):
        word = arr[i]
        try:
            letter_code = ord(word[letter_index])
        except IndexError:
            letter_code = 0
        count[letter_code] -= 1
        index = count[letter_code]
        temp_arr[index] = word

    # place words in the original array
    for i in range(arr_size):
        arr[i] = temp_arr[i]


def lsd_radix_sort(arr: list[str]):
    """
    Radix sort implementation for words
    using least significant digit approach
    """
    arr_size = len(arr)
    max_word_size = 0
    for word in arr:
        word_size = len(word)
        if word_size > max_word_size:
            max_word_size = word_size

    for i in range(max_word_size - 1, -1, -1):
        count_sort(arr, arr_size, i)


if __name__ == '__main__':
    arr = ['hello', 'hi', 'hey', 'Duncan', 'Dancun', 'Ngugi', 'ab', '21',
           'a', 'da', 'aad', 'xc', 'cy', 'b', 'bad', 'bed', '10', '1']
    lsd_radix_sort(arr)
    print(arr)
