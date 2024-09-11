import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from hw2_debugging import merge_sort 

def test_pass_1():
    assert merge_sort([1,2,3,4,5])==[1,2,3,4,5]

def test_pass_2():
    assert merge_sort([5,4,3,2,1])==[1,2,3,4,5]

def test_pass_3():
    assert merge_sort([-11,2,5,3,8])==[-11,2,3,5,8]