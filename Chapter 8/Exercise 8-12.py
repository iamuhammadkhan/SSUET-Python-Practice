def order_sandwich(type):
    print('You have ordered ' + type)

order_sandwich('club sandwitch')

def order_sandwich(type, quantity):
    print('You have ordered ' + str(quantity)+ ' ' + type)

order_sandwich('Special Sandwich', 2)

def order_sandwich(type, quantity, time):
    print('You have ordered ' + str(quantity)+ ' ' + type + ' in ' + str(time) + ' minutes')

order_sandwich('Special Sandwich', 2, 10)