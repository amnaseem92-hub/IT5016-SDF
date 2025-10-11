# Activity 7: Reusable Functions in a Simple Calculator Program / Combining functions into a real program

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers, with zero check."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Main program
print("--------- Calculator ----------")
print("Select option:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter option (1,2,3, or 4) to proceed: ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice selected. Please choose a number between 1 to 4.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
