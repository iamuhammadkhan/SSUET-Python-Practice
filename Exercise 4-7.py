data = []

my_range = range(1,31)

for a in range(len(my_range)):
    if a % 3 == 0:
        data.append(my_range[a])

print(data)