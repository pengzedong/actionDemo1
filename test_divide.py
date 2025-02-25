import unittest
from target_code import Calculator

class TestDivide(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(1, 1), 1)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(5, 0), "Error! Division by zero.")

if __name__ == '__main__':
    unittest.main()
