# sequential datatype matra indexing and slicing

a = "hello world"
# h = 0
# e = 1
# l = 2

# print(a[1:5])
# print(a[::2])

a = "Ram is ( programmer"
# print programmer
# print(a[9:])
# # print (
# print(a[7])
print(a[7:9])

#  list

a = ["apple","mango","orange","watermelon"]
# apple = 0
# mango = 1
# print(a[1:3])
# print(a)
# a[0] = "grapes"   # mutable
# print(a)

# Tuple
a = ("apple","mango","orange","watermelon")
print(a[1])

# a[0] = "grapes"   # immutable
# print(a)

# todo: remove duplicate datas
# a = ("apple","grapes","mango","orange","watermelon","mango","orange","watermelon")

# dictionary - keys are used to access its value
person = {"name":"Ram",
      "age":"25",
      "hobbies":["reading books","sleeping","drawing"]}
# a = person['hobbies']
# print(a)
# print(a[1])
# print(person['name'])
# print(person['age'])
# print(person['hobbies'])
# print(person['hobbies'][1])
# print(person['hobbies'][0][8:])

person['age'] = 200
# print(person)

# age
# hobbies
# hobbies 1 index data
# hobbies 0 index data print books

# todo : apple = grapes should be printed in tuple
a = ("apple","mango","orange","watermelon")
b = list(a)
b[0] = "grapes"
a = tuple(b)
print(a)