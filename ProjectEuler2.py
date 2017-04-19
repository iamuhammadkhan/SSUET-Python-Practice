one = 1
two = 2
my_total = 2
for i in range(32):
    three = one + two
    one = two
    two = three
    if three % 2 == 0 and three < 4000000:
        my_total += three
print(my_total)