""" class Person:
  pass # An empty block
p = Person()
print(p)

class Person1:
  def say_hi(self):
    print("Hello how are you?")
    
ps = Person1()
ps.say_hi()
Person1().say_hi """

class Persona:
  def __init__(self, name):
    self.name = name
  
  def say_me(self):
    print("Hello, my name is ", self.name * 2)

being = Persona('Swarmed ')
being.say_me()


x = 12
x += 3
print(x)

x **= 3
print(x)