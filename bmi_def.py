name1 = "XK"
height_m1 = 3
weight_kg1 = 90

name2 = "XK's Sister"
height_m2 = 1.6
weight_kg2 = 69

name3 = "KX"
height_m3 = 2.4
weight_kg3 = 160


def bmi_calculator(name, height_m, weight_kg):
  bmi = weight_kg / (height_m ** 2)
  print(bmi)
  print("bmi: ")
  if bmi < 25:
    return name + " is not overweight"
  else:
    return name + " is overweight"
  
result = bmi_calculator(name1, height_m1, weight_kg1)
result1 = bmi_calculator(name2, height_m2, weight_kg2)
result2 = bmi_calculator(name3, height_m3, weight_kg3)

print(result)
print(result1)
print(result2)