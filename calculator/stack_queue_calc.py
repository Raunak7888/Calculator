from collections import deque
from .base import CalculatorBase

class StackQueueCalculator(CalculatorBase):
    def tokenize(self, query: str) -> list:
        arr = []
        num_str = ""
        i = 0
        while i < len(query):
            ch = query[i]
            if ch.isdigit():
                num_str += ch
            elif ch == " ":
                i += 1
                continue
            elif ch == '-':
                is_unary = False
                if i == 0: 
                    is_unary = True
                elif i > 0 and arr and arr[-1] in ['(', '+', '-', '*', '/','%']:
                    is_unary = True
                
                if is_unary and not num_str:
                    num_str += ch
                else:
                    if num_str:
                        arr.append(int(num_str))
                        num_str = ""
                    arr.append(ch)
            else:
                if num_str:
                    arr.append(int(num_str))
                    num_str = ""
                arr.append(ch)
            i += 1
        
        if num_str:
            arr.append(int(num_str))
        
        return arr

    def add_implicit_multiplication(self, tokens: list) -> list:
        result = []
        for i, token in enumerate(tokens):
            result.append(token)
            if i + 1 < len(tokens):
                next_token = tokens[i + 1]
                if (isinstance(token, int) and next_token == '(') or (token == ')' and next_token == '(') or (token == ')' and isinstance(next_token, int)):
                    result.append('*')
        return result

    def token_to_postfix(self, token: list) -> list:
        precedence = {'+':1,'-':1,'*':2,'/':2,'%':2,'(':0}
        stack = []
        queue = deque()
        for t in token:
            if isinstance(t, (int, float)):
                queue.append(t)
            else:
                if t == '(':
                    stack.append(t)
                elif t == ')':
                    while stack and stack[-1] != '(':
                        queue.append(stack.pop())
                    if stack and stack[-1] == '(':
                        stack.pop()
                else:
                    while stack and stack[-1] != '(' and precedence.get(stack[-1],0) >= precedence.get(t,0):
                        queue.append(stack.pop())
                    stack.append(t)
        while stack:
            queue.append(stack.pop())
        return list(queue)

    def calc(self, num1: float, num2: float, op: str) -> float:
        if op == '+': return num1 + num2
        if op == '-': return num1 - num2
        if op == '*': return num1 * num2
        if op == '/':
          if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
          return num1 / num2
        if op == '%':
          if num2 == 0:
            raise ZeroDivisionError("Cannot modulo by zero")
          return num1%num2
        raise ValueError(f"Unknown operator: {op}")

    def evaluation(self, postfix: list) -> float:
        stack = []
        for p in postfix:
            if isinstance(p, (int, float)):
                stack.append(p)
            elif p in "+-*/%":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.calc(num1, num2, p))
            else:
                raise ValueError(f"Unknown operator: {p}")
        return stack[-1]

    def evaluate(self, query: str) -> float:
        t = self.tokenize(query)
        t = self.add_implicit_multiplication(t)
        p = self.token_to_postfix(t)
        return self.evaluation(p)
