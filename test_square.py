import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        """Тест площади с нулевой стороной"""
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_unit_area(self):
        """Тест площади со стороной 1"""
        res = area(1)
        self.assertEqual(res, 1)
    
    def test_positive_area(self):
        """Тест площади с положительной стороной"""
        res = area(5)
        self.assertEqual(res, 25)
    
    def test_negative_area(self):
        """Тест площади с отрицательной стороной"""
        res = area(-3)
        self.assertEqual(res, 9)
    
    def test_float_area(self):
        """Тест площади с дробной стороной"""
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25)
    
    def test_large_area(self):
        """Тест площади с большой стороной"""
        res = area(1000)
        self.assertEqual(res, 1000000)
    
    def test_small_float_area(self):
        """Тест площади с маленькой дробной стороной"""
        res = area(0.1)
        self.assertAlmostEqual(res, 0.01)
    
    def test_zero_perimeter(self):
        """Тест периметра с нулевой стороной"""
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_unit_perimeter(self):
        """Тест периметра со стороной 1"""
        res = perimeter(1)
        self.assertEqual(res, 4)
    
    def test_positive_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)
    
    def test_negative_perimeter(self):
        res = perimeter(-3)
        self.assertEqual(res, -12)
    
    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 10.0)
    
    def test_large_perimeter(self):
        res = perimeter(1000)
        self.assertEqual(res, 4000)
    
    def test_small_float_perimeter(self):
        res = perimeter(0.5)
        self.assertAlmostEqual(res, 2.0)


if __name__ == '__main__':
    unittest.main()