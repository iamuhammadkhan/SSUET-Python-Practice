new_message = ''

def make_shirt(size, message = new_message):
    if size == 'S':
        new_message = 'Hello World'
    elif size == 'M':
        new_message = 'I Am Learning Python'
    else:
        new_message = 'I Love Python'
    print('You have ordered a ' + size + ' shirt with the message "' + new_message + '" printed on it')

make_shirt('S')
make_shirt('M')
make_shirt('L')
make_shirt('XL')

