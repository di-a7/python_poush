# nested 
# if condtion:
#    statement 
#    if condition:
#       statement
#    elif conditon:
#       statements
#    else:
#       statement
# elif condition:
#    if condition:
#       statement
#    elif conditon:
#       statements
#    else:
#       statement

# ask user for their age
age = int(input("Enter your age:"))
#  if user age is greater then or equal to 18, print they are eligible for license, ask if they have any vehicle, if yes print some remark, if no print some remarks,

#  if user age is smaller than 18, print they are not eligible for license, ask if they have want any vehicle, if yes ask what is it, if no  print some remark

# age should be between 10 to 80

if age >= 18:
   print("eligible for license")
   q = input("Do you have any vehicle?(y/n)")
   if q == "y":
      print("Have Vehicle")
   elif q == "n":
      print("No Vehicle")
   else:
      print("Invalid input")
elif age < 18:
   print("not eligible for license")
   q = input("Do you want any vehicle?(y/n)")
   if q =="y":
      print("Want")
   else:
      print("Don't want")
