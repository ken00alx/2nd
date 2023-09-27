""" numbers = [5, 3, 2, 1, 6, 8]
numbers1 = numbers.copy()
numbers.append(10)

print(numbers1)

i = 1
while i <= 5:
  print(i)
  i += 1
print(i, "Done")

 """
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
  guess = int(input('Guess: '))
  guess_count += 1
  if guess  == secret_number:
    print("You Won!")
    break
else:
    print("Ops, Guess incorrect")