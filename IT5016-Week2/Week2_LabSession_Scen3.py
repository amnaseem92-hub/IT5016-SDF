correct_password = "python123"
attempts = 10

while attempts > 0:
    password = input("Enter password: ")
    if password == correct_password:
        print ("Access granted")
        break
    else:
        attempts -= 1
        print("Incorrect! " + str(attempts) + " attempts left.")

if attempts == 0:
  print ("Access denied. Too many failed attempts")