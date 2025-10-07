# Infix → Postfix Converter

A small utility that converts infix arithmetic/identifier expressions to postfix (RPN).

## Features

- Supports numbers (integers and floats) and identifiers (letters, digits, underscore)  
- Operators supported: `+`, `-`, `*`, `/`, `^`  
- Parentheses: `(` and `)`  
- `^` is treated as **right-associative**, other operators are left-associative  

## Examples

a + b * c -> a b c * +
(a + b) * c -> a b + c *
3 + 4 * 2 / (1 - 5) ^ 2 ^ 3 -> 3 4 2 * 1 5 - 2 3 ^ ^ / +
x ^ y ^ z -> x y z ^ ^
12 + 34 * var_1 -> 12 34 var_1 * +