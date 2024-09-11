"""
This program implements the merge sort algorithm
"""
import rand
def merge_sort(arr):
    """
    merge_sort function sorts input array using Merge sort algorithm
    """
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    The recombine function is used to combine the sorted inputed arrays into a single array
    """
    left_index = 0
    right_index = 0
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    merge_arr.extend(left_arr[left_index:])
    merge_arr.extend(right_arr[right_index:])

    return merge_arr


x = rand.random_array([None] * 20)
print(x)
arr_out = merge_sort(x)

print(arr_out)
