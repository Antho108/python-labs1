from unittest_function import new_function
import unittest


class TestNewFunction(unittest.TestCase):

    def test_new_function_result(self): 
        # Test that the result is 7 
        actual_result = new_function()
        self.assertEquals(actual_result, 7)

    def test_new_function_result_isNeg(self):
        # Test if the result is neg 
        actual_result = new_function()
        excpected = actual_result <= 0
        self.assertTrue(excpected)

    def test_new_function_result_isPos(self):
        # Test if the result is pos
        actual_result = new_function()
        expected = actual_result >= 0
        self.assertTrue(expected)

                
if __name__ == "__main__":
    unittest.main()