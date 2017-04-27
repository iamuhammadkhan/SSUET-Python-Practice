favourite_fruits = ['Mango', 'Banana', 'Apple']

user_input = input('Please write your favourite fruit ')

#if user_input in favourite_fruits:
#    print('Hey thats my favourite fruit as well')
#lse:
#   print('Your choice is different from mine')

if user_input in favourite_fruits:
    print('Hey you really like ' + user_input)
else:
    print('Thats not my favourite fruit')