import sys
import unittest
import math

EPSILON = sys.float_info.epsilon
NaN = float("NaN")
PosInf = float("+inf")
NegInf = float("-inf")

class QuadraticEquation:
    @staticmethod
    def descriminant(a: float, b: float, c: float) -> float:
        return float((b*b)-(4*a*c))

    @staticmethod
    def solve(a: float, b: float, c: float, e: float = EPSILON) -> list[float]:
        if a == 0:
            raise ValueError("Invalid a coef")
        if not all(math.isfinite(coef) for coef in [a, b, c]):
            raise ValueError("Invalid coef")
        descriminant = QuadraticEquation.descriminant(a, b, c)
        if descriminant < -e:
            return []
        if abs(descriminant) <= e:
            return [-(b/2*a), -(b/2*a)]
        if descriminant > e:
            return [(-b + (math.sqrt(descriminant)) / 2*a), (-b - math.sqrt(descriminant)) / 2*a]


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
