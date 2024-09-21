import unittest
from solution import removeDuplicates

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(removeDuplicates([1,1,2]), expected_output)
    
    def test_case_2(self):
        self.assertEqual(removeDuplicates([0,0,1,1,1,2,2,3,3,4]), expected_output)

if __name__ == '__main__':
    unittest.main()