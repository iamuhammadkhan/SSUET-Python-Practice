sandwich_orders = ['Club Sandwich', 'Tuna Sandwich', 'Special Sandwich', 'Pastrami Sandwich']

finished_sandwiches = []

for order in sandwich_orders:
    if order == 'Pastrami Sandwich':
        for i in range(1,4):
            print('I made your ' + order)
            finished_sandwiches.append(order)
    else:
        print('I made your ' + order)
        finished_sandwiches.append(order)

print(finished_sandwiches)

for i in finished_sandwiches:
    if i == 'Pastrami Sandwich':
        finished_sandwiches.remove(i)

print(finished_sandwiches)