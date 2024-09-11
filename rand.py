"""
Module for generating random arrays.
"""


import subprocess


def random_array(arr):
    '''
    Generate a random array by shuffling numbers.

    Args:
        arr (list): List of None values to be replaced by random numbers.

    Returns:
        list: List populated with random numbers.
    '''
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
