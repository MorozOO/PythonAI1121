try:
    a = 4
    print(100/int(a))
except ZeroDivisionError:
    print(f"Неможливо ділити на 0. Це математичне правило")
except :
    print(f"неможливо виконати ділення на {a}")
print('-'*20)
# a = int(input("Enter number"))
# print(100/a)
# print('-'*20)

class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house cannot be built!"

def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return "enough material"
    else:
        raise BuildingError(amount_of_material)
mater = 123
check_material(mater,300)
