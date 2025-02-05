# # String
# a = "Hello World"
# b = a.capitalize()
# c = a.count()
# d = a.split("l")
# print(d)

# list
a = ["a","b","c","d","e","a","a","a"]
a.append("Abc")
b = a.count("a")
# a.reverse()
# print(a)
# print(b)

# tuple
a = ("a","b","a","b","b","d","e")
b = a.count("a")
c = a.index("b")
# print(c)

# set
a = {1,2,3,4,5}
b = {4,5,6,7,8}

c = a.intersection(b)
a.intersection_update(b)
# print(a)

# difference, difference_update, union

# dictionary
a = {1:"ram",2:"shyam",3:"hari"}
print(a.get(4))
b = a.get(2)
c = a.items()
d = a.values()
e = a.keys()
# print(b)
# print(c)
# print(d)
# print(e)

# todo:
# create a dictionary that contains username and password, username as key and password as value
# ask user for their username and password
# check if the username and password exist in the dictionary
# if yes print("Welcome")
# if no print("Invalid username or password")

# userdata = {"ram":"123","shyam":"456","hari":"hari"}
# username = input("Enter username: ")
# password = input("Password: ")
# if username in userdata and userdata.get(username) == password:
#    print("Login successful")
# else:
#    print("Invalid credentials")