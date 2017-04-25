names = {1:'Amjad', 2:'Adil', 3:'Waheed', 4:'Awais'}

for i in set(names.keys()):
    print(i)

for j in set(names.values()):
    print(j)

aliens = []

for alien_number in range(5):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:2]:
    print(alien)

friends = []

for new_friends in range(5):
    my_friends = {'name': 'Amjad', 'age': 33, 'city': 'Karachi'}
    friends.append(my_friends)

print(friends)