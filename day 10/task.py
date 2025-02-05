# Exception handle
# make it function based calculator
# get  2 numbers from user
# get a operator from user(+,-,*,/)
# if operator is + then add two numbers and show the output
# if operator is - then subtract two numbers and show the output
# if operator is * then multiply two numbers and show the output
# if operator is / then divide two numbers and show the output

def add(a,b):
   c = a+b
   print(f"{a}+{b}={c}")

def subtract(a,b):
   return a-b

def multiply(a,b):
   return a*b

def divide(a,b):
   return a/b
num1 = int(input("First number:"))
num2 = int(input("Second number:"))

op = input("Operator:" )

if op == "+":
   add( num1, num2)
   
elif op == "-":
   sub = subtract(num1,num2)
   print(f"Subtraction:{sub}")
   
elif op == "*":
   m = multiply(num1, num2)
   print(f"Divide:{m}")

elif op == "/":
   d = divide(num1,num2)
   print(f"Divide:{d}")

# return - marks the end of the function
# def add(a,b):
#    c = a+b
#    return c
#    print("Hello")

# z = add(10,5)
# y = z * 2
# print(y)