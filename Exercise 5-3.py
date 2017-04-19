alien_life = 10
alien_color = 'Red'

if alien_color == 'Green':
    alien_life += 5
    print('You have received 5 points')
elif alien_color == 'Yellow':
    alien_life -= 5
    print('You just lost 5 points')
else:
    print('You lost')