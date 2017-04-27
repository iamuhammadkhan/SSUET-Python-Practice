student_list = ['Khan', 'Adil', 'Awais']

print('Welcome to the student portal')
print('Please enter 1 to view list of students')
print('Please enter 2 to add new student')
print('Please enter 3 to search a student')
print('Please enter 4 to delete a student')
print('Please enter 5 to sort the students')
print('Please enter 6 to exit')

while(True):
    user_input = int(input('Enter a number of your choice '))

    if user_input == 1:
        for studentnames in student_list:
            print(studentnames)
    elif user_input == 2:
        add_name = input('Enter a name to add ')
        student_list.append(add_name)
        print(student_list)
    elif user_input == 3:
        userInput = input('Search for student name ')
        if userInput in student_list:
            print(userInput + ' Found')
        else:
            print('Not found')
    elif user_input == 4:
        userInput = input('Enter a student name to delete ')
        if userInput in student_list:
            student_list.remove(userInput)
            print(userInput + ' deleted')
        else:
            print('Not found')
    elif user_input == 5:
        student_list.sort()
        print('Sorted')
        print(student_list)
    elif user_input == 6:
        exit()
    else:
        print('You have entered a wrong choice please try again')