import math
from calculator.enum.angle import AngleUnit


class AngleConverter:
    """Utility class for angle unit conversions."""
    
    @staticmethod
    def to_radians(value: float, unit: AngleUnit) -> float:
        if unit == AngleUnit.DEGREES:
            return math.radians(value)
        elif unit == AngleUnit.GRADIANS:
            return value * math.pi / 200
        elif unit == AngleUnit.TURNS:
            return value * 2 * math.pi
        return value
    
    @staticmethod
    def from_radians(value: float, unit: AngleUnit) -> float:
        if unit == AngleUnit.DEGREES:
            return math.degrees(value)
        elif unit == AngleUnit.GRADIANS:
            return value * 200 / math.pi
        elif unit == AngleUnit.TURNS:
            return value / (2 * math.pi)
        return value