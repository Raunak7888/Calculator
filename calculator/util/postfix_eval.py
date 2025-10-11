from typing import Dict, List


class PostfixEvaluator:
    """Evaluates postfix expressions."""
    
    def __init__(self, functions: Dict, binary_functions: Dict):
        self.functions = functions
        self.binary_functions = binary_functions
    
    def evaluate(self, postfix: List) -> float:
        if not postfix:
            raise ValueError("Empty postfix expression")
        
        stack = []
        
        for token in postfix:
            if isinstance(token, (int, float)):
                stack.append(token)
            elif token == '~':
                if len(stack) < 1:
                    raise ValueError("Insufficient operands for unary minus")
                stack.append(-stack.pop())
            elif token in self.functions:
                if len(stack) < 1:
                    raise ValueError(f"Insufficient operands for function '{token}'")
                val = stack.pop()
                stack.append(self.functions[token](val))
            elif token in self.binary_functions:
                if len(stack) < 2:
                    raise ValueError(f"Insufficient operands for function '{token}'")
                arg2 = stack.pop()
                arg1 = stack.pop()
                stack.append(self.binary_functions[token](arg1, arg2))
            elif token in "+-*/%^":
                if len(stack) < 2:
                    raise ValueError(f"Insufficient operands for operator '{token}'")
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self._calc(num1, num2, token))
            else:
                raise ValueError(f"Invalid token in postfix: {token}")
        
        if len(stack) != 1:
            raise ValueError("Invalid expression: too many operands")
        
        return stack[0]
    
    def _calc(self, num1: float, num2: float, op: str) -> float:
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return num1 / num2
        elif op == '%':
            if num2 == 0:
                raise ZeroDivisionError("Cannot modulo by zero")
            return num1 % num2
        elif op == '^':
            return num1 ** num2
        else:
            raise ValueError(f"Unknown operator: {op}")
