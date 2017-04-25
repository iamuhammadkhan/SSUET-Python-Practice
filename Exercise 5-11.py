ordinal_number = []

numbers = [1,2,3,4,5,6,7,8,9]

for i in numbers:
    if i == 1:
        a = (str(i)+'st')
        print(a)
        ordinal_number.append(a)
    elif i == 2:
        a = (str(i) + 'nd')
        print(a)
        ordinal_number.append(a)
    elif i == 3:
        a = (str(i)+'rd')
        print(a)
        ordinal_number.append(a)
    else:
        a = (str(i) + 'th')
        print(a)
        ordinal_number.append(a)
print(ordinal_number)

