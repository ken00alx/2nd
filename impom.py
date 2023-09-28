import random

class Dice:
  def roll(self):
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    return first, second

dice = Dice()
print(dice.roll())

for i in range (1, 11):
  if i % 2 != 0:
    print(f'range of i is {i}')