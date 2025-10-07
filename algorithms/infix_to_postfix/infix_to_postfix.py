#!/usr/bin/env python3
"""
Simple infix -> postfix (Reverse Polish Notation) converter.

Supports:
- multi-digit integers and floats
- multi-letter identifiers (variables)
- operators: + - * / ^
- parentheses: ( )
- '^' is right-associative; others are left-associative

Usage:
  python infix_to_postfix.py
  (then type an expression, e.g. "3 + 4 * 2 / (1 - 5) ^ 2 ^ 3")
"""
import re

TOKEN_RE = re.compile(r'\d+\.\d+|\d+|[A-Za-z_]\w*|[+\-*/^()]')

PREC = {
    '^': 4,
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
}

RIGHT_ASSOC = {'^'}

def tokenize(expr: str):
    return TOKEN_RE.findall(expr)

def is_operand(token: str) -> bool:
    return re.fullmatch(r'\d+\.\d+|\d+|[A-Za-z_]\w*', token) is not None

def infix_to_postfix(expr: str) -> str:
    tokens = tokenize(expr)
    output = []
    stack = []

    for tok in tokens:
        if is_operand(tok):
            output.append(tok)
        elif tok == '(':
            stack.append(tok)
        elif tok == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack or stack[-1] != '(':
                raise ValueError("Mismatched parentheses")
            stack.pop()
        else:
            while stack and stack[-1] != '(':
                top = stack[-1]
                ptop = PREC.get(top, 0)
                pcur = PREC.get(tok, 0)
                if (ptop > pcur) or (ptop == pcur and tok not in RIGHT_ASSOC):
                    output.append(stack.pop())
                else:
                    break
            stack.append(tok)

    while stack:
        top = stack.pop()
        if top in '()':
            raise ValueError("Mismatched parentheses")
        output.append(top)

    return ' '.join(output)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        expr = ' '.join(sys.argv[1:])
        print(infix_to_postfix(expr))
    else:
        try:
            expr = input("Enter infix expression: ").strip()
            if not expr:
                print("No input provided.")
            else:
                print(infix_to_postfix(expr))
        except Exception as e:
            print("Error:", e)
