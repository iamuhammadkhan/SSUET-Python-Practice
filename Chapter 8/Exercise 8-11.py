my_list = ['Khan', 'Adil', 'Waheed']

new_list = []

def make_great():
    for i in my_list:
        print(' The Geat ' + i)
        new_list.append(i)

make_great()
print(new_list)