pizzas = ["Pepperoni","Chicken Tikka","Hawaiian pizza","Italiano Crust","Crunchy Thin Crust"]
friend_pizzas = pizzas[:]
pizzas.insert(0,'Fajita')
friend_pizzas.insert(0,'Chicken Golden')
if pizzas == friend_pizzas:
	print("Both lists are same.")
else:
	print("Both lists are not same")

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("My friend’s favorite pizzas are")
for friend_pizza in friend_pizzas:
	print(friend_pizza)