class Car:                                              #Klasa (blueprint) za auto
    def __init__(self, model, year, color, for_sale):   #Konstructor metod potreban za kreiranje metoda (dunder double underscore __ metod)
        self.model = model                              #Pristupanje atributima preko self
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")