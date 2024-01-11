try:
    a = input()
    print(100/int(a))
except ZeroDivisionError:
    print(f"Неможливо ділити на 0. Це математичне правило")
except :
    print(f"неможливо виконати ділення на {a}")
else:
    print("блок відпрацював без помилок")
finally:
    print("блок завершено ")
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
mater = 400
check_material(mater,300)


import  warnings

warnings.simplefilter("ignore",SyntaxWarning)
warnings.simplefilter("always",ImportWarning)

warnings.warn("Обережно, тут немає коду", SyntaxWarning)
warnings.warn("Попередження, модуль не імпортувався", ImportWarning)