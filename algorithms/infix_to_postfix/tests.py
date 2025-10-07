from infix_to_postfix import infix_to_postfix

# Dictionary of test cases: key = infix expression, value = expected postfix
test_cases = {
    "a + b * c": "a b c * +",
    "(a + b) * c": "a b + c *",
    "3 + 4 * 2 / (1 - 5) ^ 2 ^ 3": "3 4 2 * 1 5 - 2 3 ^ ^ / +",
    "x ^ y ^ z": "x y z ^ ^",
    "12 + 34 * var_1": "12 34 var_1 * +",
}

# Run tests
for infix, expected in test_cases.items():
    result = infix_to_postfix(infix)
    assert result == expected, f"Test failed: {infix!r} -> {result!r}, expected {expected!r}"

print("All tests passed successfully!")
