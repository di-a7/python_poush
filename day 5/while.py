#  while loop - multi lined statement,
# conditional statement, if condition true, while vitra vako statements haru run huni vayo
# while should contain logics that convert the true condition into false
# while vitra vako statements haru sakisakipxi feri while ma vako condition check garxa
# syntax
# while True:
#    print("Hello World")

a = 0
b = 5
while a < b:
   a += 1 
   if a == 3:
      continue
   # print(a)

print("Outside the loop")

# break - loop terminate even though the condition is true, read next line

# continue - start the loop again

# Exam mark evaluator
# ask user for the exam mark
# if mark is greater than 90 and smaller than 100 then print excellent
# if mark is greater than 80 and smaller than 90 then print Very good
# if mark is greater than 70 and smaller then 80 then print good
# if mark is greater than 60 and smaller then 70 then print fair
# if mark is greater than 50 and samller than 60 then print could have been better
# if mark is greater then 40 and smaller then 50 then print pass
# if mark is less than 40 print fail

mark = int(input("Enter your mark:"))
if mark >= 90 and mark <= 100:
   print("Excellent")
elif mark >= 80 and mark < 90:
   print("Very Good")
elif mark >= 70 and mark < 80:
   print("Good")
elif mark >= 60 and mark < 70:
   print("Fair")
elif mark >= 50 and mark < 60 :
   print("could have been better")
elif mark >= 40 and mark < 50:
   print("pass")
elif mark < 40:
   print("fail")
else:
   print("Input invalid")