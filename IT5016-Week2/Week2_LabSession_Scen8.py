balance = 500
mypin = 1234
pin = int(input("Enter pin number : "))

if mypin != pin:
     print("you entered worng pin.")
else:
    withdraw_amount = int(input("Enter withdraw1 amount: "))
    if withdraw_amount > balance:
        print("Insufficient funds !.")    
    elif withdraw_amount % 10 != 0:
        print("You can only enter multiples of 10.")
    else:
        balance -=   withdraw_amount   
        print(f"Withdraw successfull. Your Remainig balnce: {balance}") 