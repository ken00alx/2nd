def safe_print_integer(value):
  try:
    print("{:d}".format(value))
  except ValueError:
    return False
  
value = input("Enter a value either int float or string")
value_print = safe_print_integer(value)
if not value_print:
  print("{} is not an integer". format(value))

value = -89
value_print = safe_print_integer(value)
if not value_print:
  print("{} is not an integer". format(value))

value = "School"
value_print = safe_print_integer(value)
if not value_print:
  print("{} is not an integer". format(value))