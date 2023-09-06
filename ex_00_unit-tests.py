import unittest

# Import the functions to be tested from your source code
from ex_00 import multiply, multiply2, multiply10, getSecondMax

class TestFunctions(unittest.TestCase):
    
    # Test the multiply function
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-5, 4), -20)
        # Add more test cases here
    
    # Test the multiply2 and multiply10 functions
    def test_multiply2(self):
        self.assertEqual(multiply2(5), 10)
        self.assertEqual(multiply2(0), 0)
        # Add more test cases here

    def test_multiply10(self):
        self.assertEqual(multiply10(7), 70)
        self.assertEqual(multiply10(-3), -30)
        # Add more test cases here

    # Test the getSecondMax function
    def test_getSecondMax(self):
        self.assertEqual(getSecondMax([1, 2, 3, 4, 5]), 4)
        self.assertEqual(getSecondMax([5, 3, 1, 7, 2]), 5)
        # Add more test cases here

if __name__ == '__main__':
    unittest.main()
