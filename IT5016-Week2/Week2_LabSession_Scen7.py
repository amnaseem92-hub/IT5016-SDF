number = int(input("Enter a positive number: "))

while number < 0:
    number = int(input("Enter a positive number: "))

if number % 2 == 0 and number % 5 == 0:
    print("The number is even and divisible by 5.")
else:
    print("Condition not fulfilled")