import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        """нулевые стороны"""
        res = area(0, 0)
        self.assertEqual(res, 0)
    
    def test_zero_one_side_area(self):
        """одноа нулевая сторона"""
        res = area(5, 0)
        self.assertEqual(res, 0)
    
    def test_square_area(self):
        """a = b"""
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_positive_area(self):
        """положительные стороны"""
        res = area(5, 3)
        self.assertEqual(res, 15)
    
    def test_negative_area(self):
        """отрицательные сторонаы"""
        res = area(-4, -5)
        self.assertEqual(res, 20)
    
    def test_mixed_signs_area(self):
        """разныме заки"""
        res = area(-3, 4)
        self.assertEqual(res, -12)
    
    def test_float_area(self):
        """дробное число"""
        res = area(2.5, 4.0)
        self.assertAlmostEqual(res, 10.0)
    
    def test_large_area(self):
        """большие значения"""
        res = area(1000, 2000)
        self.assertEqual(res, 2000000)
    
    def test_zero_perimeter(self):
        """нулевые стороны"""
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
    
    def test_zero_one_side_perimeter(self):
        """одноа нулевая сторона"""
        res = perimeter(5, 0)
        self.assertEqual(res, 10)
    
    def test_square_perimeter(self):
        """(a = b)"""
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    
    def test_positive_perimeter(self):
        """положительные стороны"""
        res = perimeter(5, 3)
        self.assertEqual(res, 16)
    
    def test_negative_perimeter(self):
        """отрицательнымые стороны"""
        res = perimeter(-4, -5)
        self.assertEqual(res, -18)
    
    def test_mixed_signs_perimeter(self):
        """разные знакаи"""
        res = perimeter(-3, 4)
        self.assertEqual(res, 2)
    
    def test_float_perimeter(self):
        """дробныме стороны"""
        res = perimeter(2.5, 3.5)
        self.assertAlmostEqual(res, 12.0)
    
    def test_large_perimeter(self):
        """большие значения"""
        res = perimeter(1000, 2000)
        self.assertEqual(res, 6000)


if __name__ == '__main__':
    unittest.main()