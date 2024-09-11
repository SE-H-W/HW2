"""
Module for implementing merge sort algorithm.
"""

import rand


def merge_sort(arr):
    '''
    Sort an array using the merge sort algorithm.

    Args:
        arr (list): Array to be sorted.

    Returns:
        list: Sorted array.
    '''
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    '''
    Recombine two sorted arrays into a single sorted array.

    Args:
        left_arr (list): Left half of the array.
        right_arr (list): Right half of the array.

    Returns:
        list: Recombined sorted array.
    '''
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    while right_index < len(right_arr):
        merge_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1

    while left_index < len(left_arr):
        merge_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1

    return merge_arr


array = rand.random_array([None] * 20)

arr_out = merge_sort(array)

print(arr_out)
