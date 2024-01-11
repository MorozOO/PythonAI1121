class Human:
    def __init__(self, name = "Human"):
        self.name = name

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self,human):
        self.passengers.append(human)

    def print_passengers(self):
        if self.passengers != []:
            print(f"Name of brand - {self.brand} , passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"Name of brand - {self.brand}")
    def sub_passenger(self, number = 0):
        if self.passengers != []:
            if number < len(self.passengers):
                self.passengers.pop(number)
            else:
                self.passengers.pop()
car1 = Car("Toyota")
h1 = Human("Taras")
h2 = Human("Andiy")
h3 = Human("Roma")
car1.add_passenger(h1)
car1.add_passenger(h2)
car1.print_passengers()
car1.add_passenger(h3)
car1.print_passengers()
car1.sub_passenger(4)
car1.print_passengers()
class Human:
    def __init__(self, name = "Human"):
        self.name = name

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self,human):
        self.passengers.append(human)

    def print_passengers(self):
        if self.passengers != []:
            print(f"Name of brand - {self.brand} , passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"Name of brand - {self.brand}")
    def sub_passenger(self, number = 0):
        if self.passengers != []:
            if number < len(self.passengers):
                self.passengers.pop(number)
            else:
                self.passengers.pop()
car1 = Car("Toyota")
h1 = Human("Taras")
h2 = Human("Andiy")
h3 = Human("Roma")
car1.add_passenger(h1)
car1.add_passenger(h2)
car1.print_passengers()
car1.add_passenger(h3)
car1.print_passengers()
car1.sub_passenger(4)
car1.print_passengers()
