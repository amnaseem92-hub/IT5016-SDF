score = int(input("Enter a score: "))
if score >= 90:
  print ("Grade A")
  print ("Excellent")
elif score >= 80:
  print ("Grade B")
  print ("Good")  
elif score >= 70:
  print ("Grade C")
  print ("Satisfactory")
elif score > 100:
  print ("Please  enter a number less than or equal 100")
elif score < 0:
  print ("Please  enter a number greater than or equal 0")
else:
  print("Grade :F")
  print("Fail ")
  