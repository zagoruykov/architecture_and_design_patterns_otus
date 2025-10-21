import unittest
from lessons.module_tests import QuadraticEquation, NaN, PosInf, NegInf


class TestQuadraticEquation(unittest.TestCase):
    def test_roots(self) -> None:
        """Test that solve is working using valid coefficients"""
        test_cases = (
            (1, 0, 1, []),
            (2.5, 2.5, 2.5, []),
            (1, 0, -1, [1.0, -1.0]),
            (1, -2, 1, [1.0, 1.0]),
            (1, 2, 1, [-1.0, -1.0]),
            (1.000000000000000000001, 2, 1, [-1.0, -1.0]),
        )
        for a, b, c, expected_roots in test_cases:
            with self.subTest(a=a, b=b, c=c, expected_roots=expected_roots):
                roots = QuadraticEquation.solve(a, b, c)
                self.assertListEqual(roots, expected_roots)

    def test_invalid_coef(self) -> None:
        """Test invlaid a/b/c coef"""
        test_cases = (
            (NaN, 2, 1),
            (1, NaN, 1),
            (1, 2, NaN),
            (PosInf, 2, 1),
            (1, PosInf, 1),
            (1, 2, PosInf),
            (NegInf, 2, 1),
            (1, NegInf, 1),
            (1, 2, NegInf),
            (0, 1, 1),
        )
        for a, b, c in test_cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    QuadraticEquation.solve(a, b, c)
