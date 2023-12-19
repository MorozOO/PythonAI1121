def nameFunction():
    pass

class Student:
    # print("Hi")
    counter = 0
    def __init__(self,n = "name", money = 0):
        self.name = n
        self.money = money
        Student.counter+=1
    def printInfo(self):
        print(f"{Student.counter} : {self.name}, money = {self.money}")

    def addMoney(self,coin):
        self.money += coin

    def subMoney(self, coin):
        self.money -= coin


Taras = Student("Taras")
Taras.printInfo()
Taras.addMoney(10)

Taras.printInfo()
# print(Taras.counter)
Sviat = Student("Sviat")
Sviat.printInfo()
Sviat.addMoney(20)
Sviat.printInfo()
# print(Sviat.counter)
Kate = Student()
Kate.printInfo()
Kate.addMoney(100)
Kate.printInfo()
Kate.subMoney(20)
Kate.printInfo()


# print(Kate.counter)
