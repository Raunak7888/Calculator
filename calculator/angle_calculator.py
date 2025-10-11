from calculator.enum.angle import AngleUnit
from calculator.stack_queue_calc import StackQueueCalculator


def create_calculator(angle_unit: str = "radians") -> StackQueueCalculator:
    """
    Factory function to create a calculator with specified angle unit.
    
    Args:
        angle_unit: One of "radians", "degrees", "gradians", "turns"
        
    Returns:
        Configured StackQueueCalculator instance
    """
    unit_map = {
        "radians": AngleUnit.RADIANS,
        "rad": AngleUnit.RADIANS,
        "degrees": AngleUnit.DEGREES,
        "deg": AngleUnit.DEGREES,
        "gradians": AngleUnit.GRADIANS,
        "grad": AngleUnit.GRADIANS,
        "turns": AngleUnit.TURNS,
        "turn": AngleUnit.TURNS,
    }
    
    unit = unit_map.get(angle_unit.lower(), AngleUnit.RADIANS)
    return StackQueueCalculator(unit)

