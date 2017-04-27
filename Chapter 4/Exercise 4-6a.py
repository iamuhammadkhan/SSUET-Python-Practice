odd = []
my_range = range(1,21)

for a in range(len(my_range)):
    if a % 2 != 0:
        odd.append(my_range[a])

print(odd)