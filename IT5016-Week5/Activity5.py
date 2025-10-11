# Activity 5: Default Arguments / Optional parameters

def power(number, exponent=2):
    """power of number."""
    return number ** exponent

# Test with and without giving exponent
print("square of number 7 is:", power(7))
print("power 3 of a number 5:", power(5, 3))
print("power 4 of a number 3:", power(3, 4))