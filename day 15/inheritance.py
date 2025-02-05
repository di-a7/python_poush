# Inheritance - Parent class, child class
# parent class should be defined inside the parentesis of the child class
# child class can use attributes and methods of the parent class
# child class can have their own attributes and methods
# parent class ko methods and attributes can be overridden in the child class
class Car:
   model = None
   color = None
   def get_car_details(self, model, color):
      self.model = model
      self.color = color
# c1 = Car()
# c1.get_car_details("Tata","white")
# print(c1.model)

class EV(Car):
   speed = None
   def get_speed(self, speed):
      self.speed = speed
   
   def get_car_details(self, model):
      self.model = model

class EvChild(EV):
   pass

ev1 = EV()
ev1.get_car_details("ABC")
ev1.get_speed("200")
print(ev1.model)
print(ev1.speed)

# todo:
# class named person, attributes name and age, method introduction
# class name student, it inherits person class, attributes class and roll number, method get_class_roll
# create object of student class, print out introduction, class and roll number