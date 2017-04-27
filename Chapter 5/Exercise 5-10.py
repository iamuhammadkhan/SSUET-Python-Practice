current_users = ['Khan', 'Ali', 'Waheed', 'Adil', 'Noor']

new_user = ['Aziz', 'Zohaib', 'Adil', 'Noor', 'Ali']

for i in new_user:
    for a in current_users:
        if i.lower() in a.lower():
            print(i + ' need to enter a new username')
    print('username is available')
