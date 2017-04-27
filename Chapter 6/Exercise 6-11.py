cities = {'Karachi': {'country': 'Pakistan', 'population': '20000000', 'fact': 'It is the biggest city of pakistan'}, 'London': {'country': 'UK', 'population': '500000', 'fact': 'It is the most expensive city in the world'}}

for a, b in cities.items():
    print(a)
    details = 'is the city of ' + b['country'] + ' it has population of ' + b['population'] + ' and the fact is ' + b['fact']
    print(details)