import math
from typing import Dict, List, Optional, Union


class Tokenizer:
    """Handles tokenization of mathematical expressions."""
    
    def __init__(self, functions: Dict, binary_functions: Dict, constants: Dict):
        self.functions = functions
        self.binary_functions = binary_functions
        self.constants = constants
    
    def tokenize(self, query: str) -> List[Union[float, str]]:
        if not query or not query.strip():
            raise ValueError("Empty expression")

        query = query.replace(' ', '')
        tokens = []
        i = 0
        num_str = ""
        pending_close = 0  # Track how many closing parens we need to add

        while i < len(query):
            ch = query[i]

            # Handle angle unit suffixes (°, rad, grad, turn)
            if ch == '°' or query[i:i+3] == 'rad' or query[i:i+4] in ['grad', 'turn']:
                angle_info = self._handle_angle_unit(query, i, num_str)
                if angle_info:
                    i, num_str, angle_token = angle_info
                    tokens.append(angle_token)
                    continue

            # Build number (including decimals and scientific notation)
            if ch.isdigit() or ch == '.':
                num_str += ch
                i += 1
                continue

            # Scientific notation (e.g., 1e-5, 2.5E+3)
            if ch in 'eE' and num_str and i + 1 < len(query):
                next_ch = query[i + 1]
                if next_ch in '+-' or next_ch.isdigit():
                    num_str += ch
                    i += 1
                    continue

            # Check for constants
            constant_result = self._try_parse_constant(query, i, tokens, num_str)
            if constant_result is not None:
                i, num_str = constant_result
                # If we had a pending close and just processed a constant, close it
                if pending_close > 0:
                    tokens.append(')')
                    pending_close -= 1
                continue

            # Check for binary functions
            binary_result = self._try_parse_binary_function(query, i, tokens, num_str)
            if binary_result is not None:
                i, num_str = binary_result
                continue

            # Check for unary functions
            func_result = self._try_parse_function(query, i, tokens, num_str)
            if func_result is not None:
                i, num_str = func_result
                continue

            # Flush pending number
            if num_str:
                tokens.append(self._parse_float(num_str))
                num_str = ""

            # Handle unary minus
            if ch == '-' and self._is_unary_minus(i, tokens):
                result = self._handle_unary_minus(query, i, tokens)
                i, num_str = result[0], result[1]
                if num_str == "pending_close":
                    pending_close += 1
                    num_str = ""
                continue

            # Handle closing parenthesis - check if we need to add our pending close
            if ch == ')' and pending_close > 0:
                # This closes the function call, now add our pending close
                tokens.append(ch)
                i += 1
                tokens.append(')')
                pending_close -= 1
                continue

            # Handle operators and parentheses
            if ch in '+-*/%^(),':
                tokens.append(ch)
                i += 1
            else:
                raise ValueError(f"Invalid character: '{ch}'")

        # Flush final number
        if num_str:
            tokens.append(self._parse_float(num_str))

        # Close any remaining pending parentheses
        while pending_close > 0:
            tokens.append(')')
            pending_close -= 1

        return tokens
    
    def _handle_angle_unit(self, query: str, i: int, num_str: str) -> Optional[tuple]:
        """Handle angle unit suffixes and convert to radians."""
        if not num_str:
            return None
        
        value = self._parse_float(num_str)
        
        if query[i] == '°':
            # Degrees
            radians = math.radians(value)
            return (i + 1, "", radians)
        elif query[i:i+3] == 'rad':
            # Radians (no conversion needed)
            return (i + 3, "", value)
        elif query[i:i+4] == 'grad':
            # Gradians
            radians = value * math.pi / 200
            return (i + 4, "", radians)
        elif query[i:i+4] == 'turn':
            # Turns
            radians = value * 2 * math.pi
            return (i + 4, "", radians)
        
        return None
    
    def _try_parse_constant(self, query: str, i: int, tokens: List, num_str: str) -> Optional[tuple]:
        for const_name, const_value in self.constants.items():
            if query[i:i+len(const_name)] == const_name:
                # Check if this constant name is followed by '(' - if so, it's a function, not a constant
                next_idx = i + len(const_name)
                if next_idx < len(query) and query[next_idx] == '(':
                    continue  # Skip this constant, let function parser handle it

                if num_str:
                    tokens.append(self._parse_float(num_str))
                if callable(const_value):
                    tokens.append(const_value())
                else:
                    tokens.append(const_value)
                return (i + len(const_name), "")
        return None
    
    def _try_parse_binary_function(self, query: str, i: int, tokens: List, num_str: str) -> Optional[tuple]:
        for func_name in self.binary_functions.keys():
            if query[i:i+len(func_name)+1] == f'{func_name}(':
                if num_str:
                    tokens.append(self._parse_float(num_str))
                tokens.append(func_name)
                tokens.append('(')
                return (i + len(func_name) + 1, "")
        return None
    
    def _try_parse_function(self, query: str, i: int, tokens: List, num_str: str) -> Optional[tuple]:
        for func_name in self.functions.keys():
            if query[i:i+len(func_name)+1] == f'{func_name}(':
                if num_str:
                    tokens.append(self._parse_float(num_str))
                tokens.append(func_name)
                tokens.append('(')
                return (i + len(func_name) + 1, "")
        return None
    
    def _is_unary_minus(self, i: int, tokens: List) -> bool:
        return (i == 0 or
                (tokens and tokens[-1] in ['(', '+', '-', '*', '/', '%', '^', ',', '~']))
    
    def _handle_unary_minus(self, query: str, i: int, tokens: List) -> tuple:
        i += 1
        while i < len(query) and query[i] == ' ':
            i += 1

        if i >= len(query):
            raise ValueError("Expression ends with operator")

        # Handle consecutive unary minuses
        if query[i] == '-':
            tokens.append('~')
            return (i, "")

        all_names = (list(self.functions.keys()) +
                    list(self.binary_functions.keys()) +
                    list(self.constants.keys()))

        # Check if followed by a function or constant
        for name in all_names:
            if query.startswith(name, i):
                # For -func(...), transform to (0-func(...))
                tokens.append('(')
                tokens.append(0.0)
                tokens.append('-')
                return (i, "pending_close")

        if query[i] == '(':
            tokens.append('~')
            return (i, "")

        neg_num = ""
        while i < len(query) and (query[i].isdigit() or query[i] == '.'):
            neg_num += query[i]
            i += 1

        if neg_num:
            # Check for scientific notation
            if i < len(query) and query[i] in 'eE':
                next_idx = i + 1
                if next_idx < len(query) and query[next_idx] in '+-':
                    neg_num += query[i:next_idx+1]
                    i = next_idx + 1
                    while i < len(query) and query[i].isdigit():
                        neg_num += query[i]
                        i += 1
                elif next_idx < len(query) and query[next_idx].isdigit():
                    neg_num += query[i]
                    i += 1
                    while i < len(query) and query[i].isdigit():
                        neg_num += query[i]
                        i += 1
            tokens.append(-self._parse_float(neg_num))
            return (i, "")
        else:
            raise ValueError("Invalid expression: operator followed by operator")
    
    def _parse_float(self, num_str: str) -> float:
        try:
            return float(num_str)
        except ValueError:
            raise ValueError(f"Invalid number format: {num_str}")
