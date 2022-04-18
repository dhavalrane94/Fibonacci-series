#include unittest library
import unittest
from Fibonacci_series import printFibonacciNumbers
#create class for test cases
class FibonacciTest(unittest.TestCase):
#write test cases as per scenario
    def testCase1(self):
        self.assertEqual(21, printFibonacciNumbers(9), "Valid Case function works for input 9 output expected 21")

if __name__ == '__main__':
    unittest.main()
