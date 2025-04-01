import unittest
import math
import pytest
from src import calculator

class TestSolveQuadraticFormula(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(calculator.solve_quadratic_formula.solve_quadratic_formula(1, 2, 1), (-1.0, -1.0))
        self.assertEqual(calculator.solve_quadratic_formula.solve_quadratic_formula(1, -3, 2), (2.0, 1.0))

    def test_exceptions(self):
        self.assertRaises(TypeError, calculator.solve_quadratic_formula.solve_quadratic_formula, "1", 2, 3)
        self.assertRaises(SyntaxError, calculator.solve_quadratic_formula.solve_quadratic_formula, 0, 2, 3)
        self.assertRaises(NameError, calculator.solve_quadratic_formula.solve_quadratic_formula, 1, 5, 3)
        self.assertRaises(ValueError, calculator.solve_quadratic_formula.solve_quadratic_formula, 1, 2, 3)