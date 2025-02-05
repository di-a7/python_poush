# Encapuslation - encapsulating methods and attributes in a single unit, data hiding
# '__' followed by the attributes or method name is used to hide the data,
# prevents direct access of attributes and methods by objects
class Login:
   __email = None
   __password = None
   
   def get_details(self, email, password):
      self.__email = email
      self.__password = password
   
   def __detail(self):
      return f"{self.__email} - {self.__password}"
   
   def pprint(self):
      a = self.__detail
      print(a)

l1 = Login()
l1.get_details("diya@gmail.com","123")
# print(l1.__email)
# print(l1.__password)
# print(l1.__detail())
print(l1.pprint())