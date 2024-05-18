# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import unittest
import math

class test_math_method(unittest.TestCase): 

     
    def test_log10(self):
        # Testing method log10 
        self.assertEqual(math.log10(5),  0.6989700043360189)
        pass 

    def test_square_root(self): 
        # Test sqrt method 
        self.assertEqual(math.sqrt(2), 1.4142135623730951)
        pass

    
