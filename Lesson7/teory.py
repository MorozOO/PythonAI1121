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