class CalculatorBase:
    def evaluate(self, expression: str) -> float:
        """Evaluate a mathematical expression and return the result."""
        raise NotImplementedError("Subclasses must implement evaluate()")
