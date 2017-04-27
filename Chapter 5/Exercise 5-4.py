alien_life = 10

alien_color = str(input('Please enter a color to improve alien life '))

if alien_color == 'green':
    alien_life += 5
    print('You just scored 5 points')
elif alien_color == 'yellow':
    alien_life += 10
    print('You just scored 10 points')
else:
    print('You lost')