import math


class HyperbolicFunctions:
    """Hyperbolic functions with error handling."""
    
    @staticmethod
    def csch(x: float) -> float:
        if x == 0:
            raise ZeroDivisionError("csch undefined at x=0")
        return 1 / math.sinh(x)
    
    @staticmethod
    def sech(x: float) -> float:
        return 1 / math.cosh(x)
    
    @staticmethod
    def coth(x: float) -> float:
        if x == 0:
            raise ZeroDivisionError("coth undefined at x=0")
        return 1 / math.tanh(x)
    
    @staticmethod
    def acosh(x: float) -> float:
        if x < 1:
            raise ValueError(f"Domain error: acosh({x}) requires x ≥ 1")
        return math.acosh(x)
    
    @staticmethod
    def atanh(x: float) -> float:
        if abs(x) >= 1:
            raise ValueError(f"Domain error: atanh({x}) requires |x| < 1")
        return math.atanh(x)
    
    @staticmethod
    def asech(x: float) -> float:
        if x <= 0 or x > 1:
            raise ValueError(f"Domain error: asech({x}) requires 0 < x ≤ 1")
        return math.acosh(1/x)
    
    @staticmethod
    def acoth(x: float) -> float:
        if abs(x) <= 1:
            raise ValueError(f"Domain error: acoth({x}) requires |x| > 1")
        return math.atanh(1/x)
    
    @staticmethod
    def acsch(x: float) -> float:
        if x == 0:
            raise ZeroDivisionError("acsch undefined at x=0")
        return math.asinh(1/x)
