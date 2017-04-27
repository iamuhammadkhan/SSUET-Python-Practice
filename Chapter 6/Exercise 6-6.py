exercise = {'Python': 'Python: is the most valuable language for AI', 'Swift': 'Swift: is a language used to develop iOS Applications', 'Java': 'Java: is being used to develop Android Applications'}

friends = ['Amjad', 'Adil', 'Waheed', 'Khan']

for i in set(exercise.keys()):
    for j in friends:
        if i == 'Python' and j == 'Khan':
            print('Thank you for taking the poll')
        elif i == 'Python' and j == 'Amjad':
            print('Please take the poll')
        elif i == 'Python' and j == 'Adil':
            print('Please take the poll')
        elif i == 'Python' and j == 'Waheed':
            print('Please take the poll')

