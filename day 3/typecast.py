#  Typecasting - converting a datatype into another datatype

# string - str()
a = 123
b = str(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# interger - int()
a = "123 ahddfk"
b = int(a)
# print(type(a))
# print(type(b))

# float - float()
a = 123
b = float(1325)
# print(a)
# print(b)

# list - list()- []
a = "Hello"
c = ("a","abc","apple")
b = list(a)
d = list(c)
# print(b)
# print(d)

# tuple - tuple() -()
my_list = ["a","abc","apple"]
my_tuple = tuple(my_list)
# print(my_tuple)

# set - set()
my_list = ["a","abc","apple","apple","a"]
my_set = set(my_list)
# print(my_set)

# dictionary - dict()
my_tuple = [(1,"b"),(2,'c'),(3,'c')]
my_dict = dict(my_tuple)
print(my_dict)