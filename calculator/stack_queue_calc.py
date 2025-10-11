import math
import random
from typing import Callable, Dict, List, Union
from calculator.base import CalculatorBase
from calculator.enum.angle import AngleUnit
from calculator.funtions.hyperbolic_functions import HyperbolicFunctions
from calculator.funtions.math_functions import MathFunctions
from calculator.funtions.trigo_function import TrigFunctions
from calculator.util.postfix_converter import PostfixConverter
from calculator.util.postfix_eval import PostfixEvaluator
from calculator.util.tokenizer import Tokenizer


class StackQueueCalculator(CalculatorBase):
    """
    Modular scientific calculator with comprehensive mathematical operations.
    
    Features:
    - Basic arithmetic (+, -, *, /, %, ^)
    - Trigonometric functions with multiple angle units (degrees, radians, gradians, turns)
    - Hyperbolic functions
    - Logarithmic and exponential functions
    - Statistical operations
    - Mathematical constants
    - Memory operations
    - Implicit multiplication
    """
    
    def __init__(self, angle_unit: AngleUnit = AngleUnit.RADIANS):
        super().__init__()
        self.angle_unit = angle_unit
        self._last_answer = 0.0
        self._memory = 0.0
        
        # Initialize modular components
        self.math_funcs = MathFunctions()
        self.trig_funcs = TrigFunctions(angle_unit)
        self.hyp_funcs = HyperbolicFunctions()
        
        self._initialize_functions()
        self._initialize_constants()
        
        # Initialize processing components
        self.tokenizer = Tokenizer(self.functions, self.binary_functions, self.constants)
        self.postfix_converter = PostfixConverter(
            set(self.functions.keys()), 
            set(self.binary_functions.keys())
        )
        self.evaluator = PostfixEvaluator(self.functions, self.binary_functions)
    
    def set_angle_unit(self, unit: AngleUnit) -> None:
        """Change the angle unit for trigonometric functions."""
        self.angle_unit = unit
        self.trig_funcs = TrigFunctions(unit)
        self._initialize_functions()  # Rebuild function registry
    
    def _initialize_functions(self) -> None:
        """Initialize all supported unary functions."""
        self.functions: Dict[str, Callable[[float], float]] = {
            # Basic operations
            'recip': self.math_funcs.safe_reciprocal,
            'sqrt': self.math_funcs.safe_sqrt,
            'cbrt': self.math_funcs.cbrt,
            
            # Exponential and logarithmic
            'e': math.exp,  # e(x) = e^x
            'exp': math.exp,
            'exp10': lambda x: 10 ** x,
            'ln': self.math_funcs.safe_ln,
            'log': self.math_funcs.safe_log10,
            'log2': self.math_funcs.safe_log2,

            # Angle conversion functions
            'rad': math.radians,  # Convert degrees to radians
            'deg': math.degrees,  # Convert radians to degrees

            # Trigonometric
            'sin': self.trig_funcs.sin,
            'cos': self.trig_funcs.cos,
            'tan': self.trig_funcs.tan,
            'csc': self.trig_funcs.csc,
            'sec': self.trig_funcs.sec,
            'cot': self.trig_funcs.cot,
            
            # Inverse trigonometric
            'asin': self.trig_funcs.asin,
            'acos': self.trig_funcs.acos,
            'atan': self.trig_funcs.atan,
            'acsc': self.trig_funcs.acsc,
            'asec': self.trig_funcs.asec,
            'acot': self.trig_funcs.acot,
            
            # Hyperbolic
            'sinh': math.sinh,
            'cosh': math.cosh,
            'tanh': math.tanh,
            'csch': self.hyp_funcs.csch,
            'sech': self.hyp_funcs.sech,
            'coth': self.hyp_funcs.coth,
            
            # Inverse hyperbolic
            'asinh': math.asinh,
            'acosh': self.hyp_funcs.acosh,
            'atanh': self.hyp_funcs.atanh,
            'acsch': self.hyp_funcs.acsch,
            'asech': self.hyp_funcs.asech,
            'acoth': self.hyp_funcs.acoth,
            
            # Utility functions
            'abs': abs,
            'floor': math.floor,
            'ceil': math.ceil,
            'round': round,
            'trunc': math.trunc,
            'sign': self.math_funcs.sign,
            
            # Statistical
            'fact': self.math_funcs.safe_factorial,
            
            # Random
            'rand': lambda x: random.random(),
        }
        
        # Binary functions
        self.binary_functions: Dict[str, Callable[[float, float], float]] = {
            'nPr': self.math_funcs.safe_permutation,
            'nCr': self.math_funcs.safe_combination,
            'logb': self.math_funcs.safe_log_base,
            'nrt': self.math_funcs.safe_nth_root,
            'pow': lambda x, y: x ** y,
            'atan2': self.trig_funcs.atan2,
            'hypot': math.hypot,
            'gcd': self.math_funcs.safe_gcd,
            'lcm': self.math_funcs.safe_lcm,
            'max': max,
            'min': min,
        }
    
    def _initialize_constants(self) -> None:
        """Initialize mathematical constants."""
        self.constants: Dict[str, Union[float, Callable]] = {
            'π': math.pi,
            'pi': math.pi,
            'e': math.e,
            'tau': math.tau,
            'phi': (1 + math.sqrt(5)) / 2,
            'ans': lambda: self._last_answer,
        }
    
    # ==================== Memory Operations ====================
    
    def memory_add(self, value: float) -> None:
        """Add value to memory (M+)."""
        self._memory += value
    
    def memory_subtract(self, value: float) -> None:
        """Subtract value from memory (M-)."""
        self._memory -= value
    
    def memory_recall(self) -> float:
        """Recall memory value (MR)."""
        return self._memory
    
    def memory_clear(self) -> None:
        """Clear memory (MC)."""
        self._memory = 0.0
    
    def get_last_answer(self) -> float:
        """Get the last calculated answer."""
        return self._last_answer
    
    # ==================== Implicit Multiplication ====================
    
    def add_implicit_multiplication(self, tokens: List) -> List:
        """Add implicit multiplication operators."""
        result = []
        all_funcs = set(self.functions.keys()) | set(self.binary_functions.keys())
        
        for i, token in enumerate(tokens):
            result.append(token)
            if i + 1 < len(tokens):
                next_token = tokens[i + 1]
                if self._should_add_multiplication(token, next_token, all_funcs):
                    result.append('*')
        
        return result
    
    def _should_add_multiplication(self, token, next_token, all_funcs: set) -> bool:
        """Determine if implicit multiplication should be added."""
        return (
            (isinstance(token, (int, float)) and next_token == '(') or
            (token == ')' and next_token == '(') or
            (token == ')' and isinstance(next_token, (int, float))) or
            (isinstance(token, (int, float)) and next_token == '~') or
            (isinstance(token, (int, float)) and next_token in all_funcs) or
            (isinstance(token, (int, float)) and next_token in self.constants.keys()) or
            (token == ')' and next_token in all_funcs)
        )
    
    # ==================== Main Evaluation ====================
    
    def evaluate(self, query: str) -> float:
        """
        Main method to evaluate mathematical expression.
        
        Args:
            query: Mathematical expression as string
            
        Returns:
            Result of evaluation
            
        Examples:
            >>> calc = StackQueueCalculator(AngleUnit.DEGREES)
            >>> calc.evaluate("sin(30°)")  # 30 degrees
            0.5
            >>> calc.evaluate("2π")  # 2 * pi
            6.283185307179586
            >>> calc.evaluate("e^2")  # e squared
            7.389056098930650
            >>> calc.evaluate("90grad")  # 90 gradians = 81 degrees
            1.5707963267948966  # in radians
        """
        tokens = self.tokenizer.tokenize(query)
        tokens = self.add_implicit_multiplication(tokens)
        postfix = self.postfix_converter.convert(tokens)
        result = self.evaluator.evaluate(postfix)
        self._last_answer = result
        return result
    
    def evaluate_with_steps(self, query: str) -> Dict[str, any]:
        """
        Evaluate expression and return intermediate steps for debugging.
        
        Returns:
            Dictionary containing tokens, postfix, and result
        """
        tokens = self.tokenizer.tokenize(query)
        tokens_with_mult = self.add_implicit_multiplication(tokens)
        postfix = self.postfix_converter.convert(tokens_with_mult)
        result = self.evaluator.evaluate(postfix)
        self._last_answer = result
        
        return {
            'original': query,
            'tokens': tokens,
            'tokens_with_implicit_mult': tokens_with_mult,
            'postfix': postfix,
            'result': result
        }