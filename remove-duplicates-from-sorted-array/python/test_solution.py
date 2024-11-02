import pytest
from solution import Solution
from processor import process_solution_class

def test_case_1():
    nums = [1, 1, 2]
    expected_output = [1,2]
    k = process_solution_class(nums)
    assert k == len(expected_output)
    for i in range(k):
        assert nums[i] == expected_output[i]

def test_case_2():
    nums = [0,0,1,1,1,2,2,3,3,4]
    expected_output = [0,1,2,3,4]
    k = process_solution_class(nums)
    assert k == len(expected_output)
    for i in range(k):
        assert nums[i] == expected_output[i]
