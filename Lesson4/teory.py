class Grantparent:
    height = 170
    satiety = 100
    age = 60

class Parent(Grantparent):
    age = 40
    def __init__(self):
        print(f"height - {self.height}")
        print(f"satiety - {self.satiety}")
        print(f"age - {self.age}")
class Child(Parent):
    height = 50
    age = 5
    def __init__(self):
        print(f"height - {self.height}")
        print(f"satiety - {self.satiety}")
        print(f"age - {self.age}")

nick = Child()
print("#"*50)
class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"
    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self._world = "_World"
        self.__world = "__World"
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

class Hi(Hello_world):
    def hi_printer(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        # print(self.__hello)
        # print(self.__world)

hello = Hello_world()
hello.printer()
hi = Hi()
hi.hi_printer()

print("#"*50)

class Hello:
    def __init__(self):
        print("Hello")

class Hello_world(Hello):
    def __init__(self):
        super().__init__()
        print("World")

abobus = Hello_world()
print("#"*50)

class Class1:
    var = 20
    def __init__(self):
        self.var = 10

class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)

c = Class2()

print("#"*50)

class Coputer:
    def __init__(self):
        super().__init__()
        self.memory = 128
    def calculate(self):
        print("Calculator...")

class Display:
    def __init__(self):
        super().__init__()
        self.resolution = "4K"
    def display(self):
        print("I display the image on the screen…")

class SmartPhone(Coputer,Display):
    def print_info(self):
        print(self.resolution)
        print(self.memory)

iphone = SmartPhone()
iphone.print_info()