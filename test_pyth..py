""" names = ['Jon', 'Gary', 'Kens', 'Mosh', 'Rays']
print(names)
names[0] = 'John'
print(names[2:])
print(names) """

largest_number = [21, 54, 25, 15, 10, 5, 65]
max = largest_number[0]
mean = largest_number[0]
for number in largest_number:
  if number > max:
    max = number
    print(max)

numbers = [2, 5, 5, 5, 10, 10,  2, 65]
nu_mbr = []
for number in numbers:
  if number not in nu_mbr:
    nu_mbr.append(number)
    #print(nu_mbr)
print(nu_mbr)

x, y, z = (2, 3, 4)
print (y)



customer = {
  "name": "John SMith",
  "age": 34,
  "is_verified": True
}
customer["Phone"]= "08160757042"

print(f'Name: ', customer["name"])
print(f'Phone No: ', customer["Phone"])


phone = input("Phone: ")
figure = {
  "1" : "One",
  "2": "Two",
  "3": "Three",
  "4": "Four"  
}
output = ""
for dit in phone:
  output += figure.get(dit, "!") + " "
print(output)