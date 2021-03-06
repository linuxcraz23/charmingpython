# populating a list with elements from another list
listOfDays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
animalFarm = ['dog', 'cat', 'cow', 'hen', 'rat']
print("initial list 1 : ", listOfDays)
print("initial list 2 : ", animalFarm)
listOfDays.extend(animalFarm)
print("updated list : ", listOfDays)

# creating a list with operations
squares = []
for i in range(0,10):
    squares.append(i**2) #rather than each time printing this variable will append result in list name 'squares'.
print(squares)

# another shorter way
squares2 = [x**2 for x in range(0,10)]
print(squares2)

# list inside a list known as List comprehension:
multiList = [  ['Mon', 'Tue', 'Wed'],  ['Thu', 'Fri', 'Sat', 'Sun'] ]
print(multiList)
print(multiList[0])
print(multiList[1])

print(multiList[0][2]) #first list and 2nd index no
print(multiList[1][3]) #second list & 3rd index no


# creating a matrix
matrix = []
for i in range (0,3):
    tempList = []
    for j in range(0,3):
        tempList.append(i+j)
    matrix.append(tempList)

print(matrix)