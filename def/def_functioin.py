print('Welcome to rollercoaster!')
height = int(input("Whats is your height? "))
#age = int(input("What is your age? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("Enter your age: "))
  
bill = 0
if age < 12:
  bill = 5
  print("Please pay $5.")
elif age <= 18:
  bill = 7
  print('Please pay $7.')
elif age >= 18:
  bill = 12
  print("Please pay $12.")
elif age >= 45 and age <= 55:
  print(f"Everything is going to be ok. Have a free ride on us!")
else:
  print("sorry, you have to grow taller.")