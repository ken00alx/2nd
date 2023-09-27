""" sum = lambda x, y: x + y
print("Sum: ", sum(4, 5))

attack = {'quick': (lambda: print("Quick Attack")),
          'power': (lambda: print("Power Attack")),
          'miss': (lambda: print("Missed Attack"))}

attack['quick']()
import random
attackKey = random.choice(list(attack.keys()))
attack[attackKey]()


print()

import random
roll_list  = []

#Populate the list with 100 Hs and Ts
for i in range(1, 101):
  roll_list += random.choice(['H', 'T'])
  
# Output the result
print("Heads :",  roll_list.count('H',))
print("Tails :",  roll_list.count('T')) """

import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile(""))