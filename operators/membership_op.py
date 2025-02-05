#  membership operator - check if a data/value exist in a sequential/group datatype, output (True/False), one of the variable should contain sequential datatype
# in operator (output true if a data is a member of sequential datatype)
animal = "lion"
animals = ["dog","cat","cow","goat"]

a = animal in animals
# print(a)

# # not in operator ( output true if a data is not a member of sequential datatype)
A = animal not in animals
# print(A)

a = "H"
b = "Hello World"
# print(a in b)


# Todo: check if a is the member of b
a = ['a','b','c']
b = ['a','b','c',['a','b','c']]

print(a in b)