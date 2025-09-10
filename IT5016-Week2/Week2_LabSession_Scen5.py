
temperature = float(input("Enter temerature in Fahrenheit"))

celsius = (temperature -32) * 5/9

#Celsius
if temperature > 50 or temperature < -30:
    print("It, is too extreme.") 
elif temperature > 30:
    print("It, is a hot day.")
elif temperature >= 20:
    print("It, is a warm day.")
else:
    print("It, is a cold day.")