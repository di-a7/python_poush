# Ecommerce program

# Requirements
# register
# login
# usertype= seller, buyer
# seller:
#     product add
#     list your product 
#     delete
# buyer:
#     list all the products
#     buy product
#     billing

# logout

# Workflow
# ask user (login or register)
# if register, ask for username, usertype and password, store username, usertype, password it in a file
# if login, ask for username and password, and check if the username exist in the file and password is correct,
# if the logged in user, usertype is seller, show options(
# product add (name,quantity, description, price) - store it in a file
#     list your product (seller ko name)
#     delete)
# if the logged in users' usertype is buyer, show options(list product - (all product), buy produt, optional:billing)
# login crediential,not match validation error
# in a loop

import json;

def add_product(seller):
   name = input("Name:")
   quantity = input("Quantity:")
   description =input("Description")
   price = input("Price:")
   
   a = {"name":name,
        "quantity":quantity,
        "description":description,
        "price":price,
        "seller":seller}
   
   json_a = json.dumps(a)
   f = open("ecom_product.txt",'a')
   f.write(json_a+'-')
   f.close()
   print("Product has been added.")

def list_product():
   f = open("ecom_product.txt",'r')
   a = f.read().split('-')
   f.close()
   for i in a:
      if i != '':
         print(i)
   # print(a)

def view_your_product(username):
   f = open("ecom_product.txt",'r')
   a = f.read().split('-')
   f.close()
   for i in a:
      if i != '':
         dict_a = json.loads(i)
         if dict_a.get('seller') == username:
            print(dict_a)

def buy_product():
   f = open('ecom_product.txt','r')
   a = f.read().split("-")
   f.close()
   buy = input("What do you want to buy?>>")
   quantity = int(input("What much you want to buy?>>"))
   for i in a:
      if i != '':
         dict_a = json.loads(i)
         if dict_a.get('name') == buy:
            price = int(dict_a.get('price')) * quantity
            print(f"Total Price:{price}")

def delete(username):
   f = open("ecom_product.txt",'r')
   a = f.read().split('-')
   f.close()
   for i in a:
      if i != '':
         dict_a = json.loads(i)
         if dict_a.get('seller') == username:
            print(dict_a)
   delete = input("What do you want to delete:")
   b = []
   for i in a:
      if i != '':
         dict_a = json.loads(i)
         if dict_a.get('name') == delete:
            dict_a.clear()
         json_a = json.dumps(dict_a)
         if b == []:
            f = open("ecom_product.txt",'w')
         else:
            f = open("ecom_product.txt",'a')
         f.write(json_a+'-')
         f.close()

def register():
   username = input("Enter username:")
   usertype = input("Enter usertype('buyer/seller): ").lower()
   password = input("Enter password:")
   
   a = {"username":username,
        "usertype":usertype,
        "password":password}
   
   json_a = json.dumps(a) #converts dictionay into json format
   f = open('ecom_user.txt','a')
   f.write(json_a+'-')
   f.close()


def login():
   username = input("Enter username:")
   password = input("Enter password:")
   f = open('ecom_user.txt','r')
   a = f.read()
   list_a = a.split("-")
   for i in list_a:
      if i != '':
         dict_i = json.loads(i)
         if dict_i.get('username') == username and dict_i.get('password') == password:
            usertype = dict_i.get('usertype')
   
   if usertype == "seller":
      choice = input('''
                     1. Add Product
                     2. View your products
                     3. Delete
                     >>''')
      
      if choice == "1":
         add_product(username)
      elif choice == "2":
         view_your_product(username)
      elif choice == "3":
         delete(username)
      else:
         print("Invalid crediential")
      
      
   elif usertype == "buyer":
      choice = input('''
                     1. List Product
                     2. Buy products
                     >>''')
      if choice == "1":
         list_product()
      elif choice == "2":
         buy_product()


choice = input("Register/Login: ").lower()
if choice == "register":
   register()
elif choice == "login":
   login()