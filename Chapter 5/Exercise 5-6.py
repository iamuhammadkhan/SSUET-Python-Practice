person_age = int(input('Please enter your age '))

if person_age <= 2:
    print('The person is a baby')
elif person_age <= 4:
    print('The person is toddler')
elif person_age <= 13:
    print('The person is a kid')
elif person_age <= 20:
    print('The person is a teenager')
elif person_age <= 65:
    print('The person is adult')
elif person_age > 65:
    print('The person is older')
else:
    print('You have entered invalid value')