import unittest
from target_code import Calculator

class TestPower(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(7, 1), 7)
        self.assertEqual(self.calc.power(4, -1), 0.25)

if __name__ == '__main__':
    unittest.main()
