import sys
import math

EPSILON = sys.float_info.epsilon
NaN = float("NaN")
PosInf = float("+inf")
NegInf = float("-inf")


class QuadraticEquation:
    @staticmethod
    def descriminant(a: float, b: float, c: float) -> float:
        return float((b * b) - (4 * a * c))

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
            return [-(b / 2 * a), -(b / 2 * a)]
        if descriminant > e:
            return [
                (-b + (math.sqrt(descriminant)) / 2 * a),
                (-b - math.sqrt(descriminant)) / 2 * a,
            ]
