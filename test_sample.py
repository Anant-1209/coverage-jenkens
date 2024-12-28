# test_sample.py
import unittest
from program1 import nth_fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(nth_fibonacci(5), 5)
        self.assertEqual(nth_fibonacci(0), 0)
        self.assertEqual(nth_fibonacci(1), 1)
        self.assertEqual(nth_fibonacci(10), 55)

if __name__ == "__main__":
    unittest.main()
