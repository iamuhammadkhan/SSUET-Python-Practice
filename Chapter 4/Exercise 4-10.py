my_list = ['Pizza', 'Cold Drink', 'Cake', 'Roll', 'Ice Cream', 'Burger']
print("The first three foods are:")
print(my_list[:3])
print("Three items from the middle of the list are:")
length = len(my_list)
if length % 2 == 0:
    print(my_list[int(length / 2 - 1.5):int(length / 2 + 1.5)])
else:
    print(my_list[int(length / 2 - 1.5):int(length / 2 + 1.5)])
print("The last three items in the list are:")
print(my_list[-3:])