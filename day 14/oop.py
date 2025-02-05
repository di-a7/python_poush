# OOP - Object Oriented Programming
# Inheritance, Polymorphis, encapsulation, abstraction

# class - structure, blueprint
# objects - data created using class, single class can have multiple objects, variable in class are called attribute, functions in class are called methods
# self takes objects name as argument, it is used for connectivity, every function in class must have self as parameter
class Person:
   name = None
   age = None
   
   def intro(self,name,age):
      a = f"My name is {name} amnd age is {age}."
      return a
   
   def __str__(self):
      return "this is the string represention"

person1 = Person()
person2 = Person()

a = person1.intro("Ram",25)
# print(a)
print(person1)
print(person1.__dir__())

# create class named car
# car has attribute model and color
# one method
# 2 objects of that class