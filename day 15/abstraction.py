# abstraction - hiding unncessary event from the users and only showing the relevent or necessary events to users

class Bike:
   clutch = False
   acc = False
   
   def start(self):
      clutch =True
      acc = True
      return "Bike start"  # clutch and acc are the unnecessay events when starting the bike so they are hidden.

b1 = Bike()
print(b1.start())