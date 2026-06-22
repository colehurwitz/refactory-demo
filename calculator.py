#!/usr/bin/env python3
"""A simple calculator CLI - missing multiply, divide, and error handling."""

import sys


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    """Raise a to the power of b."""
    return a ** b


def modulo(a: float, b: float) -> float:
    """Return a modulo b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def main():
    """Main entry point."""
    if len(sys.argv) < 4:
        print("Usage: calculator.py <operation> <num1> <num2>")
        print("Operations: add, subtract, multiply, divide, power, modulo")
        sys.exit(1)

    operation = sys.argv[1]
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: Arguments must be numeric")
        sys.exit(1)

    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation == "modulo":
            result = modulo(num1, num2)
        else:
            print(f"Unknown operation: {operation}")
            sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
