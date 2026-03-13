#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of n using an iterative approach.
    """
    if n < 0:
        return "Error: Negative numbers do not have factorials."
    
    result = 1
    # The original code was missing 'n -= 1', causing an infinite loop.
    # We decrement n in each iteration until it reaches 1.
    while n > 1:
        result *= n
        n -= 1
    return result

def main():
    # Check if an argument was provided
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <number>")
        sys.exit(1)

    try:
        # Convert argument to integer and calculate factorial
        num = int(sys.argv[1])
        f = factorial(num)
        print(f)
    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)

if __name__ == "__main__":
    main()
