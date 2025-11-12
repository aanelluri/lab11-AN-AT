#https://github.com/aanelluri/lab11-AN-AT
# Partner 1: Anish Nelluri
# Partner 2: Alexander Tariam

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(1,0),1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1,0),1)
        self.assertEqual(subtract(0,1),-1)
        self.assertEqual(subtract(1,-1),2)
        self.assertEqual(subtract(-1,1),-2)

    ######## Partner 1
    def test_multiply(self):
            self.assertEqual(mul(5, -2), -10)
            self.assertEqual(mul(0, 12345), 0)
            self.assertEqual(mul(3, 4), 12)

    def test_divide(self):
        self.assertAlmostEqual(div(2, 7), 3.5)
        self.assertAlmostEqual(div(3, -9), -3.0)
        with self.assertRaises(ZeroDivisionError):
            div(0, 1)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 4), 2)
        self.assertEqual(logarithm(2,2), 1)
        self.assertEqual(logarithm(2,1), 0)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 1)
        with self.assertRaises(ValueError):
            logarithm(-2, 8)
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -8)
        with self.assertRaises(ValueError):
            logarithm(2, 0)
        # a valid case to ensure function works
        self.assertAlmostEqual(log(2, 8), 3.0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
