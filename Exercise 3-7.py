myList = ['Khan', 'Amjad', 'Ali', 'Junaid', 'Ahsan']
print(myList)

myList.remove('Khan')
print(myList)

myList.append('Adil')
print(myList)

myList.append('Awais')
myList.append('Waheed')
myList.insert(7, 'Aziz')
print(myList)

print('Hi ' + myList[0],', I can only invite 2 persons for dinner.')
print('Hi ' + myList[1],', I can only invite 2 persons for dinner.')
print('Hi ' + myList[2],', I can only invite 2 persons for dinner.')
print('Hi ' + myList[3],', I can only invite 2 persons for dinner.')
print('Hi ' + myList[4],', I can only invite 2 persons for dinner.')
print('Hi ' + myList[5],', I can only invite 2 persons for dinner.')
print('Hi ' + myList[6],', I can only invite 2 persons for dinner.')
print('Hi ' + myList[7],', I can only invite 2 persons for dinner.')

myList.pop(7)
myList.pop(6)
myList.pop(5)
myList.pop(4)
myList.pop(3)
myList.pop(2)
print(myList)

print('Hi ' + myList[0],'You are invited for dinner tomorrow.')
print('Hi ' + myList[1],'You are invited for dinner tomorrow.')

del myList
print(myList)