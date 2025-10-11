# Activity 6: Small Problem-Solving Functions / Logical functions (even check, factorial)

def is_even(n):
    """Return True if number is even"""
    return n % 2 == 0

def find_max(a, b, c):
    """Return the largest of 3 numbers."""
    return max(a, b, c)

def factorial(n):
    """Returns the factorial of a number using a loop."""
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# Test the functions
print("Check 5 is even?", is_even(5))
print("Check 8 is even?", is_even(8))
print("Largest from 14, 99, 22:", find_max(4, 9, 2))
print("Factorial of 4 is:", factorial(4))