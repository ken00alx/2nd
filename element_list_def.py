#Recursive factorial function
def safe_print_list(my_list=[], x=0):
  index = 0
  while True:
    try:
      if index < x:
        print(my_list[index], end='')
        index += 1
      else:
        print()
        return index
    except IndexError:
      print()
      return index
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print('nb_print: {:d}'.format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))