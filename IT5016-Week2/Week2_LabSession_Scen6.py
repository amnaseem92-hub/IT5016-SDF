import time

correct_password = "python123"
attempts = 10
counter = 0

while attempts > 0:
    password = input("Entre password:")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        counter = counter + 1
        attempts -=1
        print(f"Incorrect password! {attempts} attempts left.")

        if counter == 3:
            print("You are locked out for 10 seconds! Please wait...")
            time.sleep(10) #locked out for 10 seconds


if attempts == 0 :     
   print("Access denied. Too many failed attempts.") 
       
