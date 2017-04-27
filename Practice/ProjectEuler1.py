my_range = list(range(1000))
new_range = 0
for a in my_range:
    if a % 3 == 0 or a % 5 == 0:
        new_range += a
print(new_range)
