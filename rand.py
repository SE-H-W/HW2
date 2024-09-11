
"""
This program is used to randomly shuffle a given array.
"""
import subprocess


def random_array(arr):
    """
    random_array function takes an array as an input 
    And uses subprocess module to randomly generate a number between 1 to 20 
    and store it in the input array at position i.
    """
    shuffled_num = None
    for i,_ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
