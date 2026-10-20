"""RPN calculation logic, independent of the graphical interface."""


def evaluate_rpn(expression: str) -> int:
    """Evaluate an integer RPN expression; division truncates toward zero."""
    notation = expression.split()
    stack = []

    for item in notation:
        if item in "+-*/":
            if len(stack) < 2:
                raise ValueError("Missing numbers")
            b = stack.pop()
            a = stack.pop()
            if item == "+":
                stack.append(a + b)
            elif item == "-":
                stack.append(a - b)
            elif item == "*":
                stack.append(a * b)
            elif item == "/":
                stack.append(int(a / b))
        else:
            try:
                stack.append(int(item))
            except ValueError:
                raise ValueError(f"Invalid token {item}")

    if len(stack) != 1:
        raise ValueError("Too many numbers")

    return stack[0]
