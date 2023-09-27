import random

random.seed(56255)
randomInteger = random.randint(1, 10)
print(randomInteger)

raodomFloat = random.random() * 5
print(randomFloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")


test_seed = int(input("Create a seed number: "))
random.seed(test_seed)