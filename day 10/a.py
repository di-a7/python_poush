# Accounting Task
# create a dictionary that stores username as key and password as value
# create a dictionary that stores username and balance as key and value respectively {"ram":"100000"}
# ask user for username and password, check if it exist in the dictionay
# if yes,(login) show them three option (check balance, add balance, withdraw balance)
# if user choise is check print the initial balance
# if add ask user the amount to add and add it with the balance
#  if withdraw, ask the amount, check if the amount is greater than the balance, if the yes break but if no subtract the amount with the balance
# if username and password doesnot match, print some remark


userdata = {"ram":"123"}
account = {"ram":10000}
name = input("Enter your name:")
password = input("Enter your password:")

if name in userdata and userdata[name]==password:
   print("LOgin in")
   a = input('''
             1. Check
             2.Add
             3.Withdraw >>''')
   
   if a == "1":
      print(f"Balance:{float(account[name])}")
      
   elif a == "2":
      amt = int(input("Enter the amount:"))
      amt += account[name]
      print(f"Balance:{amt}")
   
   elif a == "3":
      amt = int(input("Enter the amount:"))
      if amt > account[name]:
         print("You dont have enough balance.")
      else:
         account[name] -= amt
         print(f"Balance:{account[name]}")
else:
   print("INvalid credientials")