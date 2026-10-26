# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInvalidInputsA(self):
        self.assertEqual(classifyTriangle(1, 1, 0), 'InvalidInput', '0, 1, 1 should be invalid input')

    def testInvalidInputsB(self):
        self.assertNotEqual(classifyTriangle(200, 200, 200), 'InvalidInput', '200, 200, 200 should be valid input')

    def testInvalidInputsC(self):
        self.assertEqual(classifyTriangle(201, 200, 200), 'InvalidInput', '201, 200, 200 should be invalid input')

    def testInvalidInputsD(self):
        self.assertEqual(classifyTriangle(1, '1', 1), 'InvalidInput', '1, "1", 1 should be invalid input')

    def testInvalidInputsE(self):
        self.assertNotEqual(classifyTriangle(True, 1, 1), 'InvalidInput', 'True, 1, 1 should be valid input (this is a quirk of boolean/isinstance() in python)')

    def testInvalidTrianglesA(self):
        self.assertEqual(classifyTriangle(10, 1, 1), 'NotATriangle', '10, 1, 1 should not be a triangle')

    def testInvalidTrianglesB(self):
        self.assertEqual(classifyTriangle(2, 3, 5), 'NotATriangle', '2, 3, 5 should not be a triangle')

    def testInvalidTrianglesC(self):
        self.assertNotEqual(classifyTriangle(1, 2, 4), 'NotATriangle', '1, 2, 4 should be a triangle')

    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1, 1, 1 should be equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertNotEqual(classifyTriangle(1, 1, 5), 'Equilateral', '1, 1, 5 should not be equilateral')
    
    def testRightTrianglesA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3, 4, 5 should be a right triangle')

    def testRightTrianglesB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5, 3, 4 should be a right triangle')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'Scalene', '1, 2, 3 should be scalene')

    def testScaleneTrianglesB(self):
        self.assertNotEqual(classifyTriangle(1, 2, 1), 'Scalene', '1, 2, 1 should not be scalene')

    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'Isosceles', '1, 1, 2 should be isosceles')

    def testIsoscelesTrianglesB(self):
        self.assertNotEqual(classifyTriangle(42, 42, 42), 'Isosceles', '42, 42, 42 should not be isosceles')

    


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

