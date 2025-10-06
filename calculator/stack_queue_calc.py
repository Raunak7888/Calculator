from collections import deque
from .base import CalculatorBase

class StackQueueCalculator(CalculatorBase):
    def tokenize(self, query: str) -> list:
        """Tokenize the input expression into numbers and operators."""
        if not query or not query.strip():
            raise ValueError("Empty expression")
        
        query = query.replace(' ', '')  # Remove whitespace
        arr = []
        num_str = ""
        i = 0
        
        while i < len(query):
            ch = query[i]

            # Build number (including decimals)
            if ch.isdigit() or ch == '.':
                num_str += ch
                i += 1
                continue

            # Flush pending number before processing operator
            if num_str:
                try:
                    arr.append(float(num_str))
                except ValueError:
                    raise ValueError(f"Invalid number format: {num_str}")
                num_str = ""

            # Handle unary minus (negative numbers)
            if ch == '-':
                # Check if this is a unary minus
                is_unary = (
                    i == 0 or  # Start of expression
                    (arr and arr[-1] in ['(', '+', '-', '*', '/', '%', '^'])  # After operator
                )
                
                if is_unary:
                    # Look ahead to get the number or sub-expression
                    i += 1
                    # Skip whitespace if any
                    while i < len(query) and query[i] == ' ':
                        i += 1
                    
                    if i >= len(query):
                        raise ValueError("Expression ends with operator")
                    
                    # If next is '(', we need to handle it specially
                    if query[i] == '(':
                        arr.append('~')  # Unary minus marker
                        continue
                    
                    # Otherwise, collect the negative number
                    neg_num = ""
                    while i < len(query) and (query[i].isdigit() or query[i] == '.'):
                        neg_num += query[i]
                        i += 1
                    
                    if neg_num:
                        try:
                            arr.append(-float(neg_num))
                        except ValueError:
                            raise ValueError(f"Invalid number format: -{neg_num}")
                    else:
                        raise ValueError("Invalid expression: operator followed by operator")
                    continue
                else:
                    # Binary minus
                    arr.append('-')
                    i += 1
                    continue

            # Handle other operators and parentheses
            if ch in '+*/%^()':
                arr.append(ch)
                i += 1
            else:
                raise ValueError(f"Invalid character: {ch}")

        # Flush final number
        if num_str:
            try:
                arr.append(float(num_str))
            except ValueError:
                raise ValueError(f"Invalid number format: {num_str}")

        return arr

    def add_implicit_multiplication(self, tokens: list) -> list:
        """Add implicit multiplication operators (e.g., 2(3) -> 2*3)."""
        result = []
        for i, token in enumerate(tokens):
            result.append(token)
            if i + 1 < len(tokens):
                next_token = tokens[i + 1]
                # Add * between: number and (, ) and (, ) and number
                if (isinstance(token, (int, float)) and next_token == '(') or \
                   (token == ')' and next_token == '(') or \
                   (token == ')' and isinstance(next_token, (int, float))) or \
                   (isinstance(token, (int, float)) and next_token == '~'):
                    result.append('*')
        return result

    def token_to_postfix(self, tokens: list) -> list:
        """Convert infix notation to postfix (RPN) using Shunting Yard algorithm."""
        if not tokens:
            raise ValueError("No tokens to convert")
        
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3, '~': 4}  # ~ is unary minus
        right_assoc = {'^', '~'}  # Right-associative operators
        stack = []
        queue = deque()

        for t in tokens:
            if isinstance(t, (int, float)):
                queue.append(t)
            elif t == '(':
                stack.append(t)
            elif t == ')':
                # Pop until matching open parenthesis
                while stack and stack[-1] != '(':
                    queue.append(stack.pop())
                if not stack:
                    raise ValueError("Mismatched parentheses: extra ')'")
                stack.pop()  # Remove the '('
            elif t == '~' or t in precedence:
                # Pop operators with higher or equal precedence (considering associativity)
                while stack and stack[-1] != '(' and stack[-1] in precedence:
                    if (t not in right_assoc and precedence[stack[-1]] >= precedence[t]) or \
                       (t in right_assoc and precedence[stack[-1]] > precedence[t]):
                        queue.append(stack.pop())
                    else:
                        break
                stack.append(t)
            else:
                raise ValueError(f"Invalid token: {t}")
        
        # Pop remaining operators
        while stack:
            if stack[-1] == '(':
                raise ValueError("Mismatched parentheses: extra '('")
            queue.append(stack.pop())
        
        return list(queue)

    def calc(self, num1: float, num2: float, op: str) -> float:
        """Perform binary operation."""
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

    def evaluation(self, postfix: list) -> float:
        """Evaluate postfix expression."""
        if not postfix:
            raise ValueError("Empty postfix expression")
        
        stack = []
        
        for p in postfix:
            if isinstance(p, (int, float)):
                stack.append(p)
            elif p == '~':  # Unary minus
                if len(stack) < 1:
                    raise ValueError("Insufficient operands for unary minus")
                stack.append(-stack.pop())
            elif p in "+-*/%^":
                if len(stack) < 2:
                    raise ValueError(f"Insufficient operands for operator '{p}'")
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.calc(num1, num2, p))
            else:
                raise ValueError(f"Invalid token in postfix: {p}")
        
        if len(stack) != 1:
            raise ValueError("Invalid expression: too many operands")
        
        return stack[0]

    def evaluate(self, query: str) -> float:
        """Main method to evaluate mathematical expression."""
        tokens = self.tokenize(query)
        tokens = self.add_implicit_multiplication(tokens)
        postfix = self.token_to_postfix(tokens)
        return self.evaluation(postfix)