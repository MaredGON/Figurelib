import unittest
from figures import Circle, Triangle, area_calculation

class TestGeometry(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(7)
        self.assertAlmostEqual(circle.area(), 153.93804002589985, places=5)

    def test_triangle_area(self):
        triangle = Triangle(6, 8, 10)
        self.assertAlmostEqual(triangle.area(), 24.0, places=5)

    def test_right_triangle(self):
        triangle = Triangle(5, 12, 13)
        self.assertTrue(triangle.is_right_triangle())

    def test_not_right_triangle(self):
        triangle = Triangle(5, 6, 7)
        self.assertFalse(triangle.is_right_triangle())

    def test_compile_area_circle(self):
        circle = Circle(3)
        self.assertAlmostEqual(area_calculation(circle), 28.274333882308138, places=5)

    def test_compile_area_triangle(self):
        triangle = Triangle(7, 24, 25)
        self.assertAlmostEqual(area_calculation(triangle), 84.0, places=5)

if __name__ == '__main__':
    unittest.main()
