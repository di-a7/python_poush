# ask user (login or register)
# if register, ask for username and password, store username, password it in a file
# if login, ask for username and password, and check if the username exist in the file and password is correct
# if yes, show them three option (check balance, add balance, withdraw balance)
# if user choise is check print the initial balance, if balance is 0 of no data, print they have to add balance first
# if add ask user the amount to add and add it with the balance, data lai next file ma save, {username:added_balance}
# if withdraw, ask the amount, check if the amount is greater than the balance, if the yes break but if no subtract the amount with the balance
# if username and password doesnot match, print some you have register first.

import json

def add_balance(username):
   amount = input("Enter the amount you want to add:")
   a = {username:amount}
   json_a = json.dumps(a)  #dictionary lai convert into json format
   f = open("useraccount.txt",'a')
   f.write(json_a+'-')
   f.close()
   print("Amount added.")

def check_balance(username):
   f = open("useraccount.txt",'r')
   a = f.read().split("-")
   f.close()
   add = 0
   for i in a:
      if i != '':
         dict_i = json.loads(i)
         if username in dict_i:
            add += int(dict_i.get(username))
   print(f"Your balance is {add}")


def register():
   username = input("Enter username:")
   password = input("Enter password:")
   
   a = {username:password}
   
   json_a = json.dumps(a) #converts dictionay into json format
   f = open('userdata.txt','a')
   f.write(json_a+'-')
   f.close()

def login():
   is_login = False
   username = input("Enter username:")
   password = input("Enter password:")
   
   f = open('userdata.txt','r')
   a = f.read().split("-")
   f.close()
   for i in a:
      if i != '':
         dict_i = json.loads(i)
         if dict_i.get(username) == password:
            print("Login success")
            is_login = True
   
   if is_login:
      choice = input('''\
         1.Add balance
         2.Check balance
         3.Withdraw balance
         >>>''')
      if choice == "1":
         add_balance(username)
      elif choice == "2":
         check_balance(username)
choice = input("Register/Login: ").lower()
if choice == "register":
   register()
elif choice == "login":
   login()