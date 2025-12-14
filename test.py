#hello this is a comment
import unittest
from main import square_root, factorial, natural_log, power
import math

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("🔍 Running unit tests for the Scientific Calculator...")

    @classmethod
    def tearDownClass(cls):
        print("✅ All test cases ran successfully!")

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_natural_log(self):
        self.assertAlmostEqual(natural_log(1), 0, places=5)
        self.assertAlmostEqual(natural_log(math.e), 1, places=5)
        with self.assertRaises(ValueError):
            natural_log(-1)
        with self.assertRaises(ValueError):
            natural_log(0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -2), 0.25)

if __name__ == "__main__":
    print("🧪 Starting test runner...")
    unittest.main()
