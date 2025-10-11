import math
from calculator.enum.angle import AngleUnit


class TrigFunctions:
    """Trigonometric functions with angle unit support."""
    
    def __init__(self, angle_unit: AngleUnit = AngleUnit.RADIANS):
        self.angle_unit = angle_unit
    
    def _to_radians(self, angle: float) -> float:
        """Convert angle from current unit to radians."""
        if self.angle_unit == AngleUnit.DEGREES:
            return math.radians(angle)
        elif self.angle_unit == AngleUnit.GRADIANS:
            return angle * math.pi / 200
        elif self.angle_unit == AngleUnit.TURNS:
            return angle * 2 * math.pi
        return angle  # Already in radians
    
    def _from_radians(self, angle: float) -> float:
        """Convert angle from radians to current unit."""
        if self.angle_unit == AngleUnit.DEGREES:
            return math.degrees(angle)
        elif self.angle_unit == AngleUnit.GRADIANS:
            return angle * 200 / math.pi
        elif self.angle_unit == AngleUnit.TURNS:
            return angle / (2 * math.pi)
        return angle  # Already in radians
    
    def sin(self, x: float) -> float:
        return math.sin(self._to_radians(x))
    
    def cos(self, x: float) -> float:
        return math.cos(self._to_radians(x))
    
    def tan(self, x: float) -> float:
        return math.tan(self._to_radians(x))
    
    def csc(self, x: float) -> float:
        sin_val = self.sin(x)
        if abs(sin_val) < 1e-10:
            raise ZeroDivisionError(f"csc undefined at x={x}")
        return 1 / sin_val
    
    def sec(self, x: float) -> float:
        cos_val = self.cos(x)
        if abs(cos_val) < 1e-10:
            raise ZeroDivisionError(f"sec undefined at x={x}")
        return 1 / cos_val
    
    def cot(self, x: float) -> float:
        tan_val = self.tan(x)
        if abs(tan_val) < 1e-10:
            raise ZeroDivisionError(f"cot undefined at x={x}")
        return 1 / tan_val
    
    def asin(self, x: float) -> float:
        if abs(x) > 1:
            raise ValueError(f"Domain error: asin({x}) requires -1 ≤ x ≤ 1")
        return self._from_radians(math.asin(x))
    
    def acos(self, x: float) -> float:
        if abs(x) > 1:
            raise ValueError(f"Domain error: acos({x}) requires -1 ≤ x ≤ 1")
        return self._from_radians(math.acos(x))
    
    def atan(self, x: float) -> float:
        return self._from_radians(math.atan(x))
    
    def acsc(self, x: float) -> float:
        if abs(x) < 1:
            raise ValueError(f"Domain error: acsc({x}) requires |x| ≥ 1")
        return self._from_radians(math.asin(1/x))
    
    def asec(self, x: float) -> float:
        if abs(x) < 1:
            raise ValueError(f"Domain error: asec({x}) requires |x| ≥ 1")
        return self._from_radians(math.acos(1/x))
    
    def acot(self, x: float) -> float:
        if x != 0:
            return self._from_radians(math.atan(1/x))
        return self._from_radians(math.pi/2)
    
    def atan2(self, y: float, x: float) -> float:
        return self._from_radians(math.atan2(y, x))
