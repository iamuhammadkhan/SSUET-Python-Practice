favourite_number = {'Khan': [1,2,3], 'Adil': [4,5,6], 'Waheed': [7,8,9]}

for a, b in favourite_number.items():
    print(a + ' favourite number are')
    for c in b:
        print(c)