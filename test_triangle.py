import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
    
    def test_zero_base_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)
    
    def test_zero_height_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)
    
    def test_positive_area(self):
        res = area(10, 5)
        self.assertEqual(res, 25)
    
    def test_negative_area(self):
        res = area(-6, -4)
        self.assertEqual(res, 12)
    
    def test_mixed_signs_area(self):
        res = area(-8, 3)
        self.assertEqual(res, -12)
    
    def test_float_area(self):
        res = area(5.5, 4.0)
        self.assertAlmostEqual(res, 11.0)
    
    def test_large_area(self):
        res = area(1000, 500)
        self.assertEqual(res, 250000)
    
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_equilateral_perimeter(self):
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)
    
    def test_isosceles_perimeter(self):
        res = perimeter(5, 5, 3)
        self.assertEqual(res, 13)
    
    def test_positive_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_negative_perimeter(self):
        res = perimeter(-3, -4, -5)
        self.assertEqual(res, -12)
    
    def test_mixed_signs_perimeter(self):
        res = perimeter(-3, 4, 5)
        self.assertEqual(res, 6)
    
    def test_float_perimeter(self):
        res = perimeter(2.5, 3.5, 4.0)
        self.assertAlmostEqual(res, 10.0)
    
    def test_large_perimeter(self):
        res = perimeter(1000, 2000, 3000)
        self.assertEqual(res, 6000)


if __name__ == '__main__':
    unittest.main()