class Cat:
    def __init__(self,name="cat"):
        self.age = 1
        self.name = name
        self.health = 100
        self.food = 100
    def life(self):
        self.age += 0.3
        self.health -= 20
        self.food -= 10
    def eat(self):
        self.health += 20
        self.food += 10

    def printInfo(self):
        print(self.age)
        print(self.name)
        print(self.health)
        print(self.food)

cat1 = Cat("Snow")
cat1.printInfo()
cat1.life()
cat1.printInfo()
cat1.eat()
cat1.printInfo()
cat1.eat()
cat1.printInfo()
cat1.life()
cat1.printInfo()

