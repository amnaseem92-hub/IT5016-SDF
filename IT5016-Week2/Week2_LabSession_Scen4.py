age = int(input("Enter your age: "))
if age >= 18 and age < 65:
        print("you are eligible to vote.") 
elif age < 0:       
        print("please enter age greter than 0.") 
elif age  >= 65:       
        print("you are a senior citizen.")      
else:        
        print("you are not eligible to vote.")