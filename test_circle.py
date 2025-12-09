import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_unit_area(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)
    
    def test_positive_area(self):
        res = area(5)
        self.assertAlmostEqual(res, 25 * math.pi)
    
    def test_negative_area(self):
        res = area(-3)
        self.assertAlmostEqual(res, 9 * math.pi)
    
    def test_float_area(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25 * math.pi)
    
    def test_large_area(self):
        res = area(1000)
        self.assertAlmostEqual(res, 1000000 * math.pi)
    
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_unit_perimeter(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)
    
    def test_positive_perimeter(self):
        res = perimeter(3)
        self.assertAlmostEqual(res, 6 * math.pi)
    
    def test_negative_perimeter(self):
        res = perimeter(-2)
        self.assertAlmostEqual(res, -4 * math.pi)
    
    def test_float_perimeter(self):
        res = perimeter(1.5)
        self.assertAlmostEqual(res, 3 * math.pi)
    
    def test_large_perimeter(self):
        res = perimeter(500)
        self.assertAlmostEqual(res, 1000 * math.pi)


if __name__ == '__main__':
    unittest.main()