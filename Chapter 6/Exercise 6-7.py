new_friends = {'name': 'Zahid', 'name': 'Javed', 'name': 'Awais'}

old_friends = {'name': 'Amjad', 'name': 'Waheed', 'name': 'Adil'}

best_friends = {'name': 'Junaid', 'name': 'Ahsan'}

all_friends = []

for i in set(new_friends.values()):
    all_friends.append(i)
    print(all_friends)
    for j in set(old_friends.values()):
        all_friends.append(j)
        print(all_friends)
        for h in set(best_friends.values()):
            all_friends.append(h)
            print(all_friends)

print(all_friends)