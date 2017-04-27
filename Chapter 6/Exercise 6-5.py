rivers = {'Nile': 'Egypt', 'Sindh': 'Pakistan', 'Ganga': 'India'}

for i in set(rivers.keys()):
    for j in set(rivers.values()):
        if i == 'Nile' and j == 'Egypt':
            print('The ' + i + ' river is in ' + j)
        elif i == 'Sindh' and j == 'Pakistan':
            print('The ' + i + ' river is in ' + j)
        elif i == 'Ganga' and j == 'India':
            print('The ' + i + ' river is in ' + j)