""" random = [45, 93]

# transforming a list into an iterator
random_iterator = iter(random)

print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
 """
""" 
nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 
 
pos = nameList.index("GeeksforGeeks") 
 
print (pos * 3) """


""" D = dict() 
for x in enumerate(range(2)): 
    D[x[0]] = x[1] 
    D[x[1]+7] = x[0] 
print(D) """ 
numb = "\125\145\140\130\125"
numb1 = r"\125\145\140\130\125"
print(f'This is the output of numb in string form:',numb)
print(f'This is the output of numb in octal form:',numb1)