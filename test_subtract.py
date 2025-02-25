import unittest
from target_code import Calculator

class TestSubtract(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 20), -10)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

if __name__ == '__main__':
    unittest.main()
