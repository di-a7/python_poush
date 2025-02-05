# polymorphism

a = 10
b = 5
i = a + b
# print(i)

x = "mind"
y = "risers"
j = x + y
# print(j)


class Dog:
   def move(self):
      return "Dog is walking"

class Bird:
   def move(self):
      return "Bird is flying"

class Fish:
   def move(self):
      return "Fish is swimming"

dog = Dog()
bird = Bird()
fish = Fish()

print(dog.move())
print(bird.move())
print(fish.move())