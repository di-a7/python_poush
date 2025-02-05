#  function - like variable, it stores block of code, multilined, reusablility, clean code
#  syntax
# def function_name():
   # statements

def Hello():
   print("Hello World")
   print("Hello World")
   print("Hello World")

# Hello()
# print("BREAK")
# Hello()

# variables used in function are parameters
# def student(firstname):
#    print("Hello")
#    print(f"My name is {firstname}")

# data send to function are arguments
# first = "ram"
# student(first)



# local variable - variable declared inside the function, can be used only inside the function

# global variable - variable declared outside the function, can be used any where in the program
# glo = "Global"
# print(glo)

# def hello():
#    local = "abc"
#    print(glo)
#    print(local)

# hello()
# a = 10

# def add():
#    b = 10
#    global a
#    a = a + 10
#    print(a*10)
   # a = a + 10
   # print("Inside the function")
   # print(a)

# print(a)
# add()
# print("Outside the function")
# print(a)

# postional_argument - parameter accept the arguments according to the position
# def student(firstname, lastname,age):
#    print(f"Firstname: {firstname}")
#    print(f"Last name: {lastname}")

# student("Ram","Shrestha",0)
# student(lastname="Shrestha",firstname = "Ram")


# data send to function are arguments
# first = "ram"
# last = "shrestha"
# student(lastname = last, firstname = first)

# keyword argument - keyword is used to assign the valude when calling the function
# def student(firstname, lastname):
#    print("Hello")
#    print(f"My name is {firstname} {lastname}")

# # data send to function are arguments
# first = "ram"
# last = "shrestha"
# student(lastname = last, firstname = first)

# default argument - if user provide values the parameter takes thoses values otherwise it uses the default values
def student(firstname = "firstname", lastname = "lastname", age="18"):
   print(f"Firstname: {firstname}")
   print(f"Last name: {lastname}")
   print(f"Age: {age}")

# student("Ram","SHestha")

# args(arguments) = * used to define args, multiple data or values can be passed
def numbers(*args):
   print(args)
   for i in args:
      print(i)

# numbers('ram','shyam','gopal','hari')

def add(*args):
   a = 0
   for i in args:
      a += i
   print(a)

# add(5,10,50,50,60,"sdfj")

# kwargs(keyword arguments)- ** used to define kwargs, accepts multiple keyword arguments , accepts dictionary datatype, methods of dictionary can be used to access and manipulate the kwargs

def person(**kwargs):
   print(kwargs)
   for key in kwargs.values():
      print(key)
# {"key":"value"}
# person(name = "Ram",age = 20 ,phone=987535132, address ="ktm") #{"name":"Ram","age":"20"....}

def person(name,*a,**kwargs):
   print(a)
   print(f"name:{name}")
   print(kwargs)

person("Ram","ktm","987465632","25",dob = 2000,house = "ktm")