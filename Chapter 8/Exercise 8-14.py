new_cars = {}

def make_car(make, model, color = 'blue'):
    new_cars = {make: model}
    print('Your order has been received for ' + make + ', ' + model + ' in ' + color + ' color')

make_car('Sabaru', 'Outback')
print(new_cars)