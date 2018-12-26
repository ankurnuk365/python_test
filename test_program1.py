import unittest 

from program1 import add_2_numbers, subtract_2_numbers, divide_2_numbers, multiply_2_numbers


class SimpleTest(unittest.TestCase): 

    def test_add(self):         
        self.assertEqual(add_2_numbers(4,2),6)

    def test_subtract(self):         
        self.assertEqual(subtract_2_numbers(4,2),2)

    def test_divide(self):         
        self.assertEqual(divide_2_numbers(4,2),2)

    def test_multiply(self):         
        self.assertEqual(multiply_2_numbers(4,2),8)


if __name__ == '__main__': 
    unittest.main() 
