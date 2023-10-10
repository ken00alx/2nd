a, b = 0, 1
while a < 20:
  print (a)
  a, b = b, a + b


def greet_user(name, last_name):
  print(f'Hi {name} {last_name}!')
  print('Welcome aboard')

print('Start')
greet_user("Johnny", 'Weal')
greet_user("Juliana", 'Stephen')
print('Finish')

def square(number):
  return number * number

print(square(3)) 

import random
roll_dice =['3, 4', '3, 5', '2, 1', '6, 6']
members = ['john', 'mike', 'mary', 'silas']
dice_rolls = random.choice(roll_dice)
leader = random.choice(members)
print(leader)
print(dice_rolls)