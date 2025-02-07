import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
    
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
    
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
    
    def test_number(self):
        self.assertEqual(fizzbuzz(2), "2")
    
    def test_fizz_multiple(self):
        self.assertEqual(fizzbuzz(9), "Fizz")
    
    def test_buzz_multiple(self):
        self.assertEqual(fizzbuzz(10), "Buzz")
    
    def test_fizzbuzz_multiple(self):
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

if __name__ == "__main__":
    unittest.main()
