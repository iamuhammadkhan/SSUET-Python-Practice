f_name = input('Eneter your first name: ')
l_name = input('Enter your last name: ')

def make_profile(habit, hobby, age):
    print('Hello ' + f_name + ' ' + l_name + ' you are ' + str(age) + ' years old ' + 'your hobby is ' + hobby + ' and your habit is ' + habit + '. Thank you')

make_profile('trying to be polite', 'programming', 32)