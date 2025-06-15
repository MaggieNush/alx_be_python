import unittest 
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,4), 6)
        self.assertEqual(self.calc.add(-2,2), 0)
        self.assertEqual(self.calc.add(4,0), 4)
        self.assertEqual(self.calc.add(8,-2), 6)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2,-3), 5)
        self.assertEqual(self.calc.subtract(8,4), 4)
        self.assertEqual(self.calc.subtract(0,4), -4)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(7,5), 35)
        self.assertEqual(self.calc.multiply(0,9), 0)
        self.assertEqual(self.calc.multiply(6,1), 6)
        self.assertEqual(self.calc.multiply(-4,-3), 12)

    def test_division(self):
        self.assertEqual(self.calc.divide(8,2), 4)
        self.assertEqual(self.calc.divide(0,3), 0)
        self.assertEqual(self.calc.divide(9,9), 1)
        self.assertEqual(self.calc.divide(5,0), None)
        self.assertEqual(self.calc.divide(7,2), 3.5)

if __name__ == "__main__":
    unittest.main()
