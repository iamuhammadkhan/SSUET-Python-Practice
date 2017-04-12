even = []
odd = []
my_range = range(1,21)

for a in range(len(my_range)):
    if a % 2 == 0:
        even.append(my_range[a])
    else:
        odd.append(my_range[a])

print(even)
print(odd)