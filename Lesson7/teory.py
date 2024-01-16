text  = 'itStep'
print(text[1])

myList = [1,2,3,4,5,1]
print(myList)

mySet = set(myList)
print(mySet)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print('-'*20)
for i in myList:
    print(i)

# for key, val in thisdict:
#     print(key, val)

iterator = iter(thisdict)
n = next(iterator)
print(n, thisdict[n])

n = next(iterator)
print(n, thisdict[n])

n = next(iterator)
print(n, thisdict[n])

it = iter(myList)

for elem in it:
    print(elem)
import random
forList = []
for i in range(9):
    a = random.randint(0,10)
    if a %2 ==0 :
        forList.append(a)

print(forList)


generatorList = [random.randint(0,10) for i in range(9)]
print(generatorList)

generatorList = [i**2 for i in range(2,20)]
print(generatorList)

def degrees(num, max_degrees):
    i = 0
    for _ in range(max_degrees):
        yield num * i
        i+=1

res = degrees(123,500)
print(res)
for _ in res:
    print(_)