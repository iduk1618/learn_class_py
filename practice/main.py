from car import Car

car1 = Car("Dodge", 2025, "black", False)               #Kreiranje "car1" objekta
car2 = Car("Audi", 2020, "blue", True)                  #Kreiranje "car2" objekta

car1.drive()
car1.stop()

car2.drive()
car2.stop()

car1.describe()
car2.describe()