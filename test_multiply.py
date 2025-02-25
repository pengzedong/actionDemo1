import unittest
from target_code import Calculator

class TestMultiply(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 3), 9)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)

if __name__ == '__main__':
    unittest.main()
