user_input = int(input('Please enter your age '))

if user_input <= 3:
    print('You are under age you can watch the movie for free')
elif user_input <= 12:
    print('You have to pay $10 to watch the movie')
else:
    print('You have to pay $15 to watch the movie')