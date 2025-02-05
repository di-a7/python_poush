class Burger:
   def bun(self):
      print("Bun")
      return self
   
   def patty(self):
      print("Patty")
      return self
   
   def sause(self):
      print("Sause")
      return self

burger1 = Burger()
# normal method call
burger1.bun()
burger1.sause()
burger1.patty()
burger1.sause()
burger1.bun()

# Method chain
print("\nUsing Method chain")
burger1.bun().sause().patty().sause().bun()