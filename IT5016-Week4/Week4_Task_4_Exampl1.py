# Task 4 - Example 1: Functions where one function calls another to take the result and do further processing

def add(a, b):
    return a + b

def multiply(x, y):
    return x * y

def add_and_multiply(a, b, c):
    sum_result = add(a, b)              # Call the add function
    product_result = multiply(sum_result, c)  # Call the multiply function
    return product_result

# Example run
result = add_and_multiply(2, 3, 4)
print(result)   # Output: 20


