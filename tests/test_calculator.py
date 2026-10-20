"""Regression coverage for the integer RPN evaluator."""

import unittest

from calculator import evaluate_rpn


class EvaluatorTests(unittest.TestCase):
    def test_arithmetic(self):
        cases = {
            "5 3 +": 8,
            "9 4 -": 5,
            "6 7 *": 42,
            "8 2 /": 4,
            "7 2 /": 3,
            "-7 2 /": -3,
            "-5 3 +": -2,
            "5 1 2 + 4 * + 3 -": 14,
            "  42  ": 42,
        }
        for expression, expected in cases.items():
            with self.subTest(expression=expression):
                self.assertEqual(evaluate_rpn(expression), expected)

    def test_invalid_expressions(self):
        cases = {
            "5 +": "Missing numbers",
            "x": "Invalid token x",
            "5 3": "Too many numbers",
            "": "Too many numbers",
        }
        for expression, message in cases.items():
            with (
                self.subTest(expression=expression),
                self.assertRaisesRegex(ValueError, message),
            ):
                evaluate_rpn(expression)

    def test_division_by_zero_preserves_existing_exception(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate_rpn("1 0 /")
