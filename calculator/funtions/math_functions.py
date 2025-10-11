import math


class MathFunctions:
    """Repository of mathematical functions with error handling."""
    
    @staticmethod
    def safe_reciprocal(x: float) -> float:
        if x == 0:
            raise ZeroDivisionError("Cannot take reciprocal of zero")
        return 1 / x
    
    @staticmethod
    def safe_sqrt(x: float) -> float:
        if x < 0:
            raise ValueError(f"Domain error: sqrt({x}) is undefined for real numbers")
        return math.sqrt(x)
    
    @staticmethod
    def cbrt(x: float) -> float:
        """Cube root that handles negative values."""
        return math.copysign(abs(x) ** (1/3), x)
    
    @staticmethod
    def safe_ln(x: float) -> float:
        if x <= 0:
            raise ValueError(f"Domain error: ln({x}) is undefined")
        return math.log(x)
    
    @staticmethod
    def safe_log10(x: float) -> float:
        if x <= 0:
            raise ValueError(f"Domain error: log({x}) is undefined")
        return math.log10(x)
    
    @staticmethod
    def safe_log2(x: float) -> float:
        if x <= 0:
            raise ValueError(f"Domain error: log2({x}) is undefined")
        return math.log2(x)
    
    @staticmethod
    def safe_log_base(x: float, base: float) -> float:
        if x <= 0:
            raise ValueError(f"Domain error: log_base({x}) is undefined")
        if base <= 0 or base == 1:
            raise ValueError(f"Invalid logarithm base: {base}")
        return math.log(x) / math.log(base)
    
    @staticmethod
    def safe_nth_root(x: float, n: float) -> float:
        if n == 0:
            raise ValueError("Cannot take 0th root")
        if x < 0 and int(n) == n and int(n) % 2 == 0:
            raise ValueError(f"Domain error: even root of negative number")
        return math.copysign(abs(x) ** (1/n), x) if x < 0 else x ** (1/n)
    
    @staticmethod
    def safe_factorial(x: float) -> float:
        if x < 0:
            raise ValueError(f"Factorial undefined for negative numbers: {x}")
        if x != int(x):
            raise ValueError(f"Factorial requires integer input: {x}")
        if x > 170:
            raise ValueError(f"Factorial overflow: {x}! is too large")
        return float(math.factorial(int(x)))
    
    @staticmethod
    def safe_permutation(n: float, r: float) -> float:
        if n != int(n) or r != int(r):
            raise ValueError("Permutation requires integer inputs")
        if n < 0 or r < 0:
            raise ValueError("Permutation requires non-negative integers")
        if r > n:
            raise ValueError(f"Invalid permutation: r ({r}) cannot exceed n ({n})")
        return float(math.perm(int(n), int(r)))
    
    @staticmethod
    def safe_combination(n: float, r: float) -> float:
        if n != int(n) or r != int(r):
            raise ValueError("Combination requires integer inputs")
        if n < 0 or r < 0:
            raise ValueError("Combination requires non-negative integers")
        if r > n:
            raise ValueError(f"Invalid combination: r ({r}) cannot exceed n ({n})")
        return float(math.comb(int(n), int(r)))
    
    @staticmethod
    def sign(x: float) -> float:
        return 0.0 if x == 0 else math.copysign(1, x)
    
    @staticmethod
    def safe_gcd(x: float, y: float) -> float:
        return float(math.gcd(int(round(x)), int(round(y))))
    
    @staticmethod
    def safe_lcm(x: float, y: float) -> float:
        if x == 0 or y == 0:
            return 0.0
        return abs(x * y) / math.gcd(int(round(x)), int(round(y)))

