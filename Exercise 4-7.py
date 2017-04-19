data = []

my_range = range(1,30)

for a in range(len(my_range)):
    if a % 3 != 0:
        data.append(my_range[a])

print(data)