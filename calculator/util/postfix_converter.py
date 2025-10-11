from collections import deque
from typing import Dict, List


class PostfixConverter:
    """Converts infix notation to postfix (RPN) using Shunting Yard algorithm."""
    
    def __init__(self, functions: set, binary_functions: set):
        self.functions = functions
        self.binary_functions = binary_functions
        self.precedence = self._build_precedence()
        self.right_assoc = self._build_right_assoc()
    
    def _build_precedence(self) -> Dict[str, int]:
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3, '~': 5}
        for func in self.functions | self.binary_functions:
            precedence[func] = 4
        return precedence
    
    def _build_right_assoc(self) -> set:
        return {'^', '~'} | self.functions | self.binary_functions
    
    def convert(self, tokens: List) -> List:
        if not tokens:
            raise ValueError("No tokens to convert")
        
        stack = []
        queue = deque()
        
        for t in tokens:
            if isinstance(t, (int, float)):
                queue.append(t)
            elif t == '(':
                stack.append(t)
            elif t == ')':
                self._handle_closing_paren(stack, queue)
            elif t == ',':
                self._handle_comma(stack, queue)
            elif t in self.precedence:
                self._handle_operator(t, stack, queue)
            else:
                raise ValueError(f"Invalid token: {t}")
        
        while stack:
            if stack[-1] in '(,':
                raise ValueError("Mismatched parentheses or commas")
            queue.append(stack.pop())
        
        return list(queue)
    
    def _handle_closing_paren(self, stack: List, queue: deque) -> None:
        while stack and stack[-1] not in '(,':
            queue.append(stack.pop())
        if not stack or stack[-1] != '(':
            raise ValueError("Mismatched parentheses: extra ')'")
        stack.pop()
        if stack and (stack[-1] in self.functions or stack[-1] in self.binary_functions):
            queue.append(stack.pop())
    
    def _handle_comma(self, stack: List, queue: deque) -> None:
        while stack and stack[-1] not in '(,':
            queue.append(stack.pop())
        if not stack:
            raise ValueError("Comma outside of function call")
    
    def _handle_operator(self, t: str, stack: List, queue: deque) -> None:
        while stack and stack[-1] not in '(,' and stack[-1] in self.precedence:
            if ((t not in self.right_assoc and self.precedence[stack[-1]] >= self.precedence[t]) or
                (t in self.right_assoc and self.precedence[stack[-1]] > self.precedence[t])):
                queue.append(stack.pop())
            else:
                break
        stack.append(t)