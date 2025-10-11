from enum import Enum


class AngleUnit(Enum):
    """Supported angle units for trigonometric functions."""
    RADIANS = "rad"
    DEGREES = "deg"
    GRADIANS = "grad"
    TURNS = "turn"